# 03 - hadoop集群搭建

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

