# -*- coding=utf-8 -*-
# Created Time: 2018年07月27日 星期五 14时44分44秒
# File Name: consumer.py

from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "user-event",
    group_id = "user-event-test",
    bootstrap_servers = [
        "localhost:9093",
        "localhost:9094"
    ],
    value_deserializer=lambda m: json.loads(m.decode('ascii'))
)
for message in consumer:
    print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))
