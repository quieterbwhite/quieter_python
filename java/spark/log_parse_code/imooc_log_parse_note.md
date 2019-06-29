#### spark 日志清洗项目笔记

[hadoop&hdfs环境搭建](#hadoop&hdfs环境搭建)  
    
[资源调度框架Yarn](#资源调度框架Yarn)  
__[Yarn产生背景](#Yarn产生背景)  
__[Yarn架构](#Yarn架构)  
__[Yarn执行流程](#Yarn执行流程)  
__[Yarn环境搭建](#Yarn环境搭建)  

[HIVE](#HIVE)  
__[Hive产生的背景](＃Hive产生的背景)  

[Spark](#Spark)  
__[Spark产生背景](#Spark产生背景)  
__[Spark概述及特点](#Spark概述及特点)  
    
[SparkSQL](#SparkSQL)  
__[]()  
    
[环境变量](#环境变量)  

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

###### Yarn环境搭建
```
使用版本: hadoop-2.6.0-cdh5.7.0

yarn-site.xml修改

    <configuration>
        <property>
            <name>yarn.nodemanager.aux-services</name>
            <value>mapreduce_shuffle</value>
        </property>
    </configuration>

mapred-site.xml修改

    <configuration>
        <property>
            <name>mapreduce.framework.name</name>
            <value>yarn</value>
        </property>
    </configuration>

启动yarn

    $ sbin/start-yarn.sh

停止yarn

    $ sbin/stop-yarn.sh

检查启动是否成功

    $ jps
        26907 ResourceManager
        27263 NodeManager

    访问网页: http://localhost:8088

MapReduce作业提交到YARN上运行

    hadoop jar 的使用
        使用自带的例子:
        # hadoop jar /home/bwhite/software/hadoop-2.5.0-cdh5.3.6/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.5.0-cdh5.3.6.jar wordcount /spark.txt /new
        注意: 输出目录必须是空目录

        到 http://localhost:8088 查看任务运行情况
        到 http://localhost:50070 查看文件系统时候有输出结果

        查看输出内容:
        $ hadoop fs -ls /new/
        $ hadoop fs -text /new/part-r-00000
```

##### HIVE
###### Hive产生的背景
```
1. MapReduce编程的不便性
2. HDFS上的文件缺少Schema
```

##### Hive是什么
```
1. 由facebook开源，最初用于解决海量结构化的日志数据统计问题
2. 构建在hadoop上的数据仓库
3. Hive定义了一种类SQL查询语言，HQL
4. 通常用于进行离线数据处理
5. 底层支持多种不同的执行引擎
    Hive on MapReduce
    Hive on Tez
    Hive on Spark
6. 支持多种不同的压缩格式，存储格式以及自定义函数
    GZIP
    LZO
    Snappy
    BZIp2

    TextFile
    SequenceFile
    RCFile
    ORC
    Parquet

    自定义函数
```

###### 为什么要使用Hive
```
1. 简单，容易上手，类似sql
2. 为超大数据集设计的计算/存储扩展能力(MR计算，HDFS存储)
3. 统一的元数据管理(可与Presto,Impala,SparkSQL等共享数据)
```

###### Hive的发展历程
```
1. 2007-08 Journey start from facebook
2. 2013-05 Hive 0.11.0
3. 2013-10 Hive 0.12.0
4. 2014-04 Hive 0.13.0
5. 2014-11 Hive 0.14.0
6. 2015-01 Hive 1.0.0
7. 2016-06 Hive 2.1.0
```

###### Hive体系架构
```

```

###### Hive环境搭建
```
1. 下载解压
2. 配置环境变量
3. 修改hive-env.xml文件

    增加　HADOOP_HOME=/home/bwhite/software/hadoop-2.5.0-cdh5.3.6

4. 修改hive-site.xml文件

    <property>
        <name>javax.jdo.option.ConnectionURL</name>
        <value>jdbc:mysql://192.168.31.234:3306/hive_metadata?createDatabaseIfNotExist=true&amp;useSSL=false</value>
        <description>JDBC connect string for a JDBC metastore</description>
    </property>

    <property>
        <name>javax.jdo.option.ConnectionDriverName</name>
        <value>com.mysql.jdbc.Driver</value>
        <description>Driver class name for a JDBC metastore</description>
    </property>

    <property>
        <name>javax.jdo.option.ConnectionUserName</name>
        <value>hive</value>
        <description>username to use against metastore database</description>
    </property>

    <property>
        <name>javax.jdo.option.ConnectionPassword</name>
        <value>hive</value>
        <description>password to use against metastore database</description>
    </property>

    <property>
        <name>hive.metastore.warehouse.dir</name>
        <value>/home/bwhite/data/hive</value>
        <description>location of default database for the warehouse</description>
    </property>

5. 将mysql-connecter-java-5.1.27-bin.jar放到hive/lib下

6. 启动hive

    $ hive/bin/hive
```

###### Hive的基本使用
```
1. 创建表

    create table hive_wordcount(context string);

2. 加载数据到hive表

    load data local inpath '/tmp/word.txt' into table hive_wordcount;

2. 使用 Hive 完成　wordcount 统计(对比MapReduce实现的易用性)

    select word, count(1) from hive_wordcount lateral view explode(split(context, '\t')) wc as word group by word;

    lateral view explode(); 是把每行记录按照指定分隔符进行拆解

    hive sql 提交执行以后会生成mr作业，并在yarn上运行

3. 另一个例子

    create table emp(
        empno int,
        ename string,
        job string,
        mgr int,
        hiredate string,
        sal double,
        comm double,
        deptno int
    ) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t';

    create table dept(
        deptno int,
        dname string,
        location string
    ) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t';

    load data local inpath '/tmp/tmp.txt' into table emp;
    load data local inpath '/tmp/dept.txt' into table dept;

    求每个部门的人数

        select deptno, count(1) from emp group by deptno;
```

#### Spark
##### Spark产生的背景
```
1. MapReduce的局限性
2. 框架多样化
    批处理(离线): MapReduce, Hive, Pig
    流式处理(实时): Storm, JStorm
    交互计算: Impala
```
##### 实战环境搭建
```
1. Spark源码编译

    从官网下载Spark源码
    http://spark.apache.org/docs/latest/building-spark.html

    mvn 编译

    make-distribution.sh 编码

2. Local模式

    不管

3. Standalone 模式

    修改spark-env.sh, 添加如下:

        酌情修改这部分内容: 
            # Options for the daemons used in the standalone deploy mode
            SPARK_MASTER_IP=127.0.0.1
            SPARK_WORKER_MEMORY=1g
 
            export JAVA_HOME=/home/bwhite/software/jdk1.8.0_131
            export SCALA_HOME=/home/bwhite/software/scala-2.11.4
            export HADOOP_CONF_DIR=/home/bwhite/software/hadoop-2.5.0-cdh5.3.6/etc/hadoop

    检查时候启动成功:

        成功进入命令行
        ./bin/spark-shell --master local[4]

        ./bin/spark-shell --master spark://localhost:7077

        访问
            http://localhost:4040

            http://localhost:8080

Spark简单使用, wordcount统计

    val file = spark.sparkContext.textFile("file:///tmp/wc.txt")
    val wordCounts = file.flatMap(line => line.split(",")).map((word=>(word,1))).reduceByKey(_ + _)
    wordCounts.collect
```

#### SparkSQL
##### 从Hive平滑过度到SparkSQL
```
1.x SQLContext/HiveContext
2.x SparkSession

spark-shell/spark-sql的使用

thriftserver/beeline的使用

jdbc方式编程访问
```

###### 创建Maven项目
```
通过Maven创建scala项目
在idea中选择maven, 选在scala简单项目，填写项目各种配置即可

pom.xml文件中修改scala版本

编写 SQLContextAPP, 代码参考该课程的源码

编译，打包

    $ cd ImoocSparkSQLProject
    $ mvn clean package -DskipTests

将编译打包的结果上传服务器

    $ scp target/sql-1.0.jar server:/tmp/    

提交应用, 命令行执行:

    ./bin/spark-submit \
    --name myname \
    --class com.imooc.spark.SQLContextApp \
    --master local[2] \
    /tmp/sql-1.0.jar \
    /tmp/src.json 

    工作中一般是将命令写到脚本里面, touch sqlcontext.sh, 添加执行权限, 将上面的命令写到里面就可以了
```

###### HiveContext
```
Spark1.x中SparkSQL的入口点: HiveContext

val sqlContext = new org.apache.spark.sql.hive.HiveContext(sc)

参考课程源码: HiveContextApp.scala

编译，打包，上传，运行

命令中加载外部jar包

    --jars /tmp/mysql.jar
``` 

###### SparkSession
```
Spark2.x中SparkSQL的入口点: SparkSession

val spark = SparkSession
    .builder()
    .appName("Spark SQL basic example")
    .config("spark.some.config.option", "some-value")
    .gerOrCreate()

参考课程源码 SparkSessionApp.scala
```

###### SparkShell & SparkSQL
```
./spark-shell --master local[2] --jars /tmp/mysql.jar

./spark-sql --master local[2] --jars /tmp/mysql.jar
```

###### thriftserver/beeline
```
启动服务器, 默认端口是10000

    ./start-thriftserver.sh --master local[2] --jars /tmp/mysql.jar

    jps -m

通过beeline客户端连接:

    beeline -u jdbc:hive2://localhost:10000 -n hadoop 

    连接上之后就可以写sql语句了

    select * from tmp e join dept d on e.deptno=d.deptno
```

###### thriftserver/beeline & spark-shell/spark-sql 的区别
```
1. spark-shell, spark-sql 都是一个spark application
2. thriftserver 不管你启动多少个客户端(beeline/code), 永远都是一个 spark application
    解决数据共享问题, 多个客户端可以共享数据
```

##### DataFrame&Dataset
###### DataFrame产生背景
```
Dataset 是一个分布式的数据集

DataFrame 以列的形式构成的分布式数据集

    列名　列类型　列值
```

###### DataFrame对比RDD
###### DataFrame基本API常用操作
```
create dataframe
printSchema
show
select
filter
参考源码 DataFrameApp.scala
```
###### DataFrame和RDD的互操作
```
参考源码 DataFrameRDDApp.scala

1. 反射 case class, 前提，事先需要知道你的字段，字段类型

2. 编程, 我觉得第二种简单点，我用第二种
```
###### DataFrame_API实战
```
学生信息统计案例

参考源码 DataFrameCase.scala
```
###### Datasets
```
参考源码 DatasetApp.scala
```

##### Yarn
```
Spark支持4中运行模式
1. Local, 开发使用
2. Standalone, Spark自带的,需要在多台机器上同时部署spark环境
3. Yarn, 生产使用,使用Yarn进行整个集群的资源调度
4. mesos

不管使用什么模式，Spark应用程序的代码是一模一样的，只需要在提交的时候通过
--master参数指定运行模式即可

Client
    Driver运行在Client端(提交Spark作业的机器)
    Client会和请求的Container进行通信来完成作业的调度和执行，Client不能退出

    日志信息在控制台

./bin/spark-submit \
--class org.apache.spark.examples.SparkPi \
--master yarn \
--executor-memory 1G \
--num-executors 1 \
/path/to/examples.jar \
4

首先要启动程序:
start-dfs.sh
start-yarn.sh
http://localhost:8088 查看 yarn 的运行情况

如果想运行在yarn上, 需要配置环境变量 spark-env.sh

Cluster
    Driver运行在ApplicationMaster中
    Client只要提交完作业就可以关掉，因为作业已经在Yarn上运行了

    日志在终端看不到，日志在Driver上，只能通过yarn logs -applicationId application_xxx 查看

    在网页上也可以看到

Spark on Yarn 两种模式对比

1. Driver的运行位置

2. ApplicationMaster的职责

3. 日志的位置

就是这两个参数区别两种模式:

    --master yarn, 默认是client模式

    --master yarn-cluster, Cluster模式
```

###### 将我们的项目运行在Yarn上
```
1. 将我们的项目通过maven进行打包

    参考源码: SparkStatCleanJobYARN.scala

    打包, pom.xml中需要添加plugin
        <plugin>
          <artifactId>maven-assembly-plugin</artifactId>
          <configuration>
            <archive>
              <manifest>
               
              </manifest>
            </archive>
            <descriptorRefs>
              <descriptorRef>jar-with-dependencies</descriptorRef>
            </descriptorRefs>
          </configuration>
        </plugin>
        
    mvn assembly:assembly
    
    到 target　目录下查看结果包

2. 通过spark-submit方式提交

    ./bin/spark-submit \
    --class org.apache.spark.examples.SparkPi \
    --master yarn \
    --executor-memory 1G \
    --num-executors 1 \
    --files /tmp/ipDatabase.csv,/tmp/ipRegion.xlsx \   # 添加外部文件
    /path/to/examples.jar \
    hdfs://hadoop001:8020/imooc/input hdfs://hadoop001:8020/imooc/clean

    运行完之后查看结果
```

###### 性能优化
```
1. 存储格式选择

2. 压缩格式选择

3. 代码优化，批量存取数据，数据复用

4. 参数优化

    并行度, spark.sql.shuffle.partitions

    分区字段类型推测, spark.sql.soruces.partitionColumnTypeInference.enabled
```

###### 小结
```

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
