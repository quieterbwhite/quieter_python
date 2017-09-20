# -*- coding=utf-8 -*-
# Created Time: Tue 16 Jun 2015 11:03:51 PM CST
# File Name: config.py

'''
保存图片相关参数，常量
'''

import os

def parent_dir(path, n):
    o = '/../'
    for i in range(n):o += '../'
    return os.path.abspath(path + o)

# 项目根目录绝对地址
BASE_DIR = parent_dir(__file__, 2)

NEW_WIDTH = 600

THUM_FORMAT = 'png'

def main():

    print 'base dir: ', BASE_DIR

if __name__ == '__main__': main()
