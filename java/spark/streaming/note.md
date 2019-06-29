#### Imooc Spark Streaming 实战笔记

[第二章_初识实时流处理](#第二章_初识实时流处理)  
[第三章_分布式日志收集框架Flume](#第三章_分布式日志收集框架Flume)  
[第四章_分布式消息队列kafka](#第四章_分布式消息队列kafka)  
[第五章_实战环境搭建](#第五章_实战环境搭建)  
[第六章_SparkStreaming入门](#第6章_SparkStreaming入门)  
[第七章_SparkStreaming核心](#第七章_SparkStreaming核心)  
[第八章_SparkSreaming进阶](#第八章_SparkSreaming进阶)  
[第九章_SparkStream整合Flume实战](#第九章_SparkStream整合Flume实战)

##### 第二章_初识实时流处理
```
业务现状分析

    需求: 统计主站每个课程访问的客户端，地域信息分布
        地域: ip转换
        客户端: useragent获取
        => 离线处理
    实现步骤: 
        spark 进行统计分析

    项目架构:
        日志收集: Flume
        离线分析: spark
        统计结果图形化展示

    问题:
        小时级别
        10min
        5min
        1min
        秒级别

    如何解决: 实时流处理

实时流处理产生背景

    时效性高

    数据量大

实时流处理概述

    实时计算

    流式计算

    实时流式计算

离线计算与实时计算对比

    数据来源
        离线: HDFS 历史数据　数据量大
        实时: kafka, 实时新增/修改记录过来的一笔数据

    处理过程
        离线: MapReduce
        实时: Spark(DStream/SS)

    处理速度
        离线: 慢
        实时: 快

    进程
        离线: 启动+销毁
        实时: 7x24

实时流处理框架对比

    Apache Storm

    Apache Spark Stream

实时流处理架构与技术选型

    app -> WebServer -> Flume -> Kafka -> Spark/storm -> DB -> 可视化展示

实时流处理在企业中的应用

    电信行业
```

##### 第三章_分布式日志收集框架Flume
```
业务现状分析

    WebServer/ApplicationServer分散在各个机器上
    想大数据平台Hadoop进行统计分析
    日志如何收集到Hadoop平台上
    解决方案及存在的问题

Flume概述

    收集，聚合，移动大量日志数据

Flume架构及核心组件

    WebServer
    
    Source 
    
    Channel
    
    Sink
    
    HDFS

Flume环境部署

    前置条件
        JDK
        Memory
        Disk Space
        Directory Permission

    解压
    配置环境变量
    修改配置文件
        cp flume-env.sh.template flume-env.sh
        增加: export java_home的值

    检查安装时候成功
        flume-ng version

Flume实战

需求1 从指定网络端口采集数据输出到控制台: 
使用Flume的关键就是写配置文件
    1. 配置Source
    2. 配置Channel
    3. 配置Sink
    4. 把以上3个组件串起来

配置example.conf, 放到conf目录下
    # Name the components on this agent
    a1.sources = r1
    a1.sinks = k1
    a1.channels = c1
    注释:
        a1: agent名称
        r1: 数据源名称
        k1: sink的名称
        c1: channel的名称

    # Describe/configure the source
    a1.sources.r1.type = netcat
    a1.sources.r1.bind = localhost
    a1.sources.r1.port = 44444
    注释:

    # Describe the sink
    a1.sinks.k1.type = logger

    # Use a channel which buffers events in memory
    a1.channels.c1.type = memory
    a1.channels.c1.capacity = 1000
    a1.channels.c1.transactionCapacity = 100

    # Bind the source and sink to the channel
    a1.sources.r1.channels = c1
    a1.sinks.k1.channel = c1

启动:
    flume-ng agent \
    --name a1 \
    --conf $Flume_HOME/conf \
    --conf-file $FLUME_HOME/conf/example.conf \
    -Dflume.root.logger=INFO,console

测试:
    telnet hadoop000 44444

    Event是Flume数据传输的基本单元
    Event = 可选的Header+body

需求二 监控一个文件实时采集新增的数据输出到控制台:

需求三 将A服务器上的日志实时采集到B服务器上(重要)

技术选型
    exec source + memory channel + avro sink
    avro source + memory channel + logger sink
```

##### 第四章_分布式消息队列kafka
```
kafka概述

kafka架构及核心概念

    producer
    consumer
    broker
    topic

kafka部署及使用

kafka容错性测试

kafka api 编程

kafka 实战
```

##### 第五章_实战环境搭建
```
安装hbase
    下载解压

    修改hbase-env.sh
        export $JAVA_HOME=xxx
        export HBASE_MANAGES_ZK=false

    修改hbase-site.xml
        <property>
            <name>hbase.rootdir</name>
            <value>hdfs://hadoop000:8020/hbase</value>
        </property>

        <property>
            <name>hbase.cluster.distributed</name>
            <value>true</value>
        </property>

        <property>
            <name>hbase.zookeeper.quorum</name>
            <value>hadoop000:2181</value>
        </property>

    修改 regionservers
        hadoop000

    启动
        ./start_hbase.sh

    jps
        HMaster
        HRegionServer

    web验证
        http://hadoop000:60010

    命令行访问
        ./hbase shell
        > version
        > status
        # 创建表
        > create 'member', 'info', 'address'
        # 查看所有表
        > list
        # 查看表详情
        > describe 'member'

        此时，web界面已经能看到新创建的表

开发环境搭建

    实际上就是添加各种依赖到 pom.xml
    参考项目: sparktrain
```

##### 第6章_SparkStreaming入门
```
概述
    将不同数据源的数据经过Spark Streaming处理之后，将结果输出到外部系统
    低延时
    能从错误中高效的恢复
    能够运行在大量节点上
    能够将批处理，机器学习，图计算，等子框架和Spark Streaming综合起来使用

    不需要独立安装 one stack to rule them all

应用场景
    交易中实时金融欺诈检测
    传感器状态数据实时检测

集成Spark生态系统的使用
    Join 静态数据, 批处理和流处理的综合使用
    机器学习模型的训练　val model = Kmeans.train(dataset, ...)
    Combine SQL with streaming processing, Interactively query streaming data with SQL

发展史
    2011 -> 

词频统计功能入门

    spark streaming 和 spark core的编程模式是一样的。从一个word count的例子就可以看出来

    spark-submit 执行(生产)

        ./spark-submit --master --local[2] \
        --class org.apache.spark.examples.streaming.NetworkWordCount \
        --name NetworkWordCount \
        /home/bwhite/sortware/spark/examples/jars/spark-example_2.11-2.2.0.jar hadoop000 9999

        nc -lk 9999 通过这个命令往该端口发送数据用来测试

    spark-shell 执行(测试)

        ./spark-shell --master --local[2]  启动shell

        然后在shell里面写代码来执行就可以了

工作原理

    粗粒度

        1. 接收实时数据流

        2. spark streaming 按设置的秒数分割数据块

        3. spark 处理数据块

        4. 输出数据

    细粒度

        1. pass
```

##### 第七章_SparkStreaming核心
```scala
核心概念

    Streaming Context http://spark.apache.org/docs/latest/streaming-programming-guide.html

    Discretized Streams (DStreams)
        一个Dstream由多个RDD构成，底层就是处理一个个RDD

    Input Dstreams and Receivers
        上面两者是一一对应的，用于从源头接收数据并保存在spark的内存里面,供后续处理
        

    Transformations

    Output Operations

实战案例

    Spark Streaming 处理 socket 数据 - 参考 NetworkWordCount.scala

    Spark Streaming 处理 HDFS 文件数据 - 参考  FileWordCount.scala
```

##### 第八章_SparkSreaming进阶
```
带状态的算子: UpdateStateByKey
    spark streaming 默认处理每批次的数据
    如果需要计算从古至今的的数据
    那么就需要状态的累加
    所有就需要带状态的算子

    参考: StatefulWordCount.scala

实战: 计算到目前为止累积出现的单词个数写入到Mysql中

    使用 Spark Streaming进行统计分析
    Spark Streaming统计结果写入到MySQL

    参考: ForeachRDDApp.scala

基于window的统计
    定时进行一个时间段内的数据处理

    window length: 窗口的长度
    sliding interval: 窗口的间隔

    这两个参数和我们的batch size有关系: 倍数

    每隔多久计算某个范围内的数据: 每隔十秒计算前10分钟的wc
    每隔sliding interval统计前window length的值

实战: 黑名单过滤

    参考: TransformApp.scala

    访问日志        ==> DStream
    20180808,zs
    20180808,ls
    20180808,ww
      ==> (zs:20180808,zs)(ls:20180808,ls)(ww:20180808,ww)

    黑名单列表  ==> RDD
    zs
    ls
      ==> (zs:true)(ls:true)

    leftjoin
    (zs: [<20180808,zs>, <true>])  x
    (ls: [<20180808,ls>, <true>])  x
    (ww: [<20180808,ww>, <false>]) => tuple 1

    => 20180808,ww 只应该输出这个不在黑名单的记录

实战: Spark Streaming整合Spark SQL实战 完成 word count

    参考 SqlNetworkWordCount.scala
```

##### 第九章_SparkStream整合Flume实战
```
实战一： Flume-style Push-based Approach

实战二: Pull-based Approach using a Custom Sink
```