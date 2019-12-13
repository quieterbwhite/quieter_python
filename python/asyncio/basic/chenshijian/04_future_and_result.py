# -*- coding=utf-8 -*-
# Created Time: 2017年08月29日 星期二 21时13分33秒
# File Name: 04_future_and_result.py


"""
future 与 result

回调一直是很多异步编程的恶梦，程序员更喜欢使用同步的编写方式写异步代码，以避免回调的恶梦。
回调中我们使用了future对象的result方法。前面不绑定回调的例子中，我们可以看到task有fiinished状态。
在那个时候，可以直接读取task的result方法。
"""

import time
import asyncio

async def do_some_work(x):
    print('Waiting {}'.format(x))
    return 'Done after {}s'.format(x)

now = lambda : time.time()

start = now()

coroutine = do_some_work(2)
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(coroutine)
loop.run_until_complete(task)

print('Task ret: {}'.format(task.result()))
print('TIME: {}'.format(now() - start))

"""
output:

Waiting:  2
Task ret:  Done after 2s
TIME:  0.0003650188446044922

"""

