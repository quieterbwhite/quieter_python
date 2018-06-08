# -*- coding=utf-8 -*-
# Created Time: 2018年06月08日 星期五 17时35分15秒
# File Name: daemon.py

import sys
import os
import time
import atexit
from signal import SIGTERM


class Daemon:
    """
    通用的Daemonlize类，能将一个程序变成守护进程
    使用方式：继承Daemon类，然后重写run()函数即可
    """

    def __init__(self, pidfile='nbMon.pid', stdin='/dev/null', stdout='nbMon.log', stderr='nbMon.log'):
        self.stdin = stdin
        self.stdout = stdout
        self.stderr = stderr
        self.pidfile = pidfile

    def daemonize(self):
        """
        双重fork，具体原因参见Stevens写的《UNIX环境高级编程》
        书籍链接参见：http://book.douban.com/subject/1788421/
        还有：
        http://www.erlenstar.demon.co.uk/unix/faq_2.html#SEC16
        """
        try:
            pid = os.fork()
            if pid > 0:
                # 退出第一个“爷爷进程”，因为后面还要第二次fork
                # 所以这个进程辈分是“爷爷”
                sys.exit(0)
        except OSError, e:
            sys.stderr.write("fork #1 failed: %d (%s)\n" %
                             (e.errno, e.strerror))
            sys.exit(1)

        # 需要执行一些操作避免可能从父进程继承过来的影响守护进程的设定
        # 改变当前工作目录
        os.chdir("/")
        # 设置sid，成为session Leader
        os.setsid()
        # 重设umask
        os.umask(0)

        # 第二次fork
        try:
            pid = os.fork()
            if pid > 0:
                # 父进程依然退出
                sys.exit(0)
        except OSError, e:
            sys.stderr.write("fork #2 failed: %d (%s)\n" %
                             (e.errno, e.strerror))
            sys.exit(1)

        # 重定向0、1、2三个fd（依次为标准输入、标准输出、错误输出）
        # 这里需要注意，有些不讲究的程序或者文章，会直接将0、1、2关闭，
        # 这样会造成一定的隐患，可能会导致后续操作打开的文件句柄占用
        # 0、1、2这三个一般认为有特殊含义的句柄，会导致一些莫名其妙的问题发生
        # 所以这里最好的建议是，将这三个fd重新定向到/dev/null,或者相应的日志文件

        # 重新定向之前flush一次，确保该打印出来的文字已经输出
        sys.stdout.flush()
        sys.stderr.flush()
        si = file(self.stdin, 'r')
        so = file(self.stdout, 'a+')
        se = file(self.stderr, 'a+', 0)
        os.dup2(si.fileno(), sys.stdin.fileno())
        os.dup2(so.fileno(), sys.stdout.fileno())
        os.dup2(se.fileno(), sys.stderr.fileno())

        """
        写pid文件
        """
        # 这里设定一个程序退出时回调，但必须知道的是，这个回调
        # 在一些情况下并不保证一定会被执行，比如被kill -9
        atexit.register(self.delpid)
        pid = str(os.getpid())
        file(self.pidfile, 'w+').write("%s\n" % pid)

    def delpid(self):
        os.remove(self.pidfile)

    def start(self):
        """
        启动守护进程
        """
        # 检查pid文件是否存在，如果存在就认为程序还在运行
        try:
            pf = file(self.pidfile, 'r')
            pid = int(pf.read().strip())
            pf.close()
        except IOError:
            pid = None

        if pid:
            message = "pidfile %s already exist. Daemon already running?\n"
            sys.stderr.write(message % self.pidfile)
            sys.exit(1)

        # 开始变身守护进程，哈哈哈哈
        self.daemonize()
        self.run()

    def stop(self):
        """
        停止守护进程
        """
        # 从pid文件中获取进程id
        try:
            pf = file(self.pidfile, 'r')
            pid = int(pf.read().strip())
            pf.close()
        except IOError:
            pid = None

        if not pid:
            message = "pidfile %s does not exist. Daemon not running?\n"
            sys.stderr.write(message % self.pidfile)
            return

        # 开始尝试kill掉守护进程
        try:
            while 1:
                os.kill(pid, SIGTERM)
                time.sleep(0.1)
        except OSError, err:
            err = str(err)
            if err.find("No such process") > 0:
                if os.path.exists(self.pidfile):
                    os.remove(self.pidfile)
            else:
                print str(err)
                sys.exit(1)

    def restart(self):
        """
        重启
        """
        self.stop()
        self.start()

    def run(self):
        """
        这个方法是空的，所以要想使用这个类，必须在子类中
        重写这个函数，这个函数应该写的是程序的主逻辑循环。
        后面这个函数将会在start()和restart()函数中被调用。
        """
