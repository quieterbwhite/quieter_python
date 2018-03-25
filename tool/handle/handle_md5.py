# -*- coding=utf-8 -*-
# Created Time: 2015年06月17日 星期三 14时50分55秒
# File Name: handle_md5.py

import hashlib
import types


def md5(content):
    """ 字符串内容的md5 """

    if type(content) is types.StringType:
        m = hashlib.md5()
        m.update(content)
        return m.hexdigest()
    else:
        return ''


def md5_file(file_path):
    """ 全部文件内容的md5 """

    md5 = ''

    try:
        f = open(file_path,'rb')
        md5_obj = hashlib.md5()
        while True:
            d = f.read(8096)
            if not d:
                break
            md5_obj.update(d)
        hash_code = md5_obj.hexdigest()
        f.close()
        md5 = str(hash_code).lower()
    except Exception, e:
        print e

    return md5