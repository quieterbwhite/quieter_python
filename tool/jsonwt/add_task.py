# -*- coding=utf-8 -*-
# Created Time: Wed 14 Jan 2015 08:48:57 PM CST
# File Name: add_task.py

import traceback

from task import exe_task

def add_task_to_queue(mobile, content):

    try:
        exe_task.apply_async(args=[mobile, content], queue='sms_q')
    except:
        traceback.print_exc()

    print 'added one task: ', mobile

def main():

    mobile = '15202897835'
    content = 'tiger'
    add_task_to_queue(mobile, content)

if __name__ == '__main__':

    main()
