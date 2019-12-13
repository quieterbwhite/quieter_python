# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from watcher.model.model_me import Me

from logs.mylog import flogger


class MeMapper(object):

    @classmethod
    def me_add(cls, me_dict):

        me_obj = Me(**me_dict)
        me_obj.save(force_insert=True)
        return me_obj

    @classmethod
    def me_update(cls, me_dict):

        filters = {}
        updates = {}



    @classmethod
    def me_get(cls, me_dict):

        filters = {}

        if me_dict.get("uid"): filters.update({"uid" : me_dict["uid"]})

        me_obj = Me.objects.filter(**me_dict).first()

        flogger.info("MeMapper - me_get - me_obj: %s" % me_obj)

        return me_obj

    @classmethod
    def me_filter(cls, me_dict):

        filters = {}

        if me_dict.get("uid"): filters.update({"uid" : me_dict["uid"]})

        me_objs = Me.objects.filter(**me_dict)

        # order_by

        # limit

        # offset

        flogger.info("MeMapper - me_filter - me_objs: %s" % me_objs)

        return me_objs

    @classmethod
    def me_delete(cls, me_dict):

        filters = {}

        if me_dict.get("uid"): filters.update({"uid": me_dict["uid"]})

        delete_res = Me.objects.filter(**filters).delete()

        flogger.info("MeMapper - me_delete - delete_res: %s" % delete_res)

        return delete_res