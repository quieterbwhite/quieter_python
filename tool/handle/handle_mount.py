# -*- coding=utf-8 -*-
# Created Time: 2015年06月17日 星期三 14时50分55秒
# File Name: handle_mount.py


import subprocess


def check_if_disk_mounted(uuid):
    """ 检查可移动磁盘是否挂载 """

    out = subprocess.check_output("ls -l /dev/disk/by-uuid/", shell=True)

    if uuid in out:
        return True
    else:
        return False