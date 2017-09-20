# -*- coding=utf-8 -*-
# Created Time: Fri 16 Jan 2015 03:36:27 PM CST
# File Name: ce_config.py

from celery import Celery

'''
task_sms: 是任务的名称
broker: 通过 amqp://用户名：密码＠ip／虚拟主机连接 amqp
include: 任务程序
'''
app = Celery('task_sms',
            broker='amqp://bwhite:tiger@192.168.2.34/sms',
            include=['task']
        )

# TODO 将某些值当做常量提取出来

'''
指定任务存储队列
'''
app.conf.update(
            CELERY_ROUTES = {
                'task_sms.task.add':{'queue':'sms_q'},
            },
            CELERY_TASK_RESULT_EXPIRES = 3600,
        )

if __name__ == '__main__':
    app.start()
