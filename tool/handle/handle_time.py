# -*- coding=utf-8 -*-
# Created Time: 2015年06月17日 星期三 14时50分55秒
# File Name: handletime.py

'''
各种时间相关处理
'''

import datetime
import time


def get_timestamp():

    return int(time.time())

def dt_str_now(show='str', layout='%Y-%m-%d %H:%M:%S'):
    ''' 获取当前时间 的 datetime 或 str '''

    if show == 'dt':
        return datetime.datetime.now()
    return datetime2str(datetime.datetime.now(), layout)


def datetime2str(d, set_format='%Y-%m-%d %H:%M:%S'):
    ''' datetime 转换为指定格式的字符串 '''

    return datetime.datetime.strftime(d, set_format)


def datetime_to_str(d):

    return datetime.datetime.strftime(d, '%Y-%m-%d %H:%M:%S')

def str_to_datetime(d):
    ''' d: '2010-10-10' '''

    return datetime.datetime.strptime(d, '%Y-%m-%d %H:%M:%S')

def get_timestamp_of_today():
    ''' 获取今天过了多少秒

        是我自己一步一步构造的，不知道有没有高级的方法
    '''

    # 今天的日期
    today_str = str(datetime.date.today())
    # 今天0点时的时间戳
    today_0_timestamp = int(time.mktime(time.strptime(today_str,'%Y-%m-%d')))

    # 当前的时间戳减去0点的时间戳 就是今天过去的秒数
    timestamp_over_today = int(time.time()) - today_0_timestamp

    print 'timestamp_over_today: ', timestamp_over_today
    return timestamp_over_today


def week_day_now():
    ''' 返回今天星期几 '''

    return datetime.datetime.now().weekday()


def get_days_later(days=1, format_type='datetime',
                set_format="%Y-%m-%d %H:%M:%S"):
    ''' 获取几天后的时间

    可以指定返回的该天的时间格式
        默认 datetime , 可以 str
    '''

    now_datetime = datetime.datetime.now()
    days_datetime = (now_datetime + datetime.timedelta(days=days))
    if format_type == 'str':
        days_str = datetime2str(days_datetime, set_format=set_format)
        return days_str
    return days_datetime