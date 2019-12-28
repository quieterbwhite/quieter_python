# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.views.generic import View

from watcher.service.service_publish import PublishService

from utils.container import data_list

from conns.redis_service.redis_client import redis_client

from logs.mylog import flogger


class WatchTestView(View):

    def get(self, request, *args, **kwargs):

        res = {'code':0}

        flogger.info(data_list)

        is_url_exists = redis_client.conn.exists("url")

        flogger.info("is_url_exists: %s" % is_url_exists)

        flogger.info("WatchTestView - redis obj id: %s" % id(redis_client))

        return JsonResponse(res)

        see_dict = {
            "uid" : 5,
            "openid" : 5,
            "shopid" : 5,
            "content" : "four",
            "is_pub" : 1,
            "created" : "2017-10-01",
            "updated" : "2018-09-01"
        }

        me_dict = {
            "title" : "the five title"
        }

        PublishService.publish(see_dict, me_dict)

        res.update({"data":data_list})

        return JsonResponse(res)