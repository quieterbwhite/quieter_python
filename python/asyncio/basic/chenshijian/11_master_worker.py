# -*- coding=utf-8 -*-
# Created Time: 2017年08月29日 星期二 22时02分12秒
# File Name: 11_master_worker.py


"""
master-worker主从模式

对于并发任务，通常是用生成消费模型，对队列的处理可以使用类似master-worker的方式，master主要用户获取队列的msg，worker用户处理消息。

为了简单起见，并且协程更适合单线程的方式，我们的主线程用来监听队列，子线程用于处理队列。这里使用redis的队列。主线程中有一个是无限循环，用户消费队列。

    while True:
        task = rcon.rpop("queue")
        if not task:
            time.sleep(1)
            continue
        asyncio.run_coroutine_threadsafe(do_some_work(int(task)), new_loop)

给队列添加一些数据：

127.0.0.1:6379[3]> lpush queue 2
(integer) 1
127.0.0.1:6379[3]> lpush queue 5
(integer) 1
127.0.0.1:6379[3]> lpush queue 1
(integer) 1
127.0.0.1:6379[3]> lpush queue 1
可以看见输出：

Waiting  2
Done 2
Waiting  5
Waiting  1
Done 1
Waiting  1
Done 1
Done 5

我们发起了一个耗时5s的操作，然后又发起了连个1s的操作，可以看见子线程并发的执行了这几个任务，其中5s awati的时候，相继执行了1s的两个任务。
"""