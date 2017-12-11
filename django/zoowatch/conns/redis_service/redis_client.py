# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import redis

from django.conf import settings


class RedisConn(object):

    def __init__(self):
        conn_params_dict = {
            "host" : settings.REDIS_IP,
            "port" : settings.REDIS_PORT,
            # "password" : settings.REDIS_PASSWD
        }
        poll = redis.ConnectionPool(**conn_params_dict)
        self.conn = redis.Redis(connection_pool=poll)

redis_client = RedisConn()
