# -*- coding=utf-8 -*-
# Created Time: 2015年06月17日 星期三 14时47分00秒
# File Name: pages.py

'''
django 分页处理
'''

from django.core.paginator import Paginator, EmptyPage, InvalidPage

def pages(queryset, page=1, perPage=20):
    ''' 分页函数
    queryset  queryset:   查询结果
    int       page    :   第几页
    int       perPage :   每页多少条数据
    '''

    paginator = Paginator(queryset, perPage)
    try:
        items = paginator.page(page)
    except (EmptyPage, InvalidPage):
        items = paginator.page(paginator.num_pages)
    return items


