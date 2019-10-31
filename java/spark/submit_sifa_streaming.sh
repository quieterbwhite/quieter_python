#!/usr/bin/env bash

DEPEND_JARS=hdfs:///user/oozie/phoenix/phoenix-4.14.1-HBase-1.2-client.jar,hdfs:///user/oozie/phoenix/phoenix-spark-4.14.1-HBase-1.2.jar

nohup spark2-submit --class com.ufm.dp.streaming.SiFaStreaming \
--master yarn \
--deploy-mode client \
--driver-memory 2g \
--executor-memory 2g \
--executor-cores 2 \
--conf spark.executor.extraJavaOptions=-Djava.security.auth.login.config=/etc/kafka/conf/kafka_client_jaas.config \
--driver-class-path hdfs:///user/oozie/phoenix/phoenix-4.14.1-HBase-1.2-client.jar,hdfs:///user/oozie/phoenix/phoenix-spark-4.14.1-HBase-1.2.jar \
--jars hdfs:///user/oozie/phoenix/phoenix-4.14.1-HBase-1.2-client.jar,hdfs:///user/oozie/phoenix/phoenix-spark-4.14.1-HBase-1.2.jar \
/home/libo/jar/sifa-streaming.jar 1>streaming_sifa_success.log 2>streaming_sifa_error.log &
