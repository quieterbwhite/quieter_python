### kafka环境搭建和使用(python API)](https://www.cnblogs.com/iforever/p/9130983.html)

## 引言

上一篇文章了解了kafka的重要组件zookeeper，用来保存broker、consumer等相关信息，做到平滑扩展。这篇文章就实际操作部署下kafka，用几个简单的例子加深对kafka的理解，学会基本使用kafka。

## 环境搭建

我将会在本地部署一个三台机器的zookeeper集群，和一个2台机器的kafka集群。

### zookeeper集群

zookeeper的搭建可以看我的上一篇文章[分布式系统中zookeeper实现配置管理+集群管理](https://www.cnblogs.com/iforever/p/9095095.html)，按照步骤，一步步可以很容易的搭建3太服务器的zookeeper集群。跟之前一样，我还是在本地的3个端口搭建了3台服务器，地址如下所示：

```
192.168.0.105:2181
192.168.0.105:2182
192.168.0.105:2183
```

这三台服务器一会儿会在kafka配置中用到。

### kafka集群

*第一步. 下载kafka*

到kafka官网下载[apache kafka](http://mirrors.tuna.tsinghua.edu.cn/apache/kafka/1.1.0/kafka_2.12-1.1.0.tgz)，解压到`/path/to/kafka`目录。

*第二步. 修改配置文件*
复制`/path/to/kafka/config/server.properties`，到`/path/to/kafka/config/server-1.properties`和`/path/to/kafka/config/server-2.properties`

配置文件中修改的差异内容如下所示：
`server-1.properties`：

```
broker.id=1
listeners=PLAINTEXT://:9093
log.dirs=/tmp/kafka-logs-1
zookeeper.connect=192.168.0.105:2181,192.168.0.105:2182,192.168.0.105:2183
```

`server-2.properties`：

```
broker.id=2
listeners=PLAINTEXT://:9094
log.dirs=/tmp/kafka-logs-2
zookeeper.connect=192.168.0.105:2181,192.168.0.105:2182,192.168.0.105:2183
```

其中`broker.id`是broker的唯一标示，集群中的broker标识必须唯一。
`listeners`是broker监听的地址和端口，`advertised.listeners`用于和producer、consumer交互，后者未配置会默认使用前者，listeners的完整格式是`listeners = listener_name://host_name:port`，其中`PLAINTEXT`是协议，还有一种是`SSL`，具体还没太搞明白（TODO）。
`log.dirs`是日志数据的存放目录，也就是producer产生的数据存放的目录。
`zookeeper.connect`配置是zookeeper的集群，broker启动之后将信息注册到zookeeper集群中。

*第三步. 启动服务器*

```
cd /path/to/kafka
bin/kafka-server-start.sh -daemon config/server-1.properties
bin/kafka-server-start.sh -daemon config/server-2.properties
```

使用`jps`命令可以看见2个kafka进程，证明启动成功了。

*第四步. 创建topic*
创建topic一般使用kafka自带的脚本创建:

```
bin/kafka-topics.sh --create --zookeeper 192.168.0.105:2181,192.168.0.105:2182,192.168.0.105:2183 --replication-factor 2 --partitions 10 --topic user-event
```

其中`--zookeeper`就是后面就是我们上面配置的zookeeper集群，`--replication-factor`代表每个分区在集群中复制的份数，后面的值要小于kafka集群中服务器数量，`--partitions`表示创建主题的分区数量，一般分区越大，性能越好，`--topic`后边儿就是创建主题的名字，运行成功之后会看到`Created topic "user-event".`字样，表示创建成功，会在kafka配置的日志目录下创建主题信息，比如下面的：
`ll /tmp/kafka-logs-1`

```
drwxr-xr-x  7 ritoyan  wheel  224  6  3 21:21 clock-tick-0
drwxr-xr-x  7 ritoyan  wheel  224  6  3 21:21 clock-tick-2
drwxr-xr-x  6 ritoyan  wheel  192  6  3 21:26 user-event-0
drwxr-xr-x  6 ritoyan  wheel  192  6  3 21:26 user-event-1
drwxr-xr-x  6 ritoyan  wheel  192  6  3 21:26 user-event-2
drwxr-xr-x  6 ritoyan  wheel  192  6  3 21:26 user-event-3
drwxr-xr-x  6 ritoyan  wheel  192  6  3 21:26 user-event-4
drwxr-xr-x  6 ritoyan  wheel  192  6  3 21:26 user-event-5
drwxr-xr-x  6 ritoyan  wheel  192  6  3 21:26 user-event-6
drwxr-xr-x  6 ritoyan  wheel  192  6  3 21:26 user-event-7
drwxr-xr-x  6 ritoyan  wheel  192  6  3 21:26 user-event-8
drwxr-xr-x  6 ritoyan  wheel  192  6  3 21:26 user-event-9
```

`ll /tmp/kafka-logs-2`

```
drwxr-xr-x  7 ritoyan  wheel  224  6  3 21:21 clock-tick-1
drwxr-xr-x  6 ritoyan  wheel  192  6  3 21:26 user-event-0
drwxr-xr-x  6 ritoyan  wheel  192  6  3 21:26 user-event-1
drwxr-xr-x  6 ritoyan  wheel  192  6  3 21:26 user-event-2
drwxr-xr-x  6 ritoyan  wheel  192  6  3 21:26 user-event-3
drwxr-xr-x  6 ritoyan  wheel  192  6  3 21:26 user-event-4
drwxr-xr-x  6 ritoyan  wheel  192  6  3 21:26 user-event-5
drwxr-xr-x  6 ritoyan  wheel  192  6  3 21:26 user-event-6
drwxr-xr-x  6 ritoyan  wheel  192  6  3 21:26 user-event-7
drwxr-xr-x  6 ritoyan  wheel  192  6  3 21:26 user-event-8
drwxr-xr-x  6 ritoyan  wheel  192  6  3 21:26 user-event-9
```

可以看到两个broker中都创建了主题`user-event`的10个分区。可能也有人要问了，`clock-tick`这个主题怎么在broker1中有2个分区，broker2中有1个分区，这个是我之前创建的一个分区，用了下面的命令`bin/kafka-topics.sh --create --zookeeper 192.168.0.105:2181,192.168.0.105:2182,192.168.0.105:2183 --replication-factor 1 --partitions 3 --topic clock-tick`，只有一份日志记录，3个分区，分区会均匀的分布在所有broker上。

至此kafka环境配置好了，西面我们看看如何使用。

## 基本使用

安装`kafka-python`，用来操作kafka，`pip3 install kafka-python`，这里是他的文档，文档写的不错，简洁易懂[kafka-python](http://kafka-python.readthedocs.io/en/master/index.html)

### producer 向broker发送消息

`bootstrap_servers`是kafka集群地址信息，下面事项主题`user-event`发送一条消息，`send`发送消息是异步的，会马上返回，因此我们要通过阻塞的方式等待消息发送成功(或者`flush()`也可以，flush会阻塞知道所有log都发送成功)，否则消息可能会发送失败，但也不会有提示，关于上面这个可以通过删除send之后的语句试试，会发现broker不会收到消息，然后在send后加上`time.sleep(10)`之后，会看到broker收到消息。

```
from kafka import KafkaProducer
from kafka.errors import KafkaError

producer = KafkaProducer(
    bootstrap_servers=[
        "localhost:9093",
  "localhost:9094"
  ]
)

future = producer.send("user-event", b'I am rito yan')
try:
    record_metadata = future.get(timeout=10)
    print_r(record_metadata)
except KafkaError as e:
    print(e)
```

阻塞等待发送成功之后，会看到返回插入记录的信息：
`RecordMetadata(topic='user-event', partition=7, topic_partition=TopicPartition(topic='user-event', partition=7), offset=1, timestamp=1528034253757, checksum=None, serialized_key_size=-1, serialized_value_size=13)`，里面包括了插入log的主题、分区等信息。

### 格式化发送的信息

创建producer的时候可以通过`value_serializer`指定格式化函数，比如我们数据是个dict，可以指定格式化函数，将dict转化为byte：

```
import json

producer = KafkaProducer(
    bootstrap_servers=[
        "localhost:9093",
        "localhost:9094"
    ],
    value_serializer=lambda m: json.dumps(m).encode('ascii')
)

future = producer.send("user-event", {
    "name": "燕睿涛",
    "age": 26,
    "friends": [
        "ritoyan",
        "luluyrt"
    ]
})
```

这样就可以将格式化之后的信息发送给broker，不用每次发送的时候都自己格式化，真是不要太好用。

### consumer 消费数据

创建一个consumer，其中`group_id`是分组，broker中的每一个数据只能被consumer组中的一个consumer消费。

```
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    "user-event",
    group_id = "user-event-test",
    bootstrap_servers = [
        "localhost:9093",
        "localhost:9094"
    ]
)
for message in consumer:
    print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))
```

启动之后，进程会一直阻塞在哪里，等broker中有消息的时候就会去消费，启动多个进程，只要保证group_id一致，就可以保证消息只被组内的一个consumer消费，上面的程序会输出：

```
user-event:8:2: key=None value=b'{"name": "\\u71d5\\u777f\\u6d9b", "age": 26, "friends": ["ritoyan", "luluyrt"]}'
```

同样，进入的时候有`value_serializer`，出来的时候对应的也有`value_deserializer`，消费者可以配置`value_deserializer`来格式化内容，跟producer对应起来

```
consumer = KafkaConsumer(
    "user-event",
  group_id = "user-event-test",
  bootstrap_servers = [
        "localhost:9093",
  "localhost:9094"
  ],
  value_deserializer=lambda m: json.loads(m.decode('ascii'))
)
```

输出内容`user-event:8:3: key=None value={'name': '燕睿涛', 'age': 26, 'friends': ['ritoyan', 'luluyrt']}`

## kafka其他命令

### 查看分组

我们的consumer可能有很多分组，可以通过西面的命令查看分组信息：

```
cd /path/to/kafka
bin/kafka-consumer-groups.sh --bootstrap-server localhost:9093,localhost:9094 --list
```

可以看到我使用中的分组有4个，分别如下所示

```
clock-tick-test3
user-event-test
clock-tick-test2
clock-tick-test
```

### 查看特定分组信息

可以通过`bin/kafka-consumer-groups.sh --bootstrap-server 127.0.0.1:9093 --group user-event-test --describe`，查看分组`user-event-test`的信息，可以看到西面的信息，包含消费的主题、分区信息，以及consumer在分区中的offset和分区的总offset。（为了格式化显示，删了部分列的部分字母）

```
TOPIC       PARTITION   CURRENT-OFFSET  LOG-END-OFFSET  LAG CONSUMER-ID HOST    CLIENT-ID
user-event  3   0   0   0   kafka-python-154b2 /127.0.0.1   kafka-python
user-event  0   0   0   0   kafka-python-154b2 /127.0.0.1   kafka-python
user-event  1   1   1   0   kafka-python-154b2 /127.0.0.1   kafka-python
user-event  2   1   1   0   kafka-python-154b2 /127.0.0.1   kafka-python
user-event  4   0   0   0   kafka-python-154b2 /127.0.0.1   kafka-python
user-event  9   1   1   0   kafka-python-78517 /127.0.0.1   kafka-python
user-event  8   4   4   0   kafka-python-78517 /127.0.0.1   kafka-python
user-event  7   2   2   0   kafka-python-78517 /127.0.0.1   kafka-python
user-event  6   1   1   0   kafka-python-78517 /127.0.0.1   kafka-python
user-event  5   0   0   0   kafka-python-78517 /127.0.0.1   kafka-python
```

## 结语

至此，kafka的基本使用算是掌握了，以后要是有机会在项目中实践就好了，在实际工程中的各种问题可以更加深刻的理解其中的原理。