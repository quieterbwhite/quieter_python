# -*- coding=utf-8 -*-
# Created Time: Tue 16 Sep 2014 10:08:30 PM CST

'''
任务脚本
'''

import time
import traceback

from ce_config import app


@app.task
def exe_task(task_id, number):
    ''' 根据参数执行任务 '''

    try:
        print 'exe task: ', task_id
        time.sleep(number)
    except:
        traceback.print_exc()
        return (task_id, number, -1)

    return (task_id, number, 1)

def main():
    res = exe_task(2, 2)
    print 'res: ', res

if __name__ == '__main__':
    main()