# -*- coding=utf-8 -*-
# Created Time: 2015年12月16日 星期三 20时03分42秒
# File Name: global_exception.py


from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

from logs.mylog import flogger


class GlobalExceptionMiddleware(MiddlewareMixin):
    """ 处理未捕获的全局异常 """

    def process_exception(self, request, exception):
        flogger.info("GlobalExceptionMiddleware - Catch a global exception")
        flogger.exception(exception)

        # TODO 发送邮件通知

        # TODO 发送微信通知

        return JsonResponse({"code" : -1, "msg" : "error"})