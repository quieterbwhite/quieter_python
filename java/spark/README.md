# Spark数据分析及调度

安装教程  
Azkaban任务调度基础  
Azkaban任务调度实战  
Azkaban任务调度进阶  
项目实战  

#### 安装教程
1. 安装 JDK1.8
2. 安装 Scala-2.11.8
3. 安装 Hadoop-2.6.0-cdh5.7.0
   1. 修改hadoop-env.sh -> 配置 JAVA_HOME
   2. 修改core-site.xml 见下表
   3. 修改hdfs-site.xml 见下表
   4. 配置mapred-site.xml Yarn相关，见下表
   5. 配置yarn-site.xml Yarn相关，见下表
   6. 格式化 $ hadoop namenode -format，格式化成功，临时目录下会新增内容
   7. 启动hdfs，$ start-dfs.sh
   8. jps 检查服务是否启动成功 -> NameNode,DataNode,SecondaryNameNode
   9. hadoop fs -ls / ，检查文件系统
   10. hadoop fs -mkdir /test，创建文件夹
   11. hadoop fs -put somefile.txt /test/
   12. hadoop fs -text /test/somefile.txt
   13. http://127.0.0.1:50070，浏览文件系统
   14. 启动yarn，start-yarn.sh
   15. jps -> ResourceManager，NodeManager
   16. http://127.0.0.1:8088
4. 安装Maven
5. 安装Python3
   1. $ cd Python3.6.5
   2. $ sudo yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel
   3. $ ./configure --prefix=/home/hadoop/app/python3 --enable-optimizations
   4. $ makd && make install
   5. 配置环境变量
6. 安装Spark
   1. 下载源码 spark.apache.org
   2. 解压，编译 http://spark.apache.org/docs/latest/building-spark.html
   3. Building a Runnable Distribution 参考文档里面这部分
   4. $ ./dev/make-distribution.sh --name 2.6.0-cdh5.7.0 --tgz -Pyarn -Phadoop-2.6 -Phive -Phive-thriftserver -Dhadoop.version=2.6.0-cdh5.7.0，这个命令会生成一个spark包
   5. 解压，安装
   6. $ pyspark-shell
   7. http://127.0.0.1:4040

环境变量  more .bash_profile

```shell
export JAVA_HOME=/home/hadoop/app/jdk1.8.0_91
export PATH=$JAVA_HOME/bin:$PATH

export SCALA_HOME=/home/hadoop/app/scala-2.11.8
export PATH=$SCALA_HOME/bin:$PATH


export HADOOP_HOME=/home/hadoop/app/hadoop-2.6.0-cdh5.7.0
export PATH=$HADOOP_HOME/bin:$PATH

export MAVEN_HOME=/home/hadoop/app/apache-maven-3.3.9
export PATH=$MAVEN_HOME/bin:$PATH

export PATH=/home/hadoop/app/python3/bin:/usr/bin/python:$PATH

export PYSPARK_PYTHON=python

export SPARK_HOME=/home/hadoop/app/spark-2.3.0-bin-2.6.0-cdh5.7.0
export PATH=$SPARK_HOME/bin:$PATH
```

core-site.xml

```xml
<configuration>
  <property>
    <name>fs.default.name</name>
    <value>hdfs://hadoop000:8020</value>
  </property>
</configuration>
```

hdfs-site.xml

```xml
<configuration>
  <property>
    <name>dfs.namenode.name.dir</name>
    <value>/home/hadoop/app/tmp/dfs/name</value>
  </property>

  <property>
    <name>dfs.datanode.data.dir</name>
    <value>/home/hadoop/app/tmp/dfs/data</value>
  </property>

  <property>
    <name>dfs.replication</name>
    <value>1</value>
  </property>
</configuration>
```

mapred-site.xml

```xml
<configuration>
  <property>
    <name>mapreduce.framework.name</name>
    <value>yarn</value>
  </property>
</configuration>
```

yarn-site.xml

```xml
<configuration>
  <property>
    <name>yarn.nodemanager.aux-services</name>
    <value>mapreduce_shuffle</value>
  </property>
</configuration>
```

#### Azkaban任务调度基础
```
https://azkaban.github.io/
https://www.xn--7qv19ae78e.cn/2017/09/09/2017-09-09-azkaban-execute-jobs/

工作流概述

ETL
  1. 数据抽取
    Sqoop把RDBMS中的数据抽取到Hadoop
    Flume进行日志，文书数据的采集，采集到Hadoop
  2. 数据处理
    Hive/MapReduce/Spark/...
  3. 统计结果入库
    数据就存放在HDFS(Hive/Spark SQL文件)
      启动一个Server: HiveServer2 / ThriftServer
      jdbc方式去访问统计结果
    使用Sqoop把结果导出到RDBMS

调度在大数据处理中的重要性

  定时调度

  依赖调度

常见的调度框架

  Azkaban 

  Oozie

  宙斯(alibaba)

Azkaban 概述

  批处理工作流， 用于跑hadoop的job
  易于使用的web界面

Azkaban 架构

  Web Server
  
  Executor Server
  
  MySQL

Azkaban 运行模式

  solo server mode

  two server mode

  distributed multiple-executor mode

Azkaban 源码编译

  https://azkaban.readthedocs.io/en/latest/getStarted.html#building-from-source

Azkaban 单机部署及快速入门

  安装 gradle, maven
  
  下载，解压，编译成安装包

  JCE报错:
    https://yq.aliyun.com/articles/648399

    解决方法：
    下载JCE
    https://www.oracle.com/technetwork/cn/java/javase/downloads/jce8-download-2133166-zhs.html
    我这边使用的JDK8，包含了JCE所需要的jre8
    解压搜下载好的文件，放置到以下目录：
    放置到jdk所在目录下的：
    cp UnlimitedJCEPolicyJDK8/* /usr/local/jdk1.8.0_74/jre/lib/security
    对原有的文件进行覆盖
    然后在进行重新编译

  【npm ERR】cb() never called!解决方案
    https://blog.csdn.net/TalonZhang/article/details/88538361
    解决方案：
    安装node, 再执行下面的命令:
    清理 npm缓存就可以了
    sudo npm cache clean --force
    
  编译成功
  
  去对应了模式的目录下找到安装包即可:
  $ cd /home/bwhite/software/azkaban-master/azkaban-solo-server/build/distributions
  
  $ tar xzvf azkaban-solo-server-0.1.0-SNAPSHOT.tar.gz -C /home/bwhite/software/

  $ cd /home/bwhite/software/azkaban-solo-server-0.1.0-SNAPSHOT
  
  # 奇葩啊，一定要在bin目录下执行才能正常启动，这些开源的东西真是要命
  $ ./bin/start-solo.sh
  	
  jps查看有 AzkabanSingleServer 进程
  
  访问页面: http://localhost:8081
  默认用户名密码: azkaban:azkaban
  
  修改配置文件:
  /conf/azkaban-user.xml 修改用户信息
  
  <azkaban-users>
    <user groups="azkaban" password="" roles="admin" username="root"/>
    <!--<user password="metrics" roles="metrics" username="metrics"/>-->

    <role name="admin" permissions="ADMIN"/>
    <role name="metrics" permissions="METRICS"/>
  </azkaban-users>
 
  jps 查看启动的进程
  
  修改时区:
  	default.timezone.id=Asia/Shanghai

  用户名&密码: $ ./azkaban-solo-server/conf/

  创建Job
  
  打包zip
  	zip -r foo.zip *
  
  上传
  
  执行
```

#### Azkaban任务调度实战
```
Dependency作业

  # foo.job
  type=command
  command=echo foo

  # bar.job
  type=command
  dependencies=foo
  command=echo bar

  zip -r dependencies.zip foo.job bar.job

  azkaban web UI:
  1. 创建项目
  2. 上传dependencies.zip
  3. 点击执行按钮

HDFS作业

  简单的hadoop命令
  hadoop fs -l /list

MapReduce作业

  测试命令

    hadoop jar hadoop-mapreduce-examples-2.6.0-cdh5.7.0.jar pi 2 3

  mapreduce.job

    type=command
    command=/path/to/hadoop jar /path/to/hadoop-mapreduce-examples-2.6.0-cdh5.7.0.jar pi 2 3

    command=/path/to/hadoop jar /path/to/hadoop-mapreduce-examples-2.6.0-cdh5.7.0.jar wordcount /text.txt /az/wc

Hive作业

  # 创建表
  create table emp(
    empno int, ename string, job string,
    mgr int, hiredate string, sal double,
    comm double, deptno int
  )row format delimited fields terminated by '\t'

  # 导入数据
  load data local inpath '/home/hadoop/data/emp.txt' overwrite into table emp;

  # 测试需要用到的语句时候工作正常
  select deptno, count(1) from emp group by deptno;

  hive.job
    type=command
    command=/path/to/hive -f 'test.sql'

  test.sql
    select deptno, count(1) from emp group by deptno;

  打包上传执行

Spark作业

  https://blog.csdn.net/lsshlsw/article/details/50831239
  https://www.jianshu.com/p/f2310a5c38c6

  spark.job
    type=command
    command=/usr/install/spark/bin/spark-submit --class com.test.AzkabanTest test-1.0-SNAPSHOT.jar

    type=command
    command=${spark.home}/bin/spark-submit --master yarn-cluster --class com.dataeye.template.spark.WordCount lib/spark-template-1.0-SNAPSHOT.jar   hdfs://de-hdfs/data/yann/info.txt   paramtest

定时作业

  确定任务没有问题，在web页面上配置就可以了

邮件告警

  也是在web页面配置就可以了
```

#### Azkaban任务调度进阶
```
我自己搭建单机的就可以了。

Two Server 模式 WebServer 部署

  官网文档有详细描述: 
  https://azkaban.readthedocs.io/en/latest/getStarted.html#getting-started-with-the-multi-executor-server

Two Server 模式 ExecServer 部署

Two Server 模式案例

Ajax API 和 Plugin 的使用

短信告警的改造思路

调度框架的改造思路
```

#### 项目实战
```
企业级大数据开发流程

  1. 调研
  2. 需求分析
  3. 方案设计
  4. 功能开发
  5. 测试
  6. 部署上线
  7. 运维
  8. 后期迭代开发

企业级大数据分析平台

企业级大数据应用

数据量预估及集群规划

项目需求

功能实现

通过Azkaban进行调度

项目总结及后续课程展望
```

#### 使用说明

##### Python3实战Spark大数据分析及调度


大家好，欢迎大家来到我在[慕课网](https://imooc.com)上的实战课程[《Python3实战Spark大数据分析及调度》](https://coding.imooc.com/class/chapter/249.html)的官方代码仓。在本仓库中将提供课程学习过程中的代码以及笔记，如有错误信息，也欢迎大家以pull request的方式更新上来。

***

## 代码说明

* code：该课程的所有代码
* note：该课程的所有笔记
* OOTB环境：请关注课程页面`下载`的`大型资料下载`

***
## 课程说明
本门课程将按照如下模块进行讲解

* 实战环境搭建
* Spark Core核心RDD：RDD是什么、RDD五大特性、RDD特性在源码中的体现、图解RDD、SparkContext&SparkConf详解、RDD的2种创建方式、使用IDE开发pyspark应用程序、提交pyspark作业到服务器上运行
* Spark Core RDD编程：map & filter & flatMap & groupByKey & reduceByKey & sortByKey & union & distinct & join & action算子详解、词频统计 & TopN & 平均数统计案例编程实现
* Spark运行模式：local、standalone、yarn模式详解
* Spark Core进阶：Spark中的核心术语、运行架构、并对比Spark和MapReduce的概念区分、存储策略及选择方式、宽窄依赖及Shuffle
* Spark Core调优：从Spark作业性能指标、序列化、内存管理、广播变量及数据本地化这几个方面来介绍Spark作业的调优
* Spark SQL：Spark SQL的架构、DataFrame&Dataset、以及如何使用Python API来对DataFrame进行编程
* Spark Streaming：Spark Streaming的核心概念、执行原理、以及如何Python API来对Spark Streaming进行编程
* Azkaban基础篇：Azkaban的特性、架构、运行模式、源码编译及部署、快速入门
* Azkaban实战篇：使用Azkaban来完成HDFS、MapReduce、Hive作业的调度、定时作业调度以及邮件告警
* Azkaban进阶篇：Azkaban在生产上的部署、权限管理、Ajax API、Plugin、以及短信和调度框架的二次开发
* 项目实战：构建大数据平台的技术选型、集群升级资源评估，并使用Spark对气象数据进行分析，讲分析结果写入ES，并通过Kibana进行统计结果的可视化展示

***

## 思考题
Q1: 假设一个日志文件如下所示，字段之间分隔符是`,`

```
1,zhangsan,30
2,lisi,32
3,wangwu,abc
```

第一列id(int)，第二列name(name)，第三列age(int)，但是第三行的第三列值为abc，这是一条不符合要求的数据。

请使用Spark解析日志，使用计数器完成该日志的总行数以及符合条件的记录数统计。

***
欢迎关注个人公众号，不定期会推送一些大数据相关的文章
<br>
![个人公众号](https://git.imooc.com/Project/coding-249/raw/master/qrcode.jpg)
