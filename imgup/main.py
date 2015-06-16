# -*- coding=utf-8 -*-
# Created Time: Tue 16 Jun 2015 11:01:46 PM CST
# File Name: main.py

'''
服务端程序
从客户端接收图片文件并保存，可选择缩略图等参数
'''

from config import PATH, PATH_THUM, NEW_WIDTH, THUM_FORMAT
from PIL import Image
import uuid
import os


def process(f, thum=False):
    ''' 保存上传的文件

        f: 获取的文件
        thum: 是否生成缩略图
    '''

    img = Image.open(f)

    name = str(uuid.uuid4())
    pic = name + '.png'
    file_name = os.path.join(PATH, pic)
    img.save(file_name)

    if not thum:
        return pic

    pic_thum = name + '-thum.png'
    file_name_thum = os.path.join(PATH_THUM, pic_thum)

    original_size = img.size # PIL的size属性结构：(width, height)
    new_width = NEW_WIDTH
    new_height = new_width * (float(original_size[1]) / float(original_size[0]))
    size = new_width, new_height
    img.thumbnail(size, Image.ANTIALIAS)
    img.save(file_name_thum, THUM_FORMAT)

    return pic, pic_thum


