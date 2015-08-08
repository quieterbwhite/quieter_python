# -*- coding=utf-8 -*-
# Created Time: 2015年08月08日 星期六 12时15分20秒
# File Name: manager.py

from models import TokenUser


class UserManager(object):
    '''  '''

    def __init__(self, uid):
        self.user = TokenUser.objects(id=uid).first()

    @classmethod
    def save_user(cls, user_dict):
        user = TokenUser.create_user(
                                username = user_dict['username'],
                                password = user_dict['password']
                            )
        user.mobile = user_dict['mobile']
        user.save()
