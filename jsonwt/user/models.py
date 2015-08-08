# -*- coding=utf-8 -*-
# Created Time: 2015年08月08日 星期六 12时15分10秒
# File Name: models.py

from mongoengine import Document, StringField
from mongoengine.django.auth import User


class TokenUser(User):
    '''  '''

    mobile = StringField()
