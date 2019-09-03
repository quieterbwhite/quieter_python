# Spark-Streaming KafkaClient 异常解决

> https://www.jianshu.com/p/1db6a3096393
>
> https://blog.csdn.net/zhangshenghang/article/details/90264636
>
> https://kafka.apache.org/0110/documentation.html#security_sasl

在使用`Spark-Streaming`消费Kafka数据的时候，使用如下命令提交到`yarn`

```
Caused by: java.lang.IllegalArgumentException: Could not find a 'KafkaClient' entry in the JAAS configuration. System property 'java.security.auth.login.config' is not set
    at org.apache.kafka.common.security.JaasContext.defaultContext(JaasContext.java:131)
    at org.apache.kafka.common.security.JaasContext.load(JaasContext.java:96)
    at org.apache.kafka.common.security.JaasContext.load(JaasContext.java:78)
    at org.apache.kafka.common.network.ChannelBuilders.create(ChannelBuilders.java:104)
    at org.apache.kafka.common.network.ChannelBuilders.clientChannelBuilder(ChannelBuilders.java:61)
    at org.apache.kafka.clients.ClientUtils.createChannelBuilder(ClientUtils.java:86)
    at org.apache.kafka.clients.consumer.KafkaConsumer.<init>(KafkaConsumer.java:710)
    ... 17 more
```

如出现如上异常
配置代码如下

```
def main(args: Array[String]) {
    System.setProperty("java.security.krb5.conf", "/etc/krb5.conf")
    System.setProperty("java.security.auth.login.config", "/tmp/kafka_jaas.conf")
```

/tmp/kafka_jaas.conf

```
KafkaClient{
  com.sun.security.auth.module.Krb5LoginModule required
  doNotPrompt=true
  useTicketCache=true
  principal="admin/admin@DEMO.com"
  useKeyTab=true
  serviceName="kafka"
  keyTab="/etc/security/keytabs/admin.keytab"
  client=true;
};
```

提交命令

```
spark-submit --master yarn \
    --conf spark.yarn.tokens.hbase.enabled=true \
    --deploy-mode client \
    --class com.starsriver.platform.kafka.SparkStreamingKafka \
    --executor-memory 1G \
    --num-executors 3 \
    --executor-cores 2 \
    --keytab /etc/security/keytabs/admin.keytab \
    --principal admin/admin@dounine.com \
    target/demo-1.0.0-SNAPSHOT-jar-with-dependencies.jar > out.log
```

## 问题解决

只需要在提交的时候再添加一项配置即可

```
--conf "spark.executor.extraJavaOptions=-Djava.security.auth.login.config=/tmp/kafka_jaas.conf"  \
```

最终正确提交命令如下

```
spark-submit --master yarn \
    --conf spark.yarn.tokens.hbase.enabled=true \
    --deploy-mode client \
    --class com.starsriver.platform.kafka.SparkStreamingKafka \
    --conf "spark.executor.extraJavaOptions=-Djava.security.auth.login.config=/tmp/kafka_jaas.conf"  \
    --executor-memory 1G \
    --num-executors 3 \
    --executor-cores 2 \
    --keytab /etc/security/keytabs/admin.keytab \
    --principal admin/admin@dounine.com \
    target/demo-1.0.0-SNAPSHOT-jar-with-dependencies.jar > out.log
```

## 描述

经过测试以下配置缺一不可

```
System.setProperty("java.security.auth.login.config", "/tmp/kafka_jaas.conf")
--conf "spark.executor.extraJavaOptions=-Djava.security.auth.login.config=/tmp/kafka_jaas.conf"
```

如果大家也遇到上面问题的异常两句都添加上即可