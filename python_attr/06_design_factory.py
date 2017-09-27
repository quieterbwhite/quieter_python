# -*- coding=utf-8 -*-
# Created Time: 2017年09月26日 星期二 09时58分17秒
# File Name: 06_design_factory.py

"""
python 工厂模式

输入不同的format, 会通过getattr调用statsout的不同函数，实现不同功能
"""

import statsout

def output(data, format="text"):

    output_function = getattr(statsout, "output_%s" %format)

    return output_function(data)
