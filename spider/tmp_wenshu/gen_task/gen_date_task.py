# -*- coding=utf-8 -*-
# Created Time: 2018年07月27日 星期五 14时38分41秒
# File Name: gen_date_task.py

"""
生成日期任务并存入任务队列

主要用于全量抓取，抓取任务需要细分到每天，在这就是把输入的日期段处理成一个日期列表
然后存入kafka队列，后续抓取列表任务会获取到日期任务进行当日数据的抓取
"""

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

