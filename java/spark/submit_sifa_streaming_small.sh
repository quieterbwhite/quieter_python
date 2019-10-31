#!/usr/bin/env bash

DEPEND_JARS=hdfs:///user/oozie/phoenix/phoenix-4.14.1-HBase-1.2-client.jar,hdfs:///user/oozie/phoenix/phoenix-spark-4.14.1-HBase-1.2.jar
PROJECT_JAR=hdfs:///user/oozie/qxbfull/data-analysis-1.14.1-1.2.jar

nohup spark2-submit --class com.ufm.dp.streaming.SiFaStreaming \
--master yarn \
--deploy-mode client \
--driver-memory 4g \
--executor-memory 4g \
--conf spark.executor.extraJavaOptions=-Djava.security.auth.login.config=/etc/kafka/conf/kafka_client_jaas.config \
--driver-class-path $DEPEND_JARS \
--jars $DEPEND_JARS,$PROJECT_JAR \
--executor-cores 3 \
--num-executors 2 \
/home/libo/jar/sifa-jishi-streaming.jar 1>streaming_sifa_jishi_success.log 2>streaming_sifa_jishi_error.log &
