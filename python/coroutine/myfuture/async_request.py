# -*- coding=utf-8 -*-
# Created Time: 2018年03月07日 星期三 20时16分20秒
# File Name: async_request.py

"""
有了Future，我们可以包装一个AsyncRequest类，用以发起异步请求的操作。
"""

import socket
from selectors import DefaultSelector, EVENT_WRITE
from future import Future

selector = DefaultSelector()

class AsyncRequest(object):

    def __init__(self, host, url, port, timeout=5):
        self.sock = socket.socket()
        self.sock.settimeout(timeout)
        self.sock.setblocking(False)
        self.host = host
        self.url = url
        self.port = port
        self.method = None

    def get(self):
        self.method = "GET"
        self.request = "{} {} HTTP/1.0\r\nHost: {}\r\n\r\n".format(self.method, self.url, self.host)
        return self

    def process(self):
        if self.method is None:
            self.get()

        try:
            self.sock.connect((self.host, self.port))
        except BlockingIOError:
            pass

        self.f = Future()

        selector.register(self.sock.fileno(), EVENT_WRITE, self.on_connected)

        yield self.f

        selector.unregister(self.sock.fileno())

        self.sock.send(self.request.encode("ascii"))

        chunk = yield from read_all(self.sock)

        return chunk

    def on_connected(self, key, mask):
        self.f.set_result(None)

