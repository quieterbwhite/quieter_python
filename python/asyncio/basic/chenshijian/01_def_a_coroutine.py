import time
import asyncio

now = lambda : time.time()

# 通过async关键字定义一个协程（coroutine），协程也是一种对象。
async def do_some_work(x):
    print('Waiting: ', x)

start = now()

# 协程不能直接运行，需要把协程加入到事件循环（loop），由后者在适当的时候调用协程。
coroutine = do_some_work(2)

# 方法可以创建一个事件循环，然后使用run_until_complete将协程注册到事件循环，并启动事件循环。
loop = asyncio.get_event_loop()
loop.run_until_complete(coroutine)

print('TIME: ', now() - start)

"""
因为本例只有一个协程，于是可以看见如下输出：

Waiting:  2
TIME:  0.0004658699035644531
"""