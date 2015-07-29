# -*- coding=utf-8 -*-

from django.conf.urls import patterns, url

from views import TestView, TestDBView
from user_views import UserRegView, UserLoginView

urlpatterns = patterns('',
    url(r'^test$',TestView.as_view()),
    url(r'^data$',TestDBView.as_view()),

    url(r'^user/reg$',UserRegView.as_view()),
    url(r'^user/log$',UserLoginView.as_view()),
)
