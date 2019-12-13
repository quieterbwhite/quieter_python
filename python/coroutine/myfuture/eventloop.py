# -*- coding=utf-8 -*-
# Created Time: 2018年03月08日 星期四 17时43分19秒
# File Name: eventloop.py

"""
最终，整个程序还需要一个EventLoop类，
用来监听到来的事件为socket执行回调以及把协程包装成Task来实现异步驱动。
"""

class EventLoop(object):

    stopped = False
    select_timeout = 5

    def run_until_complete(self, coros):
        tasks = [Task(coro) for coro in coros]
        try:
            self.run_forever()
        except StopError:
            pass

    def run_forever(self):
        while not self.stopped:
            events = selector.select(self.select_timeout)
            if not events:
                raise SelectTimeout("轮训超时")

            for event_key, event_mask in events:
                callback = event_key.data
                callback(event_key, event_mask)

    def close(self):
        self.stopped = True
