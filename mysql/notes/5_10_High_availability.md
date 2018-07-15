# Mysql 高可用

## 什么是高可用架构
```
全年可用时间, 0.99999
```

## 如何实现高可用
```
避免导致系统不可用的因素, 减少系统不可用时间

    1. 建立完善的监控及报警系统
    2. 对备份数据进行恢复测试(定时测试)
    3. 正确配置数据库
    4. 对不需要的数据进行归档和清理(独立的表空间)

增加系统冗余，保证发生系统不可用时可以尽快恢复

    1. 避免存在单点故障

        利用SUN共享存储(不是好的方式)或DRDB磁盘复制解决MySQL单点故障

        利用多写集群或NDB集群来解决MySQL单点故障

        利用mysql主从复制来解决MySQL单点故障

        如何解决主服务器的单点问题：

            主服务器切换后如何通知应用新的主服务器的IP地址

            如何检查MySQL主服务器是否可用

            如何处理从服务器和新主服务器之间的那种复制关系

    2. 主从切换及故障转移

MMM(Multi-Master Replication Manager)

    主要作用:
        监控和管理MySQL的主主复制拓扑，并在当前的主服务器失效时，
        进行主和主备服务器之间的主从切换和故障转移工作。

    提供的功能:
        MMM监控MySQL主从复制健康状况
            主动主动模式的主主复制，两个主同时对外提供服务
            主动被动模式的主主复制，同时只有一个主数据库对外提供服务，另一个处于备用状态。MMM工作在这种模式下

        在主库出现宕机时进行故障转移并自动配置其他从对新主的复制
            如何找到从库对应的新的主库日志点的日志同步点
            如果存在多个从库出现数据不一致的情况如何处理
            在一个繁忙的系统，MMM对以上情况处理不够理想，可能会出现数据丢失情况

        提供了主，写虚拟ip， 在主服务器出现问题时可以自动迁移虚拟ip

    MMM架构

        主服务器

        主服务器(虚线)

        从，从，从。。

        MMM监控服务器

    MMM 部署所需资源有哪些
```
![MMM 资源](http://7sbqvw.com1.z0.glb.clouddn.com/github/mysql/github_mysql_mmm_setup_env.jpg)
```
    MMM 部署步骤
        1. 配置主主复制及主从同步集群
        2. 安装主从节点所需要的支持包
        3. 安装及配置MMM工具集
        4. 运行MMM监控服务

    MMM 演示拓扑
```
![mmm_02](http://7sbqvw.com1.z0.glb.clouddn.com/github/mysqlgithub_mysql_mmm_02.png)
```
    建立账号，
    $ mysql -uroot -p
    
    // 参考文章其他部分的创建用户，这里查看
    select user, host from mysql.user where user='repl';

    // 备份数据
    mysqldump --single-transaction --master-data=2 --all-databases -uroot -p > all.sql

    // 把主库备份的数据文件同步到其他从库上去
    scp all.sql 192.168.3.101:/root
    scp all.sql 192.168.3.102:/root

    // 从服务器上恢复数据
    mysql -uroot -p < all.sql

    // 配置复制链路
    change master to master_host='192.168.3.100',
    master_user='repl',
    master_password='123456',
    MASTER_LOG_FILE='mysql-bin.000001',MASTER_LOG_POS=154; // 去日志文件中找

    start slave; // 完成第一个主从复制

    show slave status \G

    show master status \G

    // 主主，到主服务器上配置到从服务器的复制链路
    change master to master_host='192.168.3.101',
    master_user='repl',
    master_password='123456',
    MASTER_LOG_FILE='mysql-bin.000002',MASTER_LOG_POS=1412692;

    start slave;

    show slave status \G

    // 在配置 3.102 为 3.100 的从服务器

    // 接下来就可以配置 MMM 集群
    // 每个服务器上安装
    $ yum install mysql-mmm-agent.noarch -y

    // 监控节点上安装监控需要的包
    yum -y install mysql-mmm*

    // 主服务器上创建 MMM 所需要的账号，在主服务器上创建时因为，会自动同步到其他服务器
    grant replication client on *.* to 'mmm_monitor'@'192.168.3.%' identified by '123456';

    grant super,replication_client,process on *.* to 'mmm_agent'@'192.168.3.%' identified by '123456';

    // 然后修改配置文件，服务器的地址，用户名，密码，写，读，等内容，没记录了。

    // 配置完成过后，就可以启动MMM集群

    // 首先启动三台服务器上的MMM代理
    /etc/init.d/mysql-mmm-agent start

    // 监控服务器上启动监控服务
    /etc/init.d/mysql-mmm-monitor start
    // 查看当前集群状态
    mmm_control show

    // 状态正确过后我们就可以测试故障转移等功能
    // 停止主服务器。观察从服务器是否正确完成故障转移功能
```

## MMM工具的优缺点
```
优点:
    使用Perl脚本语言开发及完全开源

    提供了读写Vip(虚拟ip)，使服务器角色的变更对前端应用透明
        在从服务器出现大量的主从延迟，主从链路中断时，
        可以把这台从服务器上的读的虚拟ip，漂移到集群中其他正常的服务器上。

    MMM提供了从服务器的延迟监控

    MMM提供了主数据库故障转移后从服务器对新主的重新同步功能

    很容易对发生故障的主数据库重新上线

缺点：
    发布时间比较早不支持mysql新的复制功能，6年前发布的新版本，有bug

    没有读负载均衡功能

    在进行主从切换时，容易造成数据丢失

    MMM监控服务存在单点故障
```

## MHA(Master High Availability)
```
    由 perl 语言开发

    更多关注的是主从复制中的主db

    使用GTID的复制模式

    MHA完成主从切换超高效，30秒内完成主从切换，最大程度保证数据一致性，达到真正意义上的高可用

    MHA提供了什么功能

        监控主数据库服务器是否可用

        当主DB不可用时，从多个服务器中选举出新的主数据库服务器

        提供了主从切换和故障转移功能

    MHA是如何进行主从切换的

        尝试从出现故障的主数据库保存二进制日志

        从多个备选从服务器中选举出新的备选主服务器
            可以人为设置某些机器不参与选举

        在备选主服务器和其他从服务器之间同步差异二进制数据

        应用从原主DB服务器上保存的二进制日志
            重复的主键等会使MHA停止进行故障转移

        提升备选主DB服务器为新的主DB服务器

        迁移集群中的其他从DB作为新的主DB的从服务器
```
![mha_jiagou](http://7sbqvw.com1.z0.glb.clouddn.com/github/mysqlgithub_mysql_mha_02.png)
```
    MHA 支持 GTID 的复制模式
    MMM 不支持 GTID 的复制模式

    MHA 配置步骤

        配置集群内所有主机的SSH免认证登录

        安装 MHA-node 软件包 和 MHA-master软件包
        MHA-node 安装到所有机器
        MHA-master 安装到监控服务器上

        建立主从复制集群
        配置MHA管理节点
        使用masterha_check_ssh 和 masterha_check_repl 对配置进行检验
        启动并测试MHA服务

    安装部署详细过程不表。预知详情，请查看视频教程。
```

## MHA优缺点
```
优点:
    同样是由Perl语言开发的开源工具

    可以支持基于GTID的复制模式

    MHA在进行故障转移时更不易产生数据丢失

    同一个监控节点可以监控多个集群

缺点:
    需要编写脚本或利用第三方工具来实现Vip配置

    MHA启动后只会对主数据库进行监控

    需要ssh免认证登录，存在一定安全隐患
```

## 读写分离
```
读写分离和负载均衡是两个不同的概念

程序实现读写分离
    优点：
        有开发人员控制什么样查询在从库中执行，因此比较灵活

        由程序直连数据库，所以性能损耗比较小

    缺点：
        增加了开发工作量，使程序代码更加复杂

        人为使用数据库，容易出错

中间件实现读写分离
    优点：
        由中间件根据查询语法分析，自动完成读写分离

        对程序透明，对于已有程序不用做任何修改

    缺点：
        由于增加了中间层，所以对查询效率有损耗

        对于延迟敏感业务无法自动在主库执行

    读的负载均衡主要解决的是具有相同角色的数据库如何共同分担相同的负载
    软件：
        LVS
        Haproxy
        MaxScale
    硬件:
        F5
```

## MaxScale
```
MaxScale 插件
    Authentication 认证插件
    Protocol 协议插件
    Router 路由插件
        readconnroute
        readwritesplit
    Monitor 监控插件
    Filter&Logging 日志和过滤插件

安装
    pass
```
最终的高可用架构:
![maxscale](http://7sbqvw.com1.z0.glb.clouddn.com/github/mysqlgithub_mysql_maxscale.png)