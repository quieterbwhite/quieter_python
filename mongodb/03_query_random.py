# -*- coding=utf-8 -*-
# Created Time: 2016年08月05日 星期五 09时45分58秒
# File Name: 03_query_random.py

'''
mongodb 随机查询
'''

'''
方法一:

    mongodb 官方支持随机查询，在 >= 3.2 版本的数据库中

    ref:
    1. https://docs.mongodb.com/manual/reference/operator/aggregation/sample/
    2. https://www.mongodb.com/blog/post/how-to-perform-random-queries-on-mongodb

    适用方法:
        db.users.aggregate(
            [{$sample:{size:3}}]
        )


方法二:

    适用于版本低于3.2的数据库, 且数据量小于 100k

    ref: http://www.cnblog.com/tr0217/p/4731486.html

    skip 过随机数量的记录

    skip 过量的集合数会性能低

'''
