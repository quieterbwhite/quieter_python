# 深入Kafka主题与消费者组

## 操作主题
```
创建主题

    ./kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic mytest2
    
打开生产者:

    ./kafka-console-producer.sh --broker-list localhost:9092 --topic mytest2
    
打开两个消费者：

    ./kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic mytest2 --from-beginning
    
都打开后，在生产者发送消息，然后两个消费者都能够接收到消息。

通过这个操作过程,我们能够看到多个Kafka Consumer可以消费同一个主题的同一条消息,
这显然就是之前课程中所介绍的广播概念,即多个客户端是可以获取到同一个主题的同一条消息并进行消费的。

--from-beginning参数的作用:

    如果消费者尚没有已建立的可用于消费的偏移量,那么就从Kafka Server日志中最早的消息开始消费,而非最新的消息开始消费。
```

## 消费者组
```
用如下命令打开两个消费者:

    ./kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic mytest2 --group mygroup
    
同一个消费者组，只会有一个消费者会收到消息。

不同的消费者组互不影响。
```
