# -*- coding=utf-8 -*-
# Created Time: 2015年06月17日 星期三 14时50分55秒
# File Name: handletime.py

'''
各种时间相关处理
'''

import datetime


def datetime_to_str(d):

    return datetime.datetime.strftime(d, '%Y-%m-%d %H:%M:%S')

def str_to_datetime(d):
    ''' d: '2010-10-10' '''

    return datetime.datetime.strptime(d, '%Y-%m-%d %H:%M:%S')
