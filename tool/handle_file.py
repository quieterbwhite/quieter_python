# -*- coding=utf-8 -*-
# Created Time: 2015年06月17日 星期三 14时50分55秒
# File Name: handle_file.py

import shutil
import os


class FileService(object):

    @classmethod
    def file_copy(cls, src, dst):
        try:
            shutil.copy(src, dst)
        except:
            pass

    @classmethod
    def folder_content_copy(cls, src, dst):
        """ 拷贝文件夹内容 """

        cmd = "cp -r {}* {}".format(src, dst)
        os.system(cmd)

    @classmethod
    def content_append(cls, src, content):

        with open(src, 'a+') as myfile:
            myfile.write(content)

    @classmethod
    def get_file_size(cls, path):
        """ 获取文件大小 """

        size = 0
        try:
            size = os.path.getsize(path)
        except:
            pass

        return size
