# -*- coding=utf-8 -*-
# Created Time: 2017年11月21日 星期二 00时05分13秒
# File Name: 07_bug_of_libxml.py

"""
libxml/xmlversion.h:No such file or directory


编译安装 lxml 时，出现了如下错误：

libxml/xmlversion.h: No such file or directory
出现这个错误是因为有些依赖包没有安装：

libxml2
libxml2-dev
libxslt
libxslt-dev
只要安装好要上面的依赖包就可以了

"""
