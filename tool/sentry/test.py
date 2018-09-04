# -*- coding=utf-8 -*-
# Created Time: 2018年07月29日 星期日 17时46分27秒
# File Name: test.py

"""
username: 7072@qq.com
pwd: tiger
"""

from raven import Client

client = Client('http://ac895c3258454b51ad0d9f95f3a7e9db:dde5a524fb224b51866ba23a6153007a@sentry.shijiyunhe.com/2')

try:
    a = 1/0
#except ZeroDivisionError:
except Exception:
    client.captureException()
