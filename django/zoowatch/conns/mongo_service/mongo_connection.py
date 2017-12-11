# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from pymongo import MongoClient


class MongoConnection(object):

    def __init__(self, host="127.0.0.1", port=27017, password="", database_name=""):
        client = MongoClient(
                        host = host,
                        port = port)

        self.db = client[database_name]

    def get_collection(self, name):
        self.collection = self.db[name]