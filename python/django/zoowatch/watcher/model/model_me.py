# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from utils.formatter import dumps_ident

@python_2_unicode_compatible
class Me(models.Model):
    """ me """

    title = models.CharField(max_length=50)

    class Meta:
        db_table = "me"
        app_label = "watcher"

    def __str__(self):
        return dumps_ident(self.to_json())

    def to_json(self):
        res = {
            "title"   : self.title
        }
        return res
