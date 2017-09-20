# -*- coding=utf-8 -*-
# Created Time: Wed 14 Jan 2015 08:48:57 PM CST
# File Name: add_task.py

import time
import traceback
import random

from task import exe_task

def action():

    tries = 0

    while 1:
        try:
            tries += 1
            if tries >= 20:
                break

            task_id = tries
            number = random.randint(1, 5)

            exe_task.apply_async(args=[task_id, number], queue='sms_q')
            print 'added one task'
            time.sleep(1)
        except:
            traceback.print_exc()
            pass

    print 'add task done'

def main():

    action()

if __name__ == '__main__':

    main()