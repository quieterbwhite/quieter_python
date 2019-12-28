# -*- coding=utf-8 -*-
# Created Time: 2015年08月08日 星期六 12时14分51秒
# File Name: lib_time.py

import datetime, time

'''
#将"2011-09-28 10:00:00"转化为时间戳
time.mktime(time.strptime(a,'%Y-%m-%d %H:%M:%S'))
>>1317091800.0

#将时间戳转化为localtime
x = time.localtime(1317091800.0)
time.strftime('%Y-%m-%d %H:%M:%S',x)
'''


def dt_str_now(show='str', layout='%Y-%m-%d %H:%M:%S'):
    ''' 获取当前时间 的 datetime 或 str '''

    if show == 'dt': return datetime.datetime.now()
    try:
        return datetime2str(datetime.datetime.now(), layout)
    except:
        return ''


def clean_time(s='', e='', days_range=7):
    ''' 时间格式化处理, 处理客户端时间查询请求

        将两个标准的字符串格式时间处理为 python datetime 类型
        '2014-12-12' -> XXOO
        如果没有传入 s or e
        那么, 默认开始时间 days_range 天之前的时间
              默认结束时间 今天
              默认时间间隔 days_range
    '''

    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)

    ee = tomorrow
    ss = ee - datetime.timedelta(days_range)

    if s and e:
        ss = str2datetime(s, '%Y-%m-%d')
        ee = str2datetime(e, '%Y-%m-%d')+datetime.timedelta(1)
    if s and not e:
        ss = str2datetime(s, '%Y-%m-%d')
        ee = datetime.datetime.strptime(str(tomorrow), '%Y-%m-%d')
    if e and not s:
        ee = str2datetime(e, '%Y-%m-%d')+datetime.timedelta(1)
        ss = ee - datetime.timedelta(days_range)

    #print 'datetime ss: ', ss
    #print 'datetime ee: ', ee
    return ss, ee


def week_day_now():
    ''' 返回今天星期几 '''

    return datetime.datetime.now().weekday()


def get_days_later(days=1, format_type='datetime',
                set_format="%Y-%m-%d %H:%M:%S", sign='+'):
    ''' 获取相差几天的时间

    可以指定返回的该天的时间格式
        默认 datetime , 可以 str
    '''

    now_datetime = datetime.datetime.now()

    if sign == '+':
        days_datetime = (now_datetime + datetime.timedelta(days=days))
    else:
        days_datetime = (now_datetime - datetime.timedelta(days=days))

    if format_type == 'str':
        days_str = datetime2str(days_datetime, set_format=set_format)
        return days_str
    return days_datetime


def get_hours_later(hours=1, set_format="%Y-%m-%d %H:%M:%S", sign='+'):
    ''' 获取相差几天的时间

    可以指定返回的该天的时间格式
        默认 datetime , 可以 str
    '''

    now_datetime = datetime.datetime.now()

    if sign == '+':
        days_datetime = (now_datetime + datetime.timedelta(hours=hours))
    else:
        days_datetime = (now_datetime - datetime.timedelta(hours=hours))

    days_str = datetime2str(days_datetime, set_format=set_format)

    return days_datetime, days_str


def datetime2str(d, set_format='%Y-%m-%d %H:%M:%S'):
    ''' datetime 转换为指定格式的字符串 '''

    try:
        return datetime.datetime.strftime(d, set_format)
    except:
        return ''


def str2datetime(d, set_format='%Y-%m-%d %H:%M:%S'):
    ''' 指定格式的字符串转换为 datetime '''

    return datetime.datetime.strptime(d, set_format)


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

    #print 'timestamp_over_today: ', timestamp_over_today
    return timestamp_over_today


def age():
    ''' 输入出生年月日得出年龄 '''

    print "Enter Your Date of Birth"
    d=input("Day:")
    m=input("Month:")
    y=input("Year:")
    #get the current time in tuple format
    a=gmtime()
    #difference in day
    dd=a[2]-d
    #difference in month
    dm=a[1]-m
    #difference in year
    dy=a[0]-y
    #checks if difference in day is negative
    if dd<0:
        dd=dd+30
        dm=dm-1
        #checks if difference in month is negative when difference in day is also negative
        if dm<0:
            dm=dm+12
            dy=dy-1
    #checks if difference in month is negative when difference in day is positive
    if dm<0:
        dm=dm+12
        dy=dy-1
    print "Your current age is %s Years %s Months & %s Days"%(dy,dm,dd)


def get_expire_time():
    ''' 积分过期时间

        添加注释，尼玛， 我自己都看不懂是写的什么了。
    '''

    now = datetime.datetime.now()
    year = now.strftime('%Y')
    t = datetime.datetime(int(year), 6, 30)
    if now > t: t = datetime.datetime(int(year) + 1, 6, 30)
    return t


def dict_list_val_to_list(data_list, key):
    ''' 将字典列表的值格式化为列表

    如: [{'initial': 'N'}, {'initial': 'A'}] -> ['A', 'N']
    '''

    data_list = [d.get(key,'') for d in data_list]
    print 'data_list: ', data_list
    return data_list


def main():

    #get_timestamp_of_today()
    #clean_time(s='', e='2015-10-18', days_range=7)
    a, b = get_hours_later(hours=5)
    print 'a: ', a
    print 'b: ', b

if __name__ == '__main__':

    main()


