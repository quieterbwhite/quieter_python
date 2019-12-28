# -*- coding=utf-8 -*-
# Created Time: 2018年03月07日 星期三 19时51分14秒
# File Name: 05_async_spider_baidu.py

"""
IO复用：预先告知内核，使内核一旦发现进程指定的一个或多个IO条件就绪
（输入准备被读取，或描述符能承接更多的输出），它就通知进程。
"""

from selectors import DefaultSelector, EVENT_WRITE

selector = DefaultSelector()

sock = socket.socket()
sock.setblocking(False)

try:
    sock.connect(("www.baidu.com", 80))
except BlockingIOError:
    pass

def connected():
    # 有写事件时，表示已经连接上，将文件描述符从事件循环中删除
    selector.unregister(sock.fileno())
    print("connected!")

selector.register(sock.fileno(), EVENT_WRITE, connected)
