# -*- coding=utf-8 -*-
# Created Time: 2017年08月29日 星期二 22时04分36秒
# File Name: 12_stop_child_thread.py


"""
停止子线程

如果一切正常，那么上面的例子很完美。可是，需要停止程序，直接ctrl+c，会抛出KeyboardInterrupt错误，我们修改一下主循环：

try:
    while True:
        task = rcon.rpop("queue")
        if not task:
            time.sleep(1)
            continue
        asyncio.run_coroutine_threadsafe(do_some_work(int(task)), new_loop)
except KeyboardInterrupt as e:
    print(e)
    new_loop.stop()

可是实际上并不好使，虽然主线程try了KeyboardInterrupt异常，但是子线程并没有退出，
为了解决这个问题，可以设置子线程为守护线程，这样当主线程结束的时候，子线程也随机退出。

new_loop = asyncio.new_event_loop()
t = Thread(target=start_loop, args=(new_loop,))
t.setDaemon(True)    # 设置子线程为守护线程
t.start()

try:
    while True:
        # print('start rpop')
        task = rcon.rpop("queue")
        if not task:
            time.sleep(1)
            continue
        asyncio.run_coroutine_threadsafe(do_some_work(int(task)), new_loop)
except KeyboardInterrupt as e:
    print(e)
    new_loop.stop()
线程停止程序的时候，主线程退出后，子线程也随机退出才了，并且停止了子线程的协程任务。

"""