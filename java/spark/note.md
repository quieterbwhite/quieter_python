#### spark 日志清晰项目笔记

[hadoop&hdfs环境搭建](#hadoop&hdfs环境搭建)  
[环境变量](#环境变量)  
[资源调度框架Yarn](#资源调度框架Yarn)  
  [Yarn产生背景](#Yarn产生背景)  
  [Yarn架构](#Yarn架构)  
  [Yarn执行流程](#Yarn执行流程)  

##### hadoop&hdfs环境搭建
```
参考搭建单机环境官方文档:
http://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/SingleCluster.html

1. 安装jdk环境
2. 下载hadoop安装包 http://archive.cloudera.com/cdh5/cdh/5/
3. hadoop-env.sh 修改
4. core-site.xml 修改
5. hdfs-site.xml 修改
6. 格式化hdfs,只需安装时执行一次
7. 起停hdfs
8. dfs命令

cd /home/bwhite/software/hadoop-2.5.0-cdh5.3.6/etc/hadoop

hadoop-env.sh 修改

    export JAVA_HOME=/home/bwhite/software/jdk1.8.0_131

core-site.xml 修改
    
    <configuration>
        <property>
            <name>fs.defaultFS</name>
            <value>hdfs://localhost:9000</value>
        </property>
        
        <property>
            <name>hadoop.tmp.dir</name>
            <value>/home/bwhite/data/tmp</value>
        </property>
    </configuration>
    
hdfs-site.xml 修改

    <configuration>
        <property>
            <name>dfs.name.dir</name>
            <value>/home/bwhite/data/hadoop/namenode</value>
        </property>

        <property>
            <name>dfs.data.dir</name>
            <value>/home/bwhite/data/hadoop/datanode</value>
        </property>

        <property>
            <name>dfs.tmp.dir</name>
            <value>/home/bwhite/data/hadoop/tmp</value>
        </property>

        <property> 副本的数量
            <name>dfs.replication</name>
            <value>1</value>
        </property>

    </configuration>

格式化hdfs,只需安装时执行一次

    cd /home/bwhite/software/hadoop-2.5.0-cdh5.3.6/bin

    $ bin/hdfs namenode -format

开启hdfs

    cd /home/bwhite/software/hadoop-2.5.0-cdh5.3.6/sbin

    $ ./start-dfs.sh 
        19/06/07 17:00:18 WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
        Starting namenodes on [localhost]
        bwhite@localhost's password: 
        localhost: starting namenode, logging to /home/bwhite/software/hadoop-2.5.0-cdh5.3.6/logs/hadoop-bwhite-namenode-os.out
        bwhite@localhost's password: 
        localhost: starting datanode, logging to /home/bwhite/software/hadoop-2.5.0-cdh5.3.6/logs/hadoop-bwhite-datanode-os.out
        Starting secondary namenodes [0.0.0.0]
        bwhite@0.0.0.0's password: 
        0.0.0.0: starting secondarynamenode, logging to /home/bwhite/software/hadoop-2.5.0-cdh5.3.6/logs/hadoop-bwhite-secondarynamenode-os.out
        19/06/07 17:00:42 WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable

    $ jps
        11617 Jps
        11495 SecondaryNameNode
        11161 NameNode
        11309 DataNode
        
    浏览器访问 http://localhost:50070

    查看文件系统
    $ hadoop fs -ls /
        19/06/07 17:05:29 WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
        Found 2 items
        drwxr-xr-x   - bwhite supergroup          0 2019-05-31 22:28 /home
        -rw-r--r--   1 bwhite supergroup       1859 2019-06-01 17:46 /spark.txt

停止hdfs

    $ ./stop-dfs.sh

dfs命令

    创建文件夹
    $ hadoop fs -mkdir /test/

    递归查看目录
    $ hadoop fs -ls -R /

    上传目录
    $ hadoop fs -put srcfile /test/

    查看内容
    $ hadoop fs -text /test/srcfile
    $ hadoop fs -cat /test/srcfile

    下载文件
    $ hadoop fs -get /test/srcfile /tmp/srcfile

    删除文件
    $ hadoop fs -rm /test/srcfile
    $ hadoop fs -rmr /test/srcfile
```

##### 资源调度框架Yarn
###### Yarn产生背景
```
1. MapReduce1.x 存在的问题
2. 资源利用率和运维成本
3. 催生了Yarn的诞生
```

###### Yarn架构
```
Client:
    pass

Resource Manager:
    一个集群Active状态的RM只有一个
    负责整个集群的资源管理和调度
    处理客户端的请求(启动/关闭)
    启动/监控ApplicationMaster(一个作业对应一个AM)
    监控Node Manager, 通过心跳
    一个Resource Manager对多个Node Manager

Node Manager:
    整个集群中有N个，负责单个节点的资源管理和使用以及task的运行情况
    接收并处理RM的container启动停止的各种命令
    单个节点的资源管理和任务管理

Application Manager:
    每个应用/作业对应一个, 负责应用程序的管理
    数据切分
    为应用程序向RM申请资源, 并分配给内部任务
    与NM通信以启停task, task是运行在container中的
    task的监控和容错

Container:
    pass
```

###### Yarn执行流程
```
1. 用户向Yarn提交作业
2. RM为该作业分配第一个container(AM)
3. RM会与对应的NM通信，要求NM在这个container上启动应用程序的AM
4. AM首先像RM注册，然后AM将为各个任务申请资源，并监控运行情况
5. AM采用轮训方式通过RPC协议向RM申请和领取资源
6. AM申请到资源以后，便和相应的NM通信，要求NM启动任务
7. NM启动我们作业对应的task
```

##### 环境变量
```
GRADLE_HOME=/home/bwhite/software/gradle-4.0.1
PATH=$GRADLE_HOME/bin:$PATH

PROTOC_HOME=/home/bwhite/software/protoc-3.3.0-linux-x86_64/bin
PATH=$PROTOC_HOME:$PATH

JAVA_HOME=/home/bwhite/software/jdk1.8.0_131
HADOOP_HOME=/home/bwhite/software/hadoop-2.5.0-cdh5.3.6
HIVE_HOME=/home/bwhite/software/hive-0.13.1-cdh5.3.6
ZOOKEEPER_HOME=/home/bwhite/software/zookeeper-3.4.10
SCALA_HOME=/home/bwhite/software/scala-2.11.4
SPARK_HOME=/home/bwhite/software/spark-1.3.0-bin-hadoop2.4

PATH=$JAVA_HOME/bin:$JAVA_HOME/jre/bin:$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$HIVE_HOME/bin:$ZOOKEEPER_HOME/bin:$SCALA_HOME/bin:$SPARK_HOME/
bin:$PATH

CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar:$JAVA_HOME/lib:$JAVA_HOME/jre/lib:$JAVA_HOME/jre/lib/rt.jar:$CLASSPATH
```