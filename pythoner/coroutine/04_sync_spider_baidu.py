# -*- coding=utf-8 -*-
# Created Time: 2018年03月07日 星期三 19时34分05秒
# File Name: 04_sync_spider_baidu.py

import socket
from time import time

def sync_way():

    for i in range(100):
        sock = socket.socket()
        sock.connect(("www.baidu.com", 80))
        print("connected")

        request = "GET {} HTTP/1.0\r\nHost: www.baidu.com\r\n\r\n".format("/s?wd={}".format(i))
        sock.send(request.encode("ascii"))

        response = b''

        chunk = sock.recv(4096)

        while chunk:
            response += chunk
            chunk = sock.recv(4096)

        print(response)
        print("done!")

start = time()

sync_way()

end = time()

print("Cost {} seconds".format(end - start))



