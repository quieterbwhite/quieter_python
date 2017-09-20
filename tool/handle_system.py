# -*- coding=utf-8 -*-
# Created Time: 2015年06月17日 星期三 14时50分55秒
# File Name: handle_system.py

import getpass

def get_current_user():
    """ 获取当前用户名 """

    return getpass.getuser()