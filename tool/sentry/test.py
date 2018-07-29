# -*- coding=utf-8 -*-
# Created Time: 2018年07月29日 星期日 17时46分27秒
# File Name: test.py

"""
username: 7072@qq.com
pwd: tiger
"""

from raven import Client

client = Client('http://c13f7e81e7d94d14a27435cdaa2c0af1:a2230e359afc4f8aa458fb8f4ad3c4e0@localhost:9000/1')

try:
    1 / 0
except ZeroDivisionError:
    client.captureException()
