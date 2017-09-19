# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class BookInfo(models.Model):

    btitle = models.CharField(max_length=20)

    bpub_date = models.DateField()

    def __str__(self):
        return self.btitle


class HeroInfo(models.Model):

    hname = models.CharField(max_length=10)

    hgender = models.BooleanField()

    hcontent = models.CharField(max_length=1000)

    hbook = models.ForeignKey(BookInfo)
