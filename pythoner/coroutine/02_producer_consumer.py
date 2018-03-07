# -*- coding=utf-8 -*-
# Created Time: 2018年03月07日 星期三 18时55分09秒
# File Name: 02_producer_consumer.py

"""
https://zhuanlan.zhihu.com/p/25228075

生产者－消费者的协程
"""

def consumer():

    status = True
    while True:
        n = yield status
        print("I got {}".format(n))
        if n == 3:
            status = False

def producer(consumer):

    n = 5
    while n > 0:
        # yield 给主程序返回消费者的状态
        yield consumer.send(n)
        n -= 1

if __name__ == "__main__":
    c = consumer()
    c.send(None)
    p = producer(c)
    for status in p:
        if status == False:
            print("3, 4, 5 is good enough!");
            break

    print("Done")

