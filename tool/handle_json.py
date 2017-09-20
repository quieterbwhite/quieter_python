# -*- coding=utf-8 -*-
# Created Time: 2015年06月17日 星期三 14时50分55秒
# File Name: handle_json.py


import json


def dumps_ident(data, indent=4, separators=(',', ':')):
    """ 格式化输出json """

    return json.dumps(data, indent=indent, separators=separators)