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
