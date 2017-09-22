# -*- coding=utf-8 -*-
# Created Time: 2017年09月22日 星期五 23时32分50秒
# File Name: 07_querys.py

"""

group by:

    select count(*) from t group by age;

    select age, count(age) from t group by age;

    select age, name count(age) from t group by age, name;


alter:

    # 删除字段
    alter table user_info drop area_id;

    # 注意自己为已有记录添加默认值
    alter table user_info add area_id varchar(10) not null default 'value' comment 'area id'


"""
