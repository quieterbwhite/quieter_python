# -*- coding=utf-8 -*-
# Created Time: 2017年08月29日 星期二 22时08分34秒
# File Name: async-custoimer.py


"""
有一个问题需要注意，我们在fetch的时候try了异常，如果没有try这个异常，即使发生了异常，子线程的事件循环也不会退出。
主线程也不会退出，暂时没找到办法可以把子线程的异常raise传播到主线程。（如果谁找到了比较好的方式，希望可以带带我）。

对于redis的消费，还有一个block的方法：

try:
    while True:
        _, task = rcon.brpop("queue")
        asyncio.run_coroutine_threadsafe(do_some_work(int(task)), new_loop)
except Exception as e:
    print('error', e)
    new_loop.stop()
finally:
    pass
    
使用 brpop方法，会block住task，如果主线程有消息，才会消费。测试了一下，似乎brpop的方式更适合这种队列消费的模型。

"""

import time
import asyncio
from threading import Thread
import redis
import aiohttp

def get_redis():
    connection_pool = redis.ConnectionPool(host='127.0.0.1', db=3)
    return redis.Redis(connection_pool=connection_pool)

rcon = get_redis()

def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print(resp.status)
            return await resp.text()

async def do_some_work(x):
    print('Waiting ', x)
    try:
        ret = await fetch(url='http://127.0.0.1:5000/{}'.format(x))
        print(ret)
    except Exception as e:
        try:
            print(await fetch(url='http://127.0.0.1:5000/error'))
        except Exception as e:
            print(e)
    else:
        print('Done {}'.format(x))

new_loop = asyncio.new_event_loop()
t = Thread(target=start_loop, args=(new_loop,))
t.setDaemon(True)
t.start()

try:
    while True:
        task = rcon.rpop("queue")
        if not task:
            time.sleep(1)
            continue
        asyncio.run_coroutine_threadsafe(do_some_work(int(task)), new_loop)
except Exception as e:
    print('error')
    new_loop.stop()
finally:
    pass
