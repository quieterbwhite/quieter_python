# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class BookInfo(models.Model):

    # 类变量，映射表结构
    btitle = models.CharField(max_length=20)

    # 对应 python datetime 类型
    bpub_date = models.DateField()

    def __str__(self):
        return self.btitle.encode("utf8")

    """
        b = BookInfo()
        b.btitle = "abc"
        # 这里的实例属性并不是在调用上面定义的类变量，只是动态绑定了一个同名的属性
        # 将来在 save() 的时候，就知道sql语句中应该用什么字段名。
    """


class HeroInfo(models.Model):

    hname = models.CharField(max_length=10)

    hgender = models.BooleanField()

    hcontent = models.CharField(max_length=1000)

    hbook = models.ForeignKey(BookInfo)

    def __str__(self):
        return self.hname.encode("utf8")
