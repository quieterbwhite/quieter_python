# -*- coding=utf-8 -*-
# Created Time: 2017年09月25日 星期一 16时35分32秒
# File Name: 02_concept.py

"""
1. ioloop 是tornado运行的核心

2. ioloop 封装了操作管理epoll的工作

3. 当ioloop实例启动时，ioloop将服务器监听的socket添加到epoll容器中，
然后循环等待epoll返回可处理的socket

4. 当有客户端发起连接后，ioloop从epoll容器中拿到了服务器监听的socket，
并调用服务器实例处理该监听socket的方法，接收连接请求，并将新的与客户端对应
的socket添加到epoll容器中，然后继续循环等待epoll返回可处理的socket

5. 当客户端发送过来请求数据后，ioloop从epoll中拿到了接收数据的socket，
并调用服务器实例处理该传输socket的方法，从socket中读取出http报文数据，
解析后调用Application的实例，进行路由分发，实例化具体的RequestHandler，
执行其中具体的http方法，生成响应数据并打包成http报文写入到缓冲区中。

6. 当与客户端对应的的socket可写时，ioloop从epoll中拿到了对应可写的socket，
将缓冲区中对应的响应报文数据写入到socket中传回给客户端，完成请求处理。

7. epoll 每次只返回给ioloop可以处理的socket，然后ioloop对拿到的socket依次
进行处理，有效充分的利用了CPU时间，进而达到提升支持高并发的能力。
"""