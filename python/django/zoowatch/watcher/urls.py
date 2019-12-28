# -*- coding=utf-8 -*-
# Created Time: 2015年10月27日 星期二 15时53分39秒
# File Name: urls.py

from django.conf.urls import url

from watcher.view import view_watch, view_redis

urlpatterns = [

    url(r'^test$', view_watch.WatchTestView.as_view()),

    url(r'^redis$', view_redis.RedisTestView.as_view())

]