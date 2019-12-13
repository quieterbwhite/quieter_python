# -*- coding=utf-8 -*-
# Created Time: 2018年03月08日 星期四 17时32分37秒
# File Name: task.py

"""
这里关键的地方就是future在yield之后会在未来某个时候再次被send然后继续往下走，
这时候就需要一个用来驱动Future的类。这里称为Task，它需要接受一个协程作为参数，并驱动协程的程序流执行。
"""

from future import Future

class Task(Future):

    def __init__(self, coro):
        super().__init__()
        self.coro = coro
        f = Future()
        f.set_result(None)
        self.step(f)

    def step(self, future):
        try:
            next_future = self.coro.send(future.result)
            if next_future is None:
                return
        except StopIteration as exc:
            self.set_result(exc.value)
            return

        next_future.add_done_callback(self.step)