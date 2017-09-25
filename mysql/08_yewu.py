# -*- coding=utf-8 -*-
# Created Time: 2017年09月25日 星期一 15时39分57秒
# File Name: 08_yewu.py

"""
mysql 实际业务相关查询
"""

"""
** 带查询条件的分页查询

    由于数据量非常大，怎样才能提高翻页性能？

    方案一:

        每次查询从page页开始，多查询需要缓存的页面数据，
        对结果进行分片，形成每页的数据json,
        并将每页数据存放到redis中，使用hash类型，
        在redis中存放的数据结构是:

            key:    hl_startDate_endData_areaId_sortKey
            value:  页码，该页的json数据

        在查询时，先查询redis，根据键和页码获取特定页码的页面数据

        总页数也存放进去

    方案二:

        结果集根据编号进行过滤，就可以不用缓存又达到极高的性能

        问题是怎么来的编号，某些数据库直接支持，mysql没有，需要自己实现，如下:

        这条语句是从最里往外一层一层加出来的～
        select * from (select @rownum:=@rownum+1 as rownum, b.* from (select @rownum:=0)
        a, (select distinct hi_house_id, hi_title, hi_price from ih_house_info order by
        hi_price desc) b) t where rownum between 3 and 5;
                                         > 10 limit 5;



"""
