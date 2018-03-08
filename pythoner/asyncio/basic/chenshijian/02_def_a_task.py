# -*- coding=utf-8 -*-
# Created Time: 2017年08月29日 星期二 21时05分10秒
# File Name: 02_def_a_task.py

"""
创建一个task

协程对象不能直接运行，在注册事件循环的时候，其实是run_until_complete方法将协程包装成为了一个任务（task）对象。
所谓task对象是Future类的子类。保存了协程运行后的状态，用于未来获取协程的结果。
"""


import asyncio
import time

now = lambda : time.time()

async def do_some_work(x):
    print('Waiting: ', x)

start = now()

coroutine = do_some_work(2)
loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(coroutine)
task = loop.create_task(coroutine)
print(task)
loop.run_until_complete(task)
print(task)
print('TIME: ', now() - start)

"""
<Task pending coro=<do_some_work() running at /Users/ghost/Rsj217/python3.6/async/async-main.py:17>>
Waiting:  2
<Task finished coro=<do_some_work() done, defined at /Users/ghost/Rsj217/python3.6/async/async-main.py:17> result=None>
TIME:  0.0003490447998046875
"""

"""
创建task后，task在加入事件循环之前是pending状态，因为do_some_work中没有耗时的阻塞操作，task很快就执行完毕了。后面打印的finished状态。

asyncio.ensure_future(coroutine) 和 loop.create_task(coroutine)都可以创建一个task，run_until_complete的参数是一个futrue对象。
当传入一个协程，其内部会自动封装成task，task是Future的子类。isinstance(task, asyncio.Future)将会输出True。
"""