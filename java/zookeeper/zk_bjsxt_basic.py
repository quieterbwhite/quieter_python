# -*- coding=utf-8 -*-
# Created Time: 2017年08月07日 星期一 19时54分23秒
# File Name: zk_bjsxt_basic.py


"""
没有单节点部署的，最少是三个节点。推荐是奇数个节点。利于选举服务。

    ZAB   了解

    paxos   了解

    面试的时候会问，了解即可。

# 集群配置:

    tickTime=2000
    dataDir=/home/bwhite/software/zookeeper-3.4.10/data
    dataLogDir=/home/bwhite/software/zookeeper-3.4.10/log
    clientPort=2181

    #server.0 = 192.168.31.35:2888:3888
    #server.1 = 192.168.31.36:2888:3888
    #server.2 = 192.168.31.37:2888:3888

    # 每台服务器增加标识
    touch /home/bwhite/software/zookeeper-3.4.10/data/myid < 0
    touch /home/bwhite/software/zookeeper-3.4.10/data/myid < 1
    touch /home/bwhite/software/zookeeper-3.4.10/data/myid < 2

# 启动&停止&状态

    zkServer.sh start

    zkServer.sh status

        the output could be: leader or follower or standalone


# 命令行客户端

    ./zkCli.sh   # 进入 zookeeper 客户端

    gui客户端工具  ZooInspector   java -jar zookeeper-dev-ZooInspector.jar

    zookeeper 就是一个树形结构的东西。每个节点包括key, value

    value 可以使字符串，图片，文件，json字符串

# Java 操作 zookeeper

    1. zookeeper 原生API不会用。

    2. zdclient 也不会用

    3. curator-client 有最完美的 api, 工作中如果需要会使用它。


# 实现分布式锁

    原理就是 zookeeper, 对节点的操作是原子的。 所以，只要是能保证原子操作的都可以用来实现分布式锁。如: redis

    比如，有很多客户端都在对自己的信息进行修改，那么zk里面user节点下就会有多个子节点, 如:

       /user/1001, /user/1002, /user/1003

    app1 要操作1001用户，
        先查询 /user/1001 临时节点是否存在
            不存在， 创建临时节点 /user/1001(加锁), 继续之后的操作。操作完了，临时节点自己销毁了。
            存在，   等待 /user/1001 的锁释放

            操作: 操作是指: 数据持久化，数据库要主从同步完成。

    app2, 也要操作相同的数据时，先去 zookeeper 查询是否已有该节点。
        如果有，那么等待。
        如果没有，那么创建临时节点然后操作。

    为什么使用临时节点:

        效率高,

        get frist ？ 效率高

# 同步 & 异步 创建节点

    同步， 阻塞， 发送请求到收到结果，一个请求完成，接着往下执行。

    异步，非阻塞，发送请求，代码接着往下执行。新起一个线程监听 callback函数。



"""