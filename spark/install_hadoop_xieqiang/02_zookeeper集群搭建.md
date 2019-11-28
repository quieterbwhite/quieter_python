# 02 - zookeeper集群搭建

```shell
1，上传zookeeper-3.4.5.tar.gz安装包到dp-hadoop3上,解压到/bigdata目录下

2, 执行如下命令： cd  /bigdata/zookeeper/conf，cp zoo_sample.cfg zoo.cfg，vi zoo.cfg 添加如下内容：

dataDir=/bigdata/zookeeper-3.4.5/zk-data

server.1=172.16.0.83:2888:3888
server.2=172.16.0.84:2888:3888
server.3=172.16.0.85:2888:3888

3.创建目录/bigdata/zookeeper-3.4.5/zk-data，并创建文件myid,vi myid ,写入1

4，将改安装包scp 拷贝到dp-hadoop4和dp-hadoop5中，并分别修改其myid的值为2，和3

5.启动zk进程，在dp-hadoop3,dp-hadoop4,dp-hadoop5中分别执行如下命令：/bigdata/zookeeper-3.4.5/bin/zkServer.sh start
```



