# -*- coding=utf-8 -*-
# Created Time: 2015年08月08日 星期六 12时15分28秒
# File Name: views.py

'''
user json web token
'''

from django.views.generic import View
from django.http import JsonResponse
from django.shortcuts import render

from manager import UserManager
from lib import res

import json, traceback


class UserPageRegisView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')


class UserRegisView(View):
    '''  '''

    def get(self, request, *args, **kwargs):
        try:
            user_dict = json.loads(request.body)
            print 'user_dict: ', user_dict
            #UserManager.save_user(user_dict)
            print 'save user'
        except ValueError:
            traceback.print_exc()
            res.update({'err_code':10002})
        except:
            traceback.print_exc()
            res.update({'err_code':10001})

        # TODO 统一为 json 返回增加 错误消息 继承/中间件
        return JsonResponse(res)
