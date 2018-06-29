# -*- coding: utf-8 -*-

from pymongo import MongoClient
#from urllib.parse import quote_plus


class MongoService(object):

    def __init__(self, host="127.0.0.1", port=27017, user="", password="", database_name=""):
        client = MongoClient(
            host=host,
            port=port
        )

        self.db = client[database_name]

    def get_collection(self, collection_name):
        self.conn = self.db[collection_name]
        return self.conn

class MongoServiceBak(object):
    """ 加了用户验证的话就用这个 """

    def __init__(self, host="127.0.0.1", port="27017", user="", password="", database_name=""):

        uri = "mongodb://{}:{}@{}:{}/{}".format(quote_plus(user), quote_plus(password), host, port, "admin")
        client = MongoClient(uri)
        self.db = client[database_name]

    def get_collection(self, collection_name):

        self.conn = self.db[collection_name]
        return self.conn

mongo_service = MongoService(
    "127.0.0.1",
    27017,
    database_name="judgements"
)


