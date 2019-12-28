# -*- coding=utf-8 -*-
# Created Time: 2017年08月29日 星期二 21时10分19秒
# File Name: 03_def_a_callback.py

"""
绑定回调

绑定回调，在task执行完毕的时候可以获取执行的结果，回调的最后一个参数是future对象，通过该对象可以获取协程返回值。
如果回调需要多个参数，可以通过偏函数导入。
"""

import time
import asyncio

now = lambda : time.time()

async def do_some_work(x):
    print('Waiting: ', x)
    return 'Done after {}s'.format(x)

def callback(future):
    print('Callback: ', future.result())

start = now()

coroutine = do_some_work(2)
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(coroutine)
task.add_done_callback(callback)
loop.run_until_complete(task)

print('TIME: ', now() - start)

"""
output:

Waiting:  2
Callback:  Done after 2s
TIME:  0.0003807544708251953
"""


"""
def callback(t, future):
    print('Callback:', t, future.result())

task.add_done_callback(functools.partial(callback, 2))
可以看到，coroutine执行结束时候会调用回调函数。并通过参数future获取协程执行的结果。我们创建的task和回调里的future对象，实际上是同一个对象。
"""