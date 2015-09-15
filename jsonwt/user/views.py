# -*- coding=utf-8 -*-
# Created Time: 2015年08月08日 星期六 12时15分28秒
# File Name: views.py

'''
user json web token
'''

from django.views.generic import View
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib import auth
from django.conf import settings

from tokens import token_en
from manager import UserManager
from lib import res
from add_task import add_task_to_queue

import json, traceback, datetime


class UserPageRegisView(View):
    ''' 注册页面 '''

    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')


class UserRegisSmsView(View):
    ''' 用户短信注册 '''

    def post(self, request, *args, **kwargs):
        try:
            udict = json.loads(request.body)
            #UserManager.save_user(udict)
            #add_task_to_queue(udict['mobile'], udict['content'])
            mobile = '15202897835'
            content = 'tiger'
            print add_task_to_queue
            print 'type of func: ', add_task_to_queue

            add_task_to_queue(mobile, content)
        except ValueError:
            traceback.print_exc()
            res.update({'err_code':10002})
        except:
            traceback.print_exc()
            res.update({'err_code':10001})

        return JsonResponse(res)




class UserRegisView(View):
    ''' 注册 '''

    def post(self, request, *args, **kwargs):
        try:
            udict = json.loads(request.body)
            UserManager.save_user(udict)
        except ValueError:
            traceback.print_exc()
            res.update({'err_code':10002})
        except:
            traceback.print_exc()
            res.update({'err_code':10001})

        # TODO 统一为 json 返回增加 错误消息 继承/中间件
        return JsonResponse(res)


class UserLoginView(View):
    ''' 登录 '''

    def post(self, request, *args, **kwargs):
        try:
            udict = json.loads(request.body)
            user = auth.authenticate(
                    username=udict['username'],
                    password=udict['password']
                )
        except:
            traceback.print_exc()
            res.update({'err_code':'10004'})
            return JsonResponse(res)

        if not user:
            res.update({'err_code':10003})
            return JsonResponse(res)

        # set token
        payload = {
            'uid':str(user.id),
            'username':user.username,
            'mobile':'15202897835',
            'exp':datetime.datetime.utcnow() + datetime.timedelta(seconds=settings.JWT_EXP)
        }

        try:
            token = token_en(payload, settings.JWT_SECRET, settings.JWT_ALGORITHM)
            res.update({'token':token})
        except:
            traceback.print_exc()
            res.update({'err_code':10001})

        return JsonResponse(res)


class UserIndexView(View):
    ''' 用户中心 '''

    def post(self, request, *args, **kwargs):
        try:
            udict = json.loads(request.body)
            # 查询需要的信息返回
        except:
            traceback.print_exc()
            res.update({'err_code':'10004'})
            return JsonResponse(res)

        return JsonResponse(res)




















