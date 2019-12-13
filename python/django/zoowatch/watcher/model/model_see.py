# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from utils.formatter import dumps_ident

@python_2_unicode_compatible
class See(models.Model):
    """ see """

    uid       = models.IntegerField(default=0)

    openid    = models.CharField(max_length=50)

    shopid    = models.IntegerField(default=0)

    content   = models.TextField()

    is_pub    = models.IntegerField(default=1)

    created   = models.CharField(max_length=50)

    updated   = models.CharField(max_length=50)

    class Meta:
        db_table = "see"
        app_label = "watcher"

    def __str__(self):
        return dumps_ident(self.to_json())

    def to_json(self):
        res = {
            "uid"     : self.uid,
            "openid"  : self.openid,
            "shopid"  : self.shopid,
            "content" : self.content,
            "is_pub"  : self.is_pub,
            "created" : self.created,
            "updated" : self.updated
        }
        return res
