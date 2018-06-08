# -*- coding=utf-8 -*-
# Created Time: 2018年06月08日 星期五 17时36分23秒
# File Name: main.py

# 从之前写好的守护进程类中导入Daemon
from daemon import Daemon
import socket
import select
import time
# 导入pdb，即Python debug模块，方便调试
import pdb

# 设定这个变量，可以控制本文件在被import *
# 的时候导入的变量、函数和类的范围
__all__ = ["nbNet"]
#DEBUG = True

# 这个文件的内容会在后面详述
from nbNetUtils import *

# 我们住程序的conn_state的类原型

class STATE:

    def __init__(self):
        self.state = "accept"  # 初始状态
        self.have_read = 0
        # 我们的程序在开始的时候总是要读取10个字节的头
        self.need_read = 5
        self.have_write = 0
        self.need_write = 0

        # 读写缓冲区
        self.buff_read = ""
        self.buff_write = ""
        # 用来后续存放sock对象
        self.sock_obj = ""

    def printState(self):
        """
        debug输出函数
        """
        if DEBUG:
            dbgPrint('\n - current state of fd: %d' % self.sock_obj.fileno())
            dbgPrint(" - - state: %s" % self.state)
            dbgPrint(" - - have_read: %s" % self.have_read)
            dbgPrint(" - - need_read: %s" % self.need_read)
            dbgPrint(" - - have_write: %s" % self.have_write)
            dbgPrint(" - - need_write: %s" % self.need_write)
            dbgPrint(" - - buff_write: %s" % self.buff_write)
            dbgPrint(" - - buff_read:  %s" % self.buff_read)
            dbgPrint(" - - sock_obj:   %s" % self.sock_obj)


class nbNetBase:
    '''
    non-blocking Net类，首先我们设定了一套通信的协议，以10个byte的
    ASCII码数字的头来表示，后续数据的长度，例如：
    0000000005HELLO
    0000000001a
    0000000012hello world\n
    这样做的好处在于，我们可以很容易的解析消息的结束位置。
    并且能够在这套框架下进行任何数据的传输，包括各种二进制数据，而不需要转义。
    '''

    def setFd(self, sock):
        """把sock放进全局的conn_state字典里"""
        dbgPrint("\n -- setFd start!")
        tmp_state = STATE()
        tmp_state.sock_obj = sock
        self.conn_state[sock.fileno()] = tmp_state
        self.conn_state[sock.fileno()].printState()
        dbgPrint("\n -- setFd end!")

    def accept(self, fd):
        """在fd上进行accept，并且把socket设置成非阻塞模式"""
        dbgPrint("\n -- accept start!")
        sock_state = self.conn_state[fd]
        sock = sock_state.sock_obj
        conn, addr = sock.accept()
        # 把socket设置成非阻塞模式
        conn.setblocking(0)
        return conn

    def close(self, fd):
        """关闭fd，从epoll中取消关注，清理conn_state里相关的数据"""
        try:
            # cancel of listen to event
            sock = self.conn_state[fd].sock_obj
            sock.close()
        except:
            dbgPrint("Close fd: %s abnormal" % fd)
        finally:
            self.epoll_sock.unregister(fd)
            self.conn_state.pop(fd)

    def read(self, fd):
        """
        读取fd中的数据（非阻塞模式）
        并且设置各个计数器的数值，以供后续处理
        返回值是个字符串，表示下一步需要进行的处理，如：
        “readcontent”、“process”、“readmore”
        """
        # pdb.set_trace()
        try:
            # 从conn_state字典中取出连接
            sock_state = self.conn_state[fd]
            conn = sock_state.sock_obj
            if sock_state.need_read <= 0:
                raise socket.error

            # 进行一次非阻塞的读取
            one_read = conn.recv(sock_state.need_read)
            dbgPrint("\tread func fd: %d, one_read: %s, need_read: %d" %
                     (fd, one_read, sock_state.need_read))

            # 如果什么都没有读到，那应该是socket出错了
            if len(one_read) == 0:
                raise socket.error
            # 将读到的数据放入buff_read，
            # 设定have_read（已经从socket中读取的数量）
            # 设定need_read（还需从socket中要读取的数量）
            sock_state.buff_read += one_read
            sock_state.have_read += len(one_read)
            sock_state.need_read -= len(one_read)
            sock_state.printState()

            # 如果已经读取的数据是10个byte，那么说明数据的10字节头已经读取完毕，
            # 我们可以解析判断后续的数据的长度了
            if sock_state.have_read == 5:
                # 由于是ASCII的数据头，我们需要用int()将它转化成数字
                header_said_need_read = int(sock_state.buff_read)
                if header_said_need_read <= 0:
                    raise socket.error
                sock_state.need_read += header_said_need_read
                sock_state.buff_read = ''

        # 为了方便大家理解，这里打印一些debug信息
                sock_state.printState()
                return "readcontent"
            elif sock_state.need_read == 0:
                # 所有数据已经读取完毕，转入业务逻辑处理“process”
                return "process"
            else:
                # 出去上述的所有情况，剩下的情况就是还需要读取更多的数据
                return "readmore"
        except (socket.error, ValueError), msg:
            # 进行一些异常处理
            try:
                # errno等于11，即“EAGAIN”。是表示，还可以尝试进行一次读取
                if msg.errno == 11:
                    dbgPrint("11 " + msg)
                    return "retry"
            except:
                pass
            # 除去上述的特殊情况，发生了任何错误，不要挣扎，直接把socket关闭
            return 'closing'

    def write(self, fd):
        """
        非阻塞的写数据到socket中，返回值的涵义和上述的read一致
        """
        # 还是取出fd对应的sock_state结构体
        sock_state = self.conn_state[fd]
        conn = sock_state.sock_obj
        last_have_send = sock_state.have_write
        try:
            # 非阻塞的发送数据，这里send的返回值是已经成功发送的数据量
            have_send = conn.send(sock_state.buff_write[last_have_send:])
            sock_state.have_write += have_send
            sock_state.need_write -= have_send
            if sock_state.need_write == 0 and sock_state.have_write != 0:
                # 如果已经全部发送成功，返回“writecomplete”
                sock_state.printState()
                dbgPrint('\n write data completed!')
                return "writecomplete"
            else:
                return "writemore"
        except socket.error, msg:
            # 发生错误，直接关闭socket
            return "closing"

    def run(self):
        """
        这个函数是装个状态机的主循环所在
        """
        while True:

            # 这部分就是我们上面多次提到的epoll
            # poll()返回的epoll_list就是有事件发生的fd的list
            # 需要在循环中按照event的类型分别处理，一般分为以下几种类型
            #  EPOLLIN ：表示对应的文件描述符可以读；
            #  EPOLLOUT：表示对应的文件描述符可以写；
            #  EPOLLPRI：表示对应的文件描述符有紧急的数据可读；一般不需要特殊处理
            #  EPOLLERR：表示对应的文件描述符发生错误；后面这两种需要关闭socket
            #  EPOLLHUP：表示对应的文件描述符被挂断；
            epoll_list = self.epoll_sock.poll()
            for fd, events in epoll_list:
                sock_state = self.conn_state[fd]
                if select.EPOLLHUP & events:
                    dbgPrint("EPOLLHUP")
                    sock_state.state = "closing"
                elif select.EPOLLERR & events:
                    dbgPrint("EPOLLERR")
                    sock_state.state = "closing"
                # 调用状态机
                self.state_machine(fd)

    def state_machine(self, fd):
        """
        这里的逻辑十分的简单：“按照不同fd的state，调用不同的函数即可”
        具体的对应表见nbNet的__init__()
        """
        sock_state = self.conn_state[fd]
        self.sm[sock_state.state](fd)


class nbNet(nbNetBase):

    def __init__(self, addr, port, logic):
        dbgPrint('\n__init__: start!')
        # 初始化conn_state字典，这个字典将会保存每个连接的状态
        # 以及连接的读写内容。
        self.conn_state = {}
        # 初始化监听socket
        # socket.AF_INET指的是以太网
        # socket.SOCK_STREAM指的是TCP
        self.listen_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        # 开启SO_REUSEADDR，这样当监听端口处于各种xxx_WAIT的状态的时候
        # 也能正常的listen、bind
        self.listen_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 绑定在制定的IP和端口上
        self.listen_sock.bind((addr, port))
        # 指定backlog数，这里初学者可能会存在一个误区，需要解释一下：
        #   有些地方把listen的参数成为“积压值”或者backlog，
        #   最大连接数是最大能处理的连接数（accept了丢一边晾着是耍流氓）
        #   提高并发处理能力是门学问，不单是提高“最大连接数”，两点结论：
        #     1. backlog不能提高“最大连接数”
        #     2. backlog不宜设置过大
        #   举个栗子，假设我们的服务器是一个非常受欢迎的饭店：
        #   最大连接数就是这个饭店最大能容纳的顾客人数，backlog就是门外允许排队的最大长度。
        #   如果饭店点菜慢上菜也慢（服务器的处理不能满足要求），饭店将很快被被顾客坐满（最大连接数上限）
        #   ，门口排位如果无限排下去（backlog设置非常大），可能还不如告诉顾客现在人太多了，
        #   我们处理不过来，不过等会儿再来试试。
        #   想要提高服务质量只能通过提高翻桌率（服务器处理速度）来实现。
        self.listen_sock.listen(5)  # backlog
        # 将listen socket同样放入conn_state
        self.setFd(self.listen_sock)
        # 初始化epoll的fd
        self.epoll_sock = select.epoll()
        # 这里指定我们的listen socket只关注EPOLLIN，即connect过来的连接
        # LT 是这里的默认, 想要ET 需要改成'select.EPOLLIN | select.EPOLLET'
        self.epoll_sock.register(self.listen_sock.fileno(), select.EPOLLIN)
        # 业务逻辑处理函数
        self.logic = logic
        # 状态机的各个状态的处理函数，这里的self.sm是一个key是字符串，value是函数的字典
        self.sm = {
            "accept": self.accept2read,
            "read": self.read2process,
            "write": self.write2read,
            "process": self.process,
            "closing": self.close,
        }
        dbgPrint('\n__init__: end, register no: %s' %
                 self.listen_sock.fileno())

    def process(self, fd):
        """
        调用业务逻辑处理函数self.logic，然后将它返回的字符串当成是
        Server对Client的回应
        通过约定好调用的函数原型，就可以实现比较干净的业务逻辑和网络框架的分离
        """
        sock_state = self.conn_state[fd]
        response = self.logic(sock_state.buff_read)
        # 组装给Client回应的10字节协议头
        sock_state.buff_write = "%05d%s" % (len(response), response)
        sock_state.need_write = len(sock_state.buff_write)
        sock_state.state = "write"
        self.epoll_sock.modify(fd, select.EPOLLOUT)
        sock_state.printState()

    def accept2read(self, fd):
        """
        这个函数主要完成accept到等待数据读取的状态转换
        """
        # accept一个连接之后，需要注册，初始化state为read
        conn = self.accept(fd)
        self.epoll_sock.register(conn.fileno(), select.EPOLLIN)
        self.setFd(conn)
        self.conn_state[conn.fileno()].state = "read"
        # 现在accept 到 read的转换完成了
        # 需要明确的是，我们的listen socket还是处于等待连接到来
        # 的accept状态
        dbgPrint("\n -- accept end!")

    def read2process(self, fd):
        """
        这个函数主要完成read完所有请求到处理业务逻辑的状态转换
        """
        # pdb.set_trace()
        read_ret = ""
        try:
            read_ret = self.read(fd)
        except (Exception), msg:
            dbgPrint(msg)
            read_ret = "closing"
        if read_ret == "process":
            # 数据接收完成，转换到process阶段
            self.process(fd)
        # readcontent、readmore、retry 都不用改变socket的state
        elif read_ret == "readcontent":
            pass
        elif read_ret == "readmore":
            pass
        elif read_ret == "retry":
            pass
        elif read_ret == "closing":
            self.conn_state[fd].state = 'closing'
            # 发生错误直接关闭，做到快速失败
            self.state_machine(fd)
        else:
            raise Exception("impossible state returned by self.read")

    def write2read(self, fd):
        """
        这个函数主要完成write给client回应到等待数据读取的状态转换。
        这个情况就是我们经常听到的“长连接”
        """
        try:
            write_ret = self.write(fd)
        except socket.error, msg:
            write_ret = "closing"

        if write_ret == "writemore":
            pass
            # 写数据完成，重置各种计数器，开始等待新请求过来
        elif write_ret == "writecomplete":
            sock_state = self.conn_state[fd]
            conn = sock_state.sock_obj
            self.setFd(conn)
            self.conn_state[fd].state = "read"
            self.epoll_sock.modify(fd, select.EPOLLIN)
        elif write_ret == "closing":
            # 发生错误直接关闭，做到快速失败
            dbgPrint(msg)
            self.conn_state[fd].state = 'closing'
            # closing directly when error.
            self.state_machine(fd)


if __name__ == '__main__':
    # 这个是我们演示用的“业务逻辑”，做的事情就是将请求的数据反转
    # 例如：
    #   收到：0000000005HELLO
    #   回应：0000000005OLLEH
    def logic(d_in):
        return(d_in[::-1])

    # 监听在0.0.0.0:9076
    reverseD = nbNet('0.0.0.0', 9090, logic)

    # 状态机开始运行，除非被kill，否则永不退出
    reverseD.run()
