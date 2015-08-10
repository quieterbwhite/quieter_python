# -*- coding=utf-8 -*-
# Created Time: 2015年08月08日 星期六 12时15分02秒
# File Name: urls.py

from django.conf.urls import patterns, url
from views import UserRegisView, UserPageRegisView, UserLoginView, UserIndexView


urlpatterns = patterns(
    '',
    url(r'/regis_page$', UserPageRegisView.as_view()),
    url(r'/regis$', UserRegisView.as_view()),
    url(r'/login$', UserLoginView.as_view()),
    url(r'/index$', UserIndexView.as_view()),

)
