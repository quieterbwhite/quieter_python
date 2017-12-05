# -*- coding=utf-8 -*-
# Created Time: 2015年10月27日 星期二 15时53分39秒
# File Name: urls.py

from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^test$', views.WatchTestView.as_view())

]