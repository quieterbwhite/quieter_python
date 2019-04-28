# Kafka
> http://kafka.apache.org/  

## 安装
```
http://kafka.apache.org/downloads

下载并解压
```

## 运行
```
kafka 严重依赖 zookeeper。所以，运行kafka之前，先安装并运行zookeeper。

进入解压后的目录，执行如下命令:

bin/kafka-server.start.sh config/server.properties

$ nohup kafka-server-start.sh /home/espai/kafka/config/server.properties 1>/dev/null 2>&1 &
```

## 测试
```
通过kafka的脚本，通过一个生产者向kafka发送消息，接下来通过一个消费者来接收该消息

创建一个名字为 mytest 的主题:

    bwhite@os:~/software/kafka_2.11-1.0.0$ bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic mytest
    Created topic "mytest".
    bwhite@os:~/software/kafka_2.11-1.0.0$ 

启动生产者:

    bwhite@os:~/software/kafka_2.11-1.0.0$ bin/kafka-console-producer.sh --broker-list localhost:9092 --topic mytest
    >

启动消费者:

    bwhite@os:~/software/kafka_2.11-1.0.0$ bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic mytest --from-beginning

接下来在生产者shell中输入内容，消费者这边就能接收到

```






