# -*- coding=utf-8 -*-
# Created Time: 2015年06月17日 星期三 14时47分00秒
# File Name: django_tools.py


from django.core.paginator import Paginator
import urllib


def pages(queryset, page=1, page_size=5):
    ''' 分页函数
    queryset  queryset:   查询结果
    int       page    :   第几页
    int       perPage :   每页多少条数据
    '''

    paginator = Paginator(queryset, page_size)
    try:
        items = paginator.page(page)
    except:
        items = paginator.page(1)
    return items


def get_current_url(request):
    ''' 获取当前的链接 '''

    host = request.get_host()
    full_path = request.get_full_path()
    return urllib.quote_plus('http://' + host + full_path)


def get_ip_address(request):
    ''' 获取客户端的ip地址 '''

    if request.META.has_key('HTTP_X_FORWARDED_FOR'):
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    return ip
