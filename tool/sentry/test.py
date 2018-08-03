# -*- coding=utf-8 -*-
# Created Time: 2018年07月29日 星期日 17时46分27秒
# File Name: test.py

"""
username: 7072@qq.com
pwd: tiger
"""

from raven import Client

client = Client('http://16d58f62e28e4e1b8d5c1f2a6bc8d384:4d99f0871b104cb9b926e15ba86e904c@localhost:9000/1')

try:
    a = int([])
#except ZeroDivisionError:
except Exception:
    client.captureException()
