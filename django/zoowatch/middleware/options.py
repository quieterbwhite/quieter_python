# -*- coding=utf-8 -*-
# Created Time: 2015年12月16日 星期三 20时03分42秒
# File Name: options.py

from django.http import JsonResponse

from django.utils.deprecation import MiddlewareMixin


class OptionsHandleMiddleware(MiddlewareMixin):
    """ 前端给了个多余的options请求，直接返回 """

    def process_request(self, request):

        method = request.method

        if method == "OPTIONS":
            return JsonResponse({"code" : 0})