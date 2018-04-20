# Kafka主题概念应用示例

## kafka 中还有哪些重要概念
```
如分区、副本、日志、保留策略、日志压缩、ISR(In-Sync Replica)集合、HW(High Watermark)、LEO(Log End Offset)等等,
这些概念可以认为是理解Kafka内核所应具备的前提。
```

## 启动服务
```
启动zookeeper

    ./zkServer.sh start-foreground
    或者
    sudo systemctl start zookeeper
    
启动kafka

    ./bin/kafka-server-start.sh config/server.properties 
```

## 操作主题
```
查看主题:

    ./kafka-topics.sh --list --zookeeper localhost:2181
    
    output:
        __consumer_offsets
        mytest
        
    __consumer_offsets是Kafka Server所创建的用于标识消费者偏移量的主题(Kafka中的消息都是顺序保存在磁盘上的,通过offset偏移量来标识消息的顺序),它由Kafka Server内部使用;
    mytest 是我们创建的主题

查看某个具体主题(如mytest)的详细信息:

    ./kafka-topics.sh --describe --topic mytest --zookeeper localhost:2181
    
    output:
        Topic:mytest	PartitionCount:1	ReplicationFactor:1	Configs:
        Topic: mytest	Partition: 0	Leader: 0	Replicas: 0	Isr: 0
	    
	第一行会显示出所有分区的一个总结信息。后续每一行则给出一个分区的信息。
	
	前情概要, mytest 的创建命令:
	
        ./bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic mytest
        可以清楚地看到,分区数设定为了1。
	
	第一行信息为:
        • 主题名:mytest
        • 分区数:1
        • 副本数:1
        
    第二行表示的信息为:
        • 主题名:mytest
        • 当前的分区:0
        • Leader Broker:0
        • 副本:0
        • Isr(In-Sync Replica):0
        
实际上,这些信息都是保存在ZooKeeper中的。Kafka是重度依赖于ZooKeeper的。
ZooKeeper保存了Kafka所需的元信息以及关于主题、消费者偏移量等诸多信息。
```
