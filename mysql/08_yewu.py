# -*- coding=utf-8 -*-
# Created Time: 2017年09月25日 星期一 15时39分57秒
# File Name: 08_yewu.py

"""
mysql 实际业务相关查询
"""

"""
** 带查询条件的分页查询

    由于数据量非常大，怎样才能提高翻页性能？

    每次查询从page页开始，多查询需要缓存的页面数据，
    对结果进行分片，形成每页的数据json,
    并将每页数据存放到redis中，使用hash类型，
    在redis中存放的数据结构是:

        key:    hl_startDate_endData_areaId_sortKey
        value:  页码，该页的json数据

    在查询时，先查询redis，根据键和页码获取特定页码的页面数据

    总页数也存放进去



"""
