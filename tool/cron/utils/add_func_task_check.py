# -*- coding=utf-8 -*-
# Created Time: Sun 26 Feb 2017 11:09:01 PM CST
# File Name: add_func_task_check.py


from consts import TASK_CHECK, HEARTBEAT
from cron.aps_background import scheduler
from cron.funcs.check_task import check_task
import logging

logging.basicConfig()


def add_task_check():
    """ 检查任务状态定时任务 """

    scheduler.add_job(
        check_task,
        'interval',
        seconds=HEARTBEAT,
        id=TASK_CHECK
    )


