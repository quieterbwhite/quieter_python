# -*- coding=utf-8 -*-
# Created Time: 2017年08月21日 星期一 22时14分16秒
# File Name: 03_basic_yield.py

"""
在 for 循环执行时，每次循环都会执行 fab 函数内部的代码，执行到 yield b 时，fab 函数就返回一个迭代值，下次迭代时，代码从 yield b 的下一条语句继续执行，而函数的本地变量看起来和上次中断执行前是完全一样的，于是函数继续执行，直到再次遇到 yield。看起来就好像一个函数在正常执行的过程中被 yield 中断了数次，每次中断都会通过 yield 返回当前的迭代值。
"""

def odd():
    n=1
    while True:
        yield n
        n+=2

odd_num = odd()
count = 0

for o in odd_num:
    if count >=5: break
    print(o)
    count +=1
