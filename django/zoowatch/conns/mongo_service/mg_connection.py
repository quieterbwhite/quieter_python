# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from conns.mongo_service.mongo_connection import MongoConnection


class MgCollection(MongoConnection):

    def __init__(self, host="127.0.0.1", port=27017, password="", database_name="", collection_name=""):
       super(MgCollection, self).__init__(host=host, port=port, database_name=database_name)
       self.get_collection(collection_name)

    def update_and_save(self, obj):
       if self.collection.find({'id': obj.id}).count():
           self.collection.update({ "id": obj.id},{'id':123,'name':'test'})
       else:
           self.collection.insert_one({'id':123,'name':'test'})

    def remove(self, obj):
        if self.collection.find({'id': obj.id}).count():
           self.collection.delete_one({ "id": obj.id})

mg_conn = MgCollection()