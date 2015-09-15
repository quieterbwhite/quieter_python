# -*- coding=utf-8 -*-
# Created Time: Fri 05 Sep 2014 05:31:23 PM CST
# File Name: token_auth.py

'''
判断登录中间件
'''

from django.conf import settings
from django.http import JsonResponse
from user.lib import res

from user.tokens import token_de

class TokenAuthMiddleware(object):
    '''
        模块 -> url 列表  模块 -> 角色  角色 -> 用户
        也就是如果需要一个权限管理系统的话,定义模块与url的映射,模块与角色的映射,
        角色与用户的映射,可以增删改查管理权限,这个要做的话,还要仔细考虑一下.
    '''

    def process_request(self, request):

        #print 'meta: ', request.META

        http_token = request.META.get('HTTP_TOKEN', '')

        req_path = request.path

        need_auth_view = [
            '/user/index'
        ]

        if req_path in need_auth_view:
            de_data, err_code = token_de(
                                            http_token,
                                            settings.JWT_SECRET,
                                            settings.JWT_ALGORITHM,
                                            settings.JWT_OPTIONS
                                        )
            if not de_data:
                res.update({'err_code':err_code})
                return JsonResponse(res)

