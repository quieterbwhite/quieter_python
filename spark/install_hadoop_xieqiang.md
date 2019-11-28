#### 安装原生hadoop

##### [环境及软件版本信息](http://confluence.dev.lhjksaas.com/pages/viewpage.action?pageId=11632872)

|                       | hive                          |                               |                           |                           |                           |
| --------------------- | ----------------------------- | ----------------------------- | ------------------------- | ------------------------- | ------------------------- |
|                       | hbase集群，zk集群             |                               |                           |                           |                           |
| hadoop集群，spark集群 |                               |                               |                           |                           |                           |
|                       | dp-hadoop1（172.16.0.81）     | dp-hadoop2（172.16.0.82）     | dp-hadoop3（172.16.0.83） | dp-hadoop4（172.16.0.84） | dp-hadoop5（172.16.0.85） |
| 运行进程1             | hadoop-namenode               | hadoop-namenode               | hive                      |                           |                           |
| 运行进程2             | hadoop-datanode               | hadoop-datanode               | hadoop-datanode           | hadoop-datanode           | hadoop-datanode           |
| 运行进程3             | spark-master                  | ResourceManager               | mysql                     |                           |                           |
| 运行进程4             | spark-slave1                  | spark-slave2                  | spark-slave3              | spark-slave4              | spark-slave5              |
| 运行进程5             | DFSZKFailoverController(zkfc) | DFSZKFailoverController(zkfc) | HRegionServer             | HRegionServer             | Hmaster                   |
| 运行进程6             | ResourceManager               |                               | ntp-server(时间服务器)    |                           |                           |
| 运行进程7             |                               |                               | zk1                       | zk2                       | zk3                       |
| 运行进程8             |                               |                               | JournalNode               | JournalNode               | JournalNode               |
| 配置                  | 4g/500g/2core                 | 4g/500g/2core                 | 4g/500g/2core             | 4g/500g/2core             | 4g/500g/2core             |

说明：1,dp-hadoop3,作为时间服务器，集群中的每个节点每天凌晨1点向时间服务器同步时间（避免节点间因时间不同步带来的不可预期的异常），

​           2,所有机器均安装jdk 1.8+

​           3，所有软件安装目录为：/bigdata

​          4，所有机器的hosts配置文件添加如下的内容：

172.16.0.81 dp-hadoop1
172.16.0.82 dp-hadoop2
172.16.0.83 dp-hadoop3
172.16.0.84 dp-hadoop4
172.16.0.85 dp-hadoop5

##### 软件版本

| 软件      | 版本  |
| --------- | ----- |
| hadoop    | 2.6.4 |
| hive      | 2.3.5 |
| spark     | 2.3.3 |
| habse     | 1.3.3 |
| zookeeper | 3.4.5 |

#### [zookeeper集群搭建](http://confluence.dev.lhjksaas.com/pages/viewpage.action?pageId=11632979)

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

##### [hadoop集群搭建](http://confluence.dev.lhjksaas.com/pages/viewpage.action?pageId=11632990)

```shell
1，上传hadoop-2.6.4.tar.gz安装包到dp-hadoop1上并解压到/bigdata目录

2，修改环境变量,添加如下内容

vim /etc/profile

export JAVA_HOME=/bigdata/jdk1.8.0_191/
export HADOOP_HOME=/bigdata/hadoop-2.6.4/
export PATH=$PATH:$JAVA_HOME/bin:$HADOOP_HOME/bin:$HADOOP_HOME/sbin

3，修改配置文件hadoop-env.sh

cd /bigdata/hadoop-2.6.4/etc/hadoop/

vi hadoop-env.sh

添加如下内容：

export JAVA_HOME=/bigdata/jdk1.8.0_191/

4,修改配置文件core-site.xml,内容为

<configuration>
<!-- 指定hdfs的nameservice为dp -->
<property>
<name>fs.defaultFS</name>
<value>hdfs://dp/</value>
</property>
<!-- 指定hadoop临时目录 -->
<property>
<name>hadoop.tmp.dir</name>
<value>/bigdata/hadoop-2.6.4/hadoop-data</value>
</property>

<!-- 指定zookeeper地址 -->
<property>
<name>ha.zookeeper.quorum</name>
<value>172.16.0.83:2181,172.16.0.84:2181,172.16.0.85:2181</value>
</property>
</configuration>

修改hdfs-site.xml，内容为：

<configuration>

<!--指定hdfs的nameservice为dp，需要和core-site.xml中的保持一致 -->
<property>
<name>dfs.nameservices</name>
<value>dp</value>
</property>
<!-- bi下面有两个NameNode，分别是nn1，nn2 -->
<property>
<name>dfs.ha.namenodes.dp</name>
<value>nn1,nn2</value>
</property>
<!-- nn1的RPC通信地址 -->
<property>
<name>dfs.namenode.rpc-address.dp.nn1</name>
<value>172.16.0.81:9000</value>
</property>
<!-- nn1的http通信地址 -->
<property>
<name>dfs.namenode.http-address.dp.nn1</name>
<value>172.16.0.81:50070</value>
</property>
<!-- nn2的RPC通信地址 -->
<property>
<name>dfs.namenode.rpc-address.dp.nn2</name>
<value>172.16.0.82:9000</value>
</property>
<!-- nn2的http通信地址 -->
<property>
<name>dfs.namenode.http-address.dp.nn2</name>
<value>172.16.0.82:50070</value>
</property>
<!-- 指定NameNode的edits元数据在JournalNode上的存放位置 -->
<property>
<name>dfs.namenode.shared.edits.dir</name>
<value>qjournal://172.16.0.83:8485;172.16.0.84:8485;172.16.0.85:8485/dp</value>
</property>
<!-- 指定JournalNode在本地磁盘存放数据的位置 -->
<property>
<name>dfs.journalnode.edits.dir</name>
<value>/bigdata/hadoop-2.6.4/journaldata</value>
</property>
<!-- 开启NameNode失败自动切换 -->
<property>
<name>dfs.ha.automatic-failover.enabled</name>
<value>true</value>
</property>
<!-- 配置失败自动切换实现方式 -->
<property>
<name>dfs.client.failover.proxy.provider.dp</name>
<value>org.apache.hadoop.hdfs.server.namenode.ha.ConfiguredFailoverProxyProvider</value>
</property>
<!-- 配置隔离机制方法，多个机制用换行分割，即每个机制暂用一行-->
<property>
<name>dfs.ha.fencing.methods</name>
<value>
sshfence
shell(/bin/true)
</value>
</property>
<!-- 使用sshfence隔离机制时需要ssh免登陆 -->
<property>
<name>dfs.ha.fencing.ssh.private-key-files</name>
<value>/home/root/.ssh/id_rsa</value>
</property>
<!-- 配置sshfence隔离机制超时时间 -->
<property>
<name>dfs.ha.fencing.ssh.connect-timeout</name>
<value>30000</value>
</property>
</configuration>

修改：mapred-site.xml内容为：

<configuration>
<!-- 指定mr框架为yarn方式 -->
<property>
<name>mapreduce.framework.name</name>
<value>yarn</value>
</property>
</configuration>

修改yarn-site.xml内容为：

<configuration>

<!-- Site specific YARN configuration properties -->

<!-- 开启RM高可用 -->
<property>
<name>yarn.resourcemanager.ha.enabled</name>
<value>true</value>
</property>
<!-- 指定RM的cluster id -->
<property>
<name>yarn.resourcemanager.cluster-id</name>
<value>dpycl</value>
</property>
<!-- 指定RM的名字 -->
<property>
<name>yarn.resourcemanager.ha.rm-ids</name>
<value>rm1,rm2</value>
</property>
<!-- 分别指定RM的地址 -->
<property>
<name>yarn.resourcemanager.hostname.rm1</name>
<value>172.16.0.83</value>
</property>
<property>
<name>yarn.resourcemanager.hostname.rm2</name>
<value>172.16.0.84</value>
</property>

<!-- 指定zk集群地址 -->
<property>
<name>yarn.resourcemanager.zk-address</name>
<value>172.16.0.83:2181,172.16.0.84:2181,172.16.0.85:2181</value>
</property>
<property>
<name>yarn.nodemanager.aux-services</name>
<value>mapreduce_shuffle</value>
</property>
</configuration>

修改slaves文件，内容为：

172.16.0.81
172.16.0.82
172.16.0.83
172.16.0.84
172.16.0.85

5，配置hd-hadoop1到dp-hadoop1,hd-hadoop2,dp-hadoop3,dh-hadoop4,dp-hadoop5的免密登录

6，将4步中修改好的hadoop安装包分别拷贝到hd-hadoop2,dp-hadoop3,dh-hadoop4,dp-hadoop5中

7，在hd-hadoop1中格式化hdfs文件系统，执行如下命令：

        hdfs namenode -format

   将格式化后生成的文件夹：/bigdata/hadoop-2.6.4/hadoop-data 拷贝到dp-hadoop2同目录中

8，格式化zkfc

    hdfs zkfc -formatZK

9,启动HDFS(在dp-hadoop1上执行)
   sbin/start-dfs.sh

10,启动yarn:

sbin/start-yarn.sh



启动成功后可通过：http://172.16.0.82:50070/dfshealth.html#tab-overview 查看hadoop集群信息
```

##### [spark集群搭建](http://confluence.dev.lhjksaas.com/pages/viewpage.action?pageId=11632994)

```shell
1，上传spark-2.3.2-bin-hadoop2.6.tgz安装包到dp-hadoop1 /bigdata目录下

2，修改spark配置文件

 vim /bigdata/spark-2.3.3-bin-hadoop2.6/conf/spark-env.sh

添加如下内容：

export JAVA_HOME=/bigdata/jdk1.8.0_191/
export SPARK_MASTER=172.16.0.81
export SPARK_MASTER_PORT=7077
export SPARK_WORKER_CORES=2
export SPARK_WORKER_MEMORY=3g

 vim /bigdata/spark-2.3.3-bin-hadoop2.6/conf/slaves：

添加如下内容

172.16.0.81
172.16.0.82
172.16.0.83
172.16.0.84
172.16.0.85

3，将修改后的安装包拷贝到dp-hadoop2,dp-hadoop3,dp-hadoop4,dp-hadoop5的同目录中


4，在dp-hadoop1中执行如下命令启动spark集群：

 /bigdata/spark-2.3.3-bin-hadoop2.6/sbin/start-all.sh


启动成功后可通过：http://172.16.0.81:8080/ 查看spark集群信息
```

