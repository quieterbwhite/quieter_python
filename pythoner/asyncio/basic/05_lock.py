# -*- coding=utf-8 -*-

"""
这个例子中我们首先使用acquire加锁，通过call_later方法添加一个0.1秒后释放锁的函数。
"""

import asyncio
import functools

def unlock(lock):
    print('callback releasing lock')
    lock.release()

async def test(locker, lock):
    print('{} waiting for the lock'.format(locker))
    with await lock:
        print('{} acquired lock'.format(locker))
    print('{} released lock'.format(locker))

async def main(loop):
    lock = asyncio.Lock()
    await lock.acquire()
    loop.call_later(0.1, functools.partial(unlock, lock))
    await asyncio.wait([test('l1', lock), test('l2', lock)])

loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.close()

