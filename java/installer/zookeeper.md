# 安装 zookeeper
  -- Created Time: 2017年08月05日 星期六 19时53分22秒

Keeper 服务注册中心

ZooKeeper 是一个分布式的，开放源码的分布式应用程序协调服务。
它是一个为分布式应用提供一致性服务的软件，提供的功能包括：配置维护、域名服务、分布式同步、组服务等。

```
下载 ZooKeeper ，地址 http://www.apache.org/dyn/closer.cgi/zookeeper

http://apache.mirror.vexxhost.com/

解压 ZooKeeper

tar zxvf zookeeper-3.4.8.tar.gz
在 conf 目录新建 zoo.cfg ，照着该目录的 zoo_sample.cfg 配置如下。

cd zookeeper-3.3.6/conf
vim zoo.cfg
zoo.cfg 代码如下（自己指定 log 文件目录）：

    tickTime=2000
    dataDir=/javaee/zookeeper/data
    dataLogDir=/javaee/zookeeper/log
    clientPort=2181

在 bin 目录下，启动 ZooKeeper：

    cd zookeeper-3.3.6/bin
    ./zkServer.sh start
```
