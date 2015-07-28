#coding=utf-8

from mongoengine import *
import datetime

from mongoengine.django.auth import User


class JWTUser(User):

    username = StringField()
    password = StringField()

    User.meta = {
        'collection':'JWTUser'
    }

class Data(Document):

    name = StringField()
    age = IntField()

    meta = {
        'collection':'Data'
    }

