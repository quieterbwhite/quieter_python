# -*- coding=utf-8 -*-
# Created Time: 2017年12月06日 星期三 19时40分01秒
# File Name: 02_middleware.py

"""
Django exception middleware: TypeError: object() takes no parameters
"""

"""

Since you are using the new MIDDLEWARE settings, your Middleware class must accept a get_response argument: https://docs.djangoproject.com/en/1.10/topics/http/middleware/#writing-your-own-middleware

You could write your class like this:
"""

from django.http import HttpResponse

class ExceptionMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exception):
        return HttpResponse("in exception")

"""
You could also use the MiddlewareMixin to make your Middleware compatible with pre-1.10 and post-1.10 Django versions: https://docs.djangoproject.com/en/1.10/topics/http/middleware/#upgrading-pre-django-1-10-style-middleware
"""

from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

class ExceptionMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        return HttpResponse("in exception")

