# -*- coding=utf-8 -*-

from django.conf.urls import patterns, url

from views import TestView, TestDBView

urlpatterns = patterns('',
    url(r'^test$',TestView.as_view()),
    url(r'^data$',TestDBView.as_view()),

)
