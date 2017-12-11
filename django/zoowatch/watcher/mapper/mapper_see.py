# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from watcher.model.model_see import See

from logs.mylog import flogger


class SeeMapper(object):

    @classmethod
    def see_add(cls, see_dict):

        see_obj = See(**see_dict)
        see_obj.save(force_insert=True)
        return see_obj

    @classmethod
    def see_update(cls, see_dict):

        filters = {}
        updates = {}



    @classmethod
    def see_get(cls, see_dict):

        filters = {}

        if see_dict.get("uid"): filters.update({"uid" : see_dict["uid"]})

        see_obj = See.objects.filter(**see_dict).first()

        flogger.info("SeeMapper - see_get - see_obj: %s" % see_obj)

        return see_obj

    @classmethod
    def see_filter(cls, see_dict):

        filters = {}

        if see_dict.get("uid"): filters.update({"uid" : see_dict["uid"]})

        see_objs = See.objects.filter(**see_dict)

        # order_by

        # limit

        # offset

        flogger.info("SeeMapper - see_filter - see_objs: %s" % see_objs)

        return see_objs

    @classmethod
    def see_delete(cls, see_dict):

        filters = {}

        if see_dict.get("uid"): filters.update({"uid": see_dict["uid"]})

        delete_res = See.objects.filter(**filters).delete()

        flogger.info("SeeMapper - see_delete - delete_res: %s" % delete_res)

        return delete_res