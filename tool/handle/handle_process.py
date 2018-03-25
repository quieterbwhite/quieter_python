# -*- coding=utf-8 -*-
# Created Time: 2015年06月17日 星期三 14时50分55秒
# File Name: handle_process.py


import psutil
import subprocess


def get_pid_info(pid):
    """ 获取进程信息 """

    is_running = False

    try:
        p = psutil.Process(pid)
        status = p.status()

        if status == "running":
            is_running = True

        pname = p.name()
    except:
        pass

    return is_running


def get_pidof_process(process_name):
    """ 获取某个进程的所有 pid """

    cmd = "pidof {}".format(process_name)
    try:
        res = subprocess.check_output(cmd, shell=True)
    except:
        res = None
    if not res: return []
    return [int(i) for i in res.split(" ")]


def new_stitch_process():

    command = "ps aux"
    p = subprocess.Popen(command, shell=True)

    if p.returncode:
        return -1

    return p.pid