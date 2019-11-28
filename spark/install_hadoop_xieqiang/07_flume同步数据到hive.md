# 07 - flume同步数据到hive

```shell
1,上传flume安装包到/bigdata目录下并解压

2，编辑flue配置文件dir-hice.conf，（该配置文件用于同步某一目录下的json文件到hive的分区中）内容如下：

# Name the components on this agent
a1.sources = r1
a1.sinks = k1
a1.channels = c1

# Describe/configure the source
a1.sources.r1.type = spooldir
a1.sources.r1.spoolDir = /home/xieq/datas/
a1.sources.r1.fileHeader = true

# Describe the sink
a1.sinks.k1.type = hive
a1.sinks.k1.hive.metastore = thrift://192.168.56.81:9083
a1.sinks.k1.hive.database = dp
a1.sinks.k1.hive.table = ods_shixin_json
a1.sinks.k1.hive.partition = %Y-%m-%d
a1.sinks.k1.batchSize=1000
a1.sinks.k1.serializer = JSON
a1.sinks.k1.useLocalTimeStamp=true
a1.sinks.k1.callTimeout=10000000



# Use a channel which buffers events in memory
a1.channels.c1.type = memory
a1.channels.c1.capacity = 1500
a1.channels.c1.transactionCapacity = 1500

# Bind the source and sink to the channel
a1.sources.r1.channels = c1
a1.sinks.k1.channel = c1

3，启动flume agent ,命令如下

./flume-ng agent -c ../conf/ -f ../conf/dir-hive.conf -n a1 -Dflume.root.logger=INFO,console
~





./kafka-console-consumer.sh --bootstrap-server dp-hadoop3:9092,dp-hadoop4:9092,dp-hadoop5:9092 --topic topic-pochan --from-beginning
```

