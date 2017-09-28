# -*- coding=utf-8 -*-
# Created Time: 2016年08月30日 星期二 16时05分45秒
# File Name: lib_re.py

"""
用到的各种正则
"""

import re


def regex_char_trans(val):
    """ 正则匹配的时候将正则特殊字符转义 """

    reg_list = ['\\', '+', '*', '?', '[', '^', ']', '$',
            '(', ')', '{', '}', '=', '!', '<', '>', '|', ':', '-'
        ]

    for i in reg_list:
        if i in val:
            val = val.replace(i, '\\'+i)

    val = val.replace('.', '\\.')
    return val


def between_quota(val):
    """ 提取字符串中 双引号 之间的值 """

    pattern = re.compile('"(.*)"')

    value = pattern.findall(val)

    return value

def between_underline_dollar(val):
    """ 下划线和美元符号 之间的值 """

    # 要匹配的是变量名，长度在 1-15 之间
    pattern = re.compile('\$(.{1,15})_')

    value = pattern.findall(val)

    return value

def format_add_0(val):

    return '%08d' % int(val)

def high2max(high):
    """ 处理版本号为可比较大小的字符串

        max_str 应该是一个16位的字符串
    """

    max_str = ''

    try:
        foo = high.split('.')
        for f in foo:
            max_str += format_add_0(f)
    except:
        pass

    return max_str