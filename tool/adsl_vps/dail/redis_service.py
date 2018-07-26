# -*- coding=utf-8 -*-
# Created Time: 2018年07月23日 星期一 16时19分29秒
# File Name: redis_service.py

import redis
import random

REDIS_HOST = 'localhost'
REDIS_PASSWORD = None
REDIS_PORT = 6379
PROXY_KEY = 'adsl'

class RedisClient(object):
    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD, proxy_key=PROXY_KEY):
        """
        """
        self.db = redis.StrictRedis(host=host, port=port, password=password, decode_responses=True)
        self.proxy_key = proxy_key

    def set(self, name, proxy):
        """
        """
        return self.db.hset(self.proxy_key, name, proxy)

    def get(self, name):
        """
        """
        return self.db.hget(self.proxy_key, name)

    def count(self):
        """
        """
        return self.db.hlen(self.proxy_key)

    def remove(self, name):
        """
        """
        return self.db.hdel(self.proxy_key, name)

    def names(self):
        """
        """
        return self.db.hkeys(self.proxy_key)

    def proxies(self):
        """
        """
        return self.db.hvals(self.proxy_key)

    def random(self):
        """
        :return:
        """
        proxies = self.proxies()
        return random.choice(proxies)

    def all(self):
        """
        :return:
        """
        return self.db.hgetall(self.proxy_key)
