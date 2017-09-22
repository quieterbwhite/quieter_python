# -*- coding=utf-8 -*-
# Created Time: 2017年09月22日 星期五 23时32分50秒
# File Name: 07_querys.py

"""

group by:

    select count(*) from t group by age;

    select age, count(age) from t group by age;

    select age, name, count(age) from t group by age, name;


alter:

    # 删除字段
    alter table user_info drop area_id;

    # 注意自己为已有记录添加默认值
    alter table user_info add area_id varchar(10) not null default 'value' comment 'area id'


update:

    # query first before update, reuse where statement from query one.
    select * from user_info where user_id = 1;
    # keep safe
    update user_info set area_id = 1 where user_if = 1;


子查询:

    select * from user_info where user_id=(select user_id from house_info where house_id=2)

子查询 & 联合查询， 优先使用联合查询
子查询是两次查询，将子查询的结果放到临时表再和外层过滤
联合查询，先组合两张表再查询，效率会高些

连接:

    user_info                   house_info

    ui_user_id, name            hi_user_id, house_id
    1           a                  1         1
    2           b                  3         2
    3           c                  4         3

inner join == join:

    from user_info inner join house_info on ui_user_id=hi_user_id;
    交集, 结果:
    user_id = 1, 3

left join:

    左边全部取，右边没有的null

right join:

    右边全部取，左边没有的null

outer join:

    pass


truncate:

    truncate table xxx

drop:

    drop database xxx

    drop table xxx








