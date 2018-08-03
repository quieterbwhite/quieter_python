# -*- coding=utf-8 -*-
# Created Time: 2018年07月29日 星期日 17时46分27秒
# File Name: test.py

"""
username: 7072@qq.com
pwd: tiger
"""

from raven import Client

client = Client('http://1e1fe90d82bd4980868b84948e8ff885@sentry.shijiyunhe.com/1')

try:
    1 / 0
except ZeroDivisionError:
    client.captureException()
