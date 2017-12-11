# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.views.generic import View

from conns.redis_service.redis_client import redis_client

from logs.mylog import flogger


class RedisTestView(View):

    def get(self, request, *args, **kwargs):

        res = {'code':0}

        flogger.info("RedisTestView - redis obj id: %s" % id(redis_client))

        return JsonResponse(res)