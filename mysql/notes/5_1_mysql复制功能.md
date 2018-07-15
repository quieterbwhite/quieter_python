# mysql 复制功能

```
复制功能，增加多个从库，分担读负载，为高可用，灾难恢复，备份提供更过选择

二进制日志，重放，异步同步

TODO:
    页内目录跳转
```

## 复制解决了什么问题
```
实现在不同服务器上的数据分布

利用二进制日志增量进行

不需要太多的带宽

但是使用基于行的复制在进行大批量的更改时，会对带宽带来一定压力
特别是跨IDC环境进行复制应该分批进行

实现在不同服务器上的数据分布

实现数据读取的负载均衡
    需要其他组件配合完成，利用DNS轮询的方式把程序的读连接到不同的备份数据库
    使用LVS，haproxy这样的代理方式
    非共享架构，同样的数据分布在多台服务器上

增强了数据安全性
    利用备库的备份来减少主库的负载
    复制并不能代替备份

实现数据库高可用和故障切换
    方便进行数据库高可用架构的部署
    避免MySQL单点失败

实现数据库在线升级
```

# mysql 二进制日志
```
mysql 服务层日志

    二进制日志
        记录了所有对MySQL数据库的修改事件
        包括增删改查事件和对表结构的修改事件

        binlog 中的日志都是已经成功执行了的，而由于语法错误等问题导致的失败语句则没有被记录
    
    慢查日志
    
    通用日志

mysql 存储引擎层日志

    Innodb：重做日志，回滚日志
```

## 二进制日志格式
```
基于段的格式
    binlog_format=STATEMENT

    记录的sql语句，不需要特殊的工具等就能查看

    优点：
        日志记录量相对较小，节约磁盘及网络IO

    缺点:
        必须要记录上下文信息
        保证语句在从服务器上执行结果和在主服务器上相同

        特定函数如UUID(), user()
        这样非确定函数还是无法复制
        可能造成MySQL复制的主备服务器数据不一致

    查看当前使用的日志格式
        show variables like 'binlog_format';

    修改日志格式
        set session binlog_format=statement;
    
    查看binglog
        show binary logs;

    刷新binlog
        flush logs;

    查看日志
        $ cd /home/mysql/sql_log
        $ mysqlbinlog mysql-bin.000002

基于行的格式
    binlog_format=ROW

    ROW 是目前默认的日志格式
    ROW 格式可以避免mysql复制中出现的主从不一致问题

    同一sql语句修改了10000条数据的情况下
    基于段的日志格式只会记录这个sql语句
    基于行的日志格式会有10000条记录分别记录每一行的数据修改

    优点:
        使mysql主从复制更加安全
        对每一行数据的修改比基于段的高效
        主从复制的性能主要在于，从服务器重放语句的效率

        误操作而修改了数据库中的数据，同时又没有备份可以恢复时，
        我们就可以通过分析二进制日志，对日志中记录的数据修改操作做反向处理的方式来达到恢复数据的目的

    缺点:
        记录日志量大

        row,记录日志方式，默认FULL, 用这个就可以了
        binlog_row_image = FULL | MINIMAL | NOBLOB

        日志都是顺序写入的，所以对磁盘顺序io性能来说，影响不大

        show variables like 'binlog_row_image';

        $ mysqlbinlog -vv mysql-bin.000002 | less

        // 测试
        set session binlog_row_image=minimal

混合日志格式

    混合了基于段和基于行
    binlog_format=MIXED

    特点:
        根据sql语句由系统决定在基于段和基于行的日志格式中进行选择
        
        数据量的大小由所执行的SQL语句决定
```

## mysql二进制日志格式对复制的影响
```
基于sql语句的复制（SBR）
    二进制日志格式使用的是statement格式

    优点:
        生成的日志量少，节约网络传输IO
        并不强制要求主从数据库的表定义完全相同
        相比于基于行的复制方式更为灵活

    缺点:
        对于非确定性事件，无法保证主从复制数据的一致性
        对于存储过程，触发器，自定义函数进行的修改也可能造成数据不一致
        相比于基于行的复制方式在从上执行时需要更多的行锁

基于行的复制（RBR）
    二进制日志格式使用的是基于行的日志格式

    优点:
        可以应用于任何sql的复制包括非确定函数，存储过程等
        可以减少数据库锁的使用

    缺点：
        要求主从数据库的表结构相同，否则可能会中断复制
        无法在从上单独执行触发器

混合模式
    根据实际内容在以上两者间切换
```

## MySQL复制工作方式
```
1. 主将变更写入二进制日志

2. 从 读取 主 的二进制日志变更并写入到 relay_log 中

    基于日志点的复制
    基于GTID的复制

3. 在 从 上重放 relay_log 中的日志

    基于sql段的日志是在从库上重新执行记录的sql

    基于行的日志则是在从库上直接应用对数据库行的修改
```

## 基于日志点的复制
```
基于日志点的复制配置步骤

    在主DB服务器上建立复制账号

        创建复制用户
        create user 'repl' @ 'IP段' identified by 'Passw0rd';
        授权
        grant replication slave on *.* to 'repl' @ 'ip段';

    配置主数据库服务器

        // 启动MySQL的bin log并指定了名字
        bin_log = mysql-bin   // mysql-bin 开头的一系列文件
        // 动态参数，可以使用set命令进行赋值, 重启服务器该配置就没有了(造成异常)，还是需要在配置文件中指定
        server_id = 100  // 该值在集群中必须唯一

    配置从数据库服务器

        bin_log = mysql-bin
        server_id = 101
        // 这个参数在开启主从复制，会自动配置，但是名字是主机名字，主机名字有可能修改，所以还是要自己指定
        relay_log = mysql-relay-bin  // 中介日志名字

        log_slave_update = on [可选]  // 链路复制时必须，链路复制：从服务器作为其他服务器的主服务器

        read_only = on [可选]  // 从服务器上启用这个参数，让其不可写

    初始化从服务器数据

        同步早期主数据库中的数据

        mysqldump --master-data = 2-single-transaction

        // 用这个
        xtrabackup --slave-info

    启动复制链路

        change master to master_host = 'master_host_ip',
                master_user = 'repl',
                master_password = 'Passw0rd',
                master_log_file = 'mysql_log_file_name',
                master_log_pos = 4;

        实际操练:

            node_master node_slave

            node_master:

                create user repl@'192.168.3.%' identified by '123456';

                grant replication slave on *.* to repl'192.168.3.%';

            主从服务器配置文件修改

            复制主数据库数据

                主:
                    mysqldump --single-transaction --master-data --triggers --routines --all-databases -uroot -p >> all.sql

                    scp all.sql root@192.168.3.101:/root

                从：
                    mysql -uroot -p < all.sql

                    change master to master_host='192.168.3.101',
                    master_user='repl',
                    master_password='123456',
                    master_log_file='mysql-bin.000003', master_log_pos=1839; // 从all.sql中拷贝的

                    show slave status\G;

                    start slave;

                    show processlist; 

    优点:
        是MySQL最早支持的复制技术，bug相对较少
        对sql查询没有任务限制
        故障处理比较容易

    缺点：
        故障转移时重新获取新主的日志点信息比较困难
```

## 基于GTID的复制
```
基于日志的复制：
    从哪个二进制日志的偏移量进行增量同步
    如果指定错误会遗漏或重复
    造成主从数据不一致

基于GTID的复制
    从库告诉主库已执行事务的GTID值
    主库返回从库未执行事务的GTID值

    同一个事务只在指定的从库执行一次
    就可以避免由于数据偏移量不正确导致数据错误

什么是GTID

    全局事务id，其保证为每一个在主上提交的事务在复制集群中可以生成一个唯一的id

    GTID = source_id:transaction_id

    步骤:
        在主DB服务器上建立复制账号

            create user 'repl' @ 'ip段' identified by 'Passw0rd';

            grant replication slave on *.* to 'repl' @ 'ip段';

        配置主数据库服务器

            bin_log = /usr/local/mysql/log/mysql-bin

            server_id = 100 // 唯一

            gtid_mode = on  // 是否开启
            // 强制gtid一致性
            enforce-gtid-consiste

            log-slave-updates = on // < 5.7 版本需要

        配置从数据库服务器

            server_id = 101

            relay_log = /usr/local/mysql/log/relay_log

            gtid_mode = on

            enforce-gtid-consistency

            log-slave-updates = on

            read_only = on  // 保证从数据库服务器的安全性

            master_info_repository = TABLE

            relay_log_info_repository = TABLE
        
        初始化从服务器数据

            mysqldump --master-data=2 --single-transaction

            xtarbackup --slave-info

            启动基于GTID的复制
                change master to master_host = 'master_host_ip',
                    master_user = 'repl',
                    master_password = 'Passw0rd',
                    master_auto_position = 1  // 告诉从服务器使用GTID方式

        实际操作：
            查看复制用户是否已经建立：
                select user, host from user;

                show grants for repl@'192.168.3.%';

                有用户过后，修改配置文件，打开相关的几个设置项

                修改配置文件过后要重启

优点:
    可以方便进行故障转移

    从库不会丢失主库上的任何修改

缺点：
    故障处理比较复杂

    对执行的SQL有一定限制

选择复制模式要考虑的问题

    所使用的MySQL数据库的版本

    复制架构及主从切换的方式

    所使用的高可用管理组件

    对应用得支持程度
```

## MySQL复制拓扑
```
mysql 5.7 之前， 一个从库只能有一个主库
mysql 5.7 之后支持一从多主架构

一主多从的复制拓扑

    优点:
        配置简单
        可以用多个从库分担读负载

    用途：
        为不同的业务使用不同的从库
        将一台从库放到远程IDC中，用作灾备恢复
        分担主库的读负载

主主复制拓扑

    主备模式的主主复制

        同时只有一个主对外提供服务，只有在其出现问题时，另一个主才会替换其成为主

        一台服务器处于只读状态并且只作为热备使用

        在对外提供服务的主库出现故障或是计划性维护时才会进行切换,
        使原来的备库成为主库，而原来的主库会成为新的备库并处于只读或是下线状态，
        待维护完成后重新上线

        这种模式更常用一些, 作为一种高可用方案

        注意：
            确保两台服务器上的初始数据相同
            确保两台服务器上已经启动binlog并且有不同的server_id
            在两台服务器上启用log_slave_updates参数
            在初始的备库上启用read_only

    主主模式的主主复制

        两个主中所操作的表最好能够分开
        使用下面两个参数控制自增id的生成
            // 步长, 默认一
            auto_increment_increment = 2
            // 自增id从哪个值开始
            auto_increment_offset = 1 | 2

        注意：
            产生数据冲突而造成复制链路的中断
            耗费大量时间
            造成数据丢失

            除非没有其他办法，否则不建议使用这种复制模式

级联复制

    主库 -> 分发主库 -> 多个从库
```

## mysql复制性能优化
```
影响主从延迟的因素

    主库写入二进制日志的时间
        控制主库的事务大小，分割大事务

    二进制日志传输时间
        使用mixed日志格式

    默认情况下 从 只有一个sql线程，主上并发的修改在从上变成了串行
        多线程复制 >5.6
            在MySQL5.7中可以按照逻辑时钟的方式来分配sql线程

            如何配置多线程复制
                stop slave // 在从上停止链路复制  show slave status \G;
                // 如何使用多线程复制，逻辑时钟
                set global slave_parallel_type = 'logical_clock';
                // 并发处理的线程数
                set global slave_parallel_workers = 4;
                // 开启复制
                start slave;

            show variables like 'slave_parallel_type';

            show processlist\G
```

## mysql复制常见问题处理
```
由于数据损坏或丢失所引起的主从复制错误

    主库或从库意外宕机引起的错误
        使用跳过二进制日志事件
        注入空事务的方式先恢复中断的复制链路
        再使用其他方法来对比主从服务器上的数据

    主库上的二进制日志损坏
        通过 change master 命令来重新指定

    备库上的中继日志损坏

在从库上进行数据修改造成的主从复制错误

不唯一的server_id 或 server_uuid

max_allow_packet设置引起的主从复制错误

mysql复制无法解决的问题

    分担主数据库的写负载
        分库分表

    自动进行故障转移和主从切换
```