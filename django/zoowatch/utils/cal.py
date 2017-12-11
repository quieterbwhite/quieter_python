# -*- coding=utf-8 -*-
# Created Time: 2016年01月13日 星期三 13时45分56秒
# File Name: cal.py

'''
计算方面 通用 的方法
'''

def getd(num):
    ''' 获取该数值的两位小数 '''

    #return float('%.2f' % num)
    return float('{:.2f}'.format(num))
