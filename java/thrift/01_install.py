# -*- coding=utf-8 -*-
# Created Time: 2017年09月28日 星期四 01时16分58秒
# File Name: 01_install.py

"""
ref:

    http://blog.csdn.net/huanbia/article/details/77098205

    http://blog.csdn.net/a19881029/article/details/69569111

    http://thrift.apache.org/docs/install/debian

"""

"""
1. 首先安装依赖项：

    sudo apt-get install automake bison flex g++ git libboost1.55-all-dev libevent-dev libssl-dev libtool make pkg-config

    sudo apt-get install python-dev python3-dev

2.将thrift安装包下载下来，并解压安装

    tar -zxvf thrift-0.10.0.tar.gz
    cd thrift-0.10.0/
    ./configure     // ./configure --prefix=/usr/local/thrift
    sudo make
    sudo make install

安装成功后可通过如下命令来验证，如果出现Thrift version 0.10.0则代表安装成功

bwhite@os:~/software/thrift-0.10.0$ which thrift
/usr/local/bin/thrift
bwhite@os:~/software/thrift-0.10.0$

thrift -version


可能出现的问题
当执行thrift -version的时候可能出现如下错误：

thrift: error while loading shared libraries: libthriftc.so.0: cannot open shared object file: No such file or directory

此时首先去查看一下/usr/local/lib下是否有libthriftc.so.0文件

ll /usr/local/lib/libthriftc.so.0
如果没有请在网上下载并安装。
如果有则需要将该文件所在的路径添加到到/etc/ld.so.conf即可：
(以下命令需要切换到root用户)

echo "/usr/local/lib" >> /etc/ld.so.conf
ldconfig
此时切换回普通用户输入thrift -version命令应该可以看到相应的版本了。

"""
