# -*- coding=utf-8 -*-
# Created Time: 2018年03月07日 星期三 20时10分02秒
# File Name: future.py

"""
有了上面这个概念，我们可以创建一个Future类，
它代表了协程中等待的“未来发生的结果”，
举例来说，在发起网络请求时，socket会在buffer中返回一些数据，
这个获取的动作在异步流程中发生的时间是不确定的，
Future就是用来封装这个未来结果的类，
但当socket在某个时间段监测到可读事件，读取到数据了，
那么他就会把数据写入Future里，并告知Future要执行某些回调动作。
"""

class Future(object):

    def __init__(self):
        self.result = None
        self._callbacks = []

    def add_done_callback(self, fn):
        self._callbacks.append(fn)

    def set_result(self, result):
        self.result = result
        for callback in _callbacks:
            callback(self)
