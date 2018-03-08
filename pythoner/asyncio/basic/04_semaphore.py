# -*- coding=utf-8 -*-

import aiohttp
import asyncio

"""
比如我现在要抓取http://httpbin.org/get?a=X这样的页面，X为1-10000的数字，
一次性的产生1w次请求显然很快就会被封掉。
那么我们可以用Semaphore控制同时的并发量(例子中为了演示，X为0-11)：

在运行的时候可以感受到并发受到了信号量的限制，基本保持在同时处理三个请求的标准。
"""

NUMBERS = range(12)
URL = 'http://httpbin.org/get?a={}'
sema = asyncio.Semaphore(3)

async def fetch_async(a):
    async with aiohttp.request('GET', URL.format(a)) as r:
        data = await r.json()
    return data['args']['a']

async def print_result(a):
    with (await sema):
        r = await fetch_async(a)
        print('fetch({}) = {}'.format(a, r))

loop = asyncio.get_event_loop()
f = asyncio.wait([print_result(num) for num in NUMBERS])
loop.run_until_complete(f)
