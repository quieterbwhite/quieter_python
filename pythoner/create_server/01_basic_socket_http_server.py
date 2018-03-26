# -*- coding=utf-8 -*-
# Created Time: 2017年09月08日 星期五 22时58分34秒
# File Name: 01_basic_socket_http_server.py

from socket import *
from multiprocessing import *
import os
import re

HTML_ROOT_DIR = "./01_content/"

def main():

    tcpSerSocket = socket(AF_INET, SOCK_STREAM)
    tcpSerSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    address = ("", 7777)
    tcpSerSocket.bind(address)
    tcpSerSocket.listen(128)

    try:
        while 1:
            print "Main process, wait for new conn..."
            newSocket, clientAddr = tcpSerSocket.accept()

            client = Process(target=pro, args=(newSocket, clientAddr))
            client.start()

            newSocket.close()
    finally:
        tcpSerSocket.close()


def pro(socket, addr):

    while 1:

        recvData = socket.recv(1024)

        if not len(recvData) > 0:
            print "Lose conn"
            break

        request_lines = recvData.splitlines()
        for line in request_lines:
            print line

        # 解析请求报文
        request_start_line = request_lines[0]
        file_name = re.match(r"\w+ +/([^ ]*) ", request_start_line).group(1)
        print "file_name: ", file_name
        file_path = os.path.join(HTML_ROOT_DIR, file_name)
        print "file_path: ", file_path

        try:
            sfile = open(file_path, "rb")
        except IOError:
            response_start_line = "HTTP/1.1 404 Not Found \r\n"
            response_headers = "Server: My server\r\n"
            response_body = "Lost"
        else:
            response_start_line = "HTTP/1.1 200 OK \r\n"
            response_headers = "Server: My server\r\n"
            response_body = sfile.read()
            sfile.close()

        response = response_start_line + response_headers + "\r\n" + response_body

        # python2
        socket.send(response)

        # python3
        # socket.send(bytes(response, "utf-8"))

        break

    socket.close()

if __name__ == "__main__":
    main()
