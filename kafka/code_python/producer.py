# -*- coding=utf-8 -*-
# Created Time: 2018年07月27日 星期五 14时38分41秒
# File Name: send_message.py

from kafka import KafkaProducer
from kafka.errors import KafkaError
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

try:
    record_metadata = future.get(timeout=10)
    print(record_metadata)
except KafkaError as e:
    print(e)

print("done")
