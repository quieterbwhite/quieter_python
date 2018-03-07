# -*- coding=utf-8 -*-
# Created Time: 2018年03月07日 星期三 18时51分11秒
# File Name: 01_fib.py

def fib(max):
    """ 那么我每一次调用函数时，都要耗费大量时间循环做重复的事情 """

    n, a, b = 0, 0, 1

    while n <= max:
        print b
        a, b = b, a+b
        n = n+1

def fib_yield(max):
    """ 使用yield的话，它则会生成一个generator，
        当我需要时，调用它的next方法获得下一个值，
        改动的方法很简单，直接把print改为yield就OK
    """

    n, a, b = 0, 0, 1

    while n <= max:
        yield b
        a, b = b, a+b
        n = n+1
