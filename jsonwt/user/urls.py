# -*- coding=utf-8 -*-

from django.conf.urls import patterns, url

from user.views import TestView, TestDBView
from user.user_views import UserRegView, UserLoginView, UserIndexView

urlpatterns = patterns('',
    url(r'^test$',TestView.as_view()),
    url(r'^data$',TestDBView.as_view()),

    url(r'^user/reg$',UserRegView.as_view(), name='reg'),
    url(r'^user/log$',UserLoginView.as_view(), name='log'),
    url(r'^user/index$',UserIndexView.as_view(), name='index'),

)
