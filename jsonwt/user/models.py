#coding=utf-8

from mongoengine import *
import datetime

from mongoengine.django.auth import User


class JWTUser(User):

    mobile = StringField()
    email = EmailField()
    token = StringField()

    # 不使用 mongoengine 的索引, 自己通过数据库创建索引
    # mobile, username
    User.meta = {
        'collection':'JWTUser'
    }

class Data(Document):

    name = StringField()
    age = IntField()

    meta = {
        'collection':'Data'
    }

