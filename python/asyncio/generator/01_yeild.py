# -*- coding=utf-8 -*-
# 注意 变成generator的函数，在首次调用的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
def consumer():
    r = 'starter'
    print('lalalalalaal') # 只有第一次会执行(启动生成器), 之后再调用生成器就会从yield处执行
    while True:
        n = yield r # 再次执行时从这里的yield继续执行, 将把produce传入的参数 n 赋给局部变量 n . 下轮循环再次遇到yield就会就将 r 返回给produce函数
        # 所以Python的yield不但可以返回一个值，它还可以接收调用者发出的参数
        print('xxxxxlalalalalaal')  # 由于生成器在启动的时候遇到上面的yield就返回了, 所以第一次不会执行这条语句. 之后每次都会被执行
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'  # 因为yield r 所以这个r会在下一次循环被返回给produce函数 
        a = 'fake 200 OK' # 返回的值与a无关

def produce(c):
    # 启动生成器，代码走到consumer中执行，到yield处，consumer将r的初始值a返回给produce,也就是produce启动生成器后得到的返回值r，启动生成器的send函数的参数无法在生成器中得到
    r = c.send(None)
    print("consumer generator has started r=%s" % r)#此时r得到consumer中yield返回的值a
    print('babababab')
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n) # # 获取生成器consumer中由yield语句返回的下一个值
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()      # 并不会启动生成器, 只是将c变为一个生成器
print('AaAaAaAaAa') # AaAaAaAaAa
produce(c)
# =>
# AaAaAaAaAa
# lalalalalaal
# babababab
# [PRODUCER] Producing 1...
# xxxxxlalalalalaal
# [CONSUMER] Consuming 1...
# [PRODUCER] Consumer return: 200 OK
# [PRODUCER] Producing 2...
# xxxxxlalalalalaal
# [CONSUMER] Consuming 2...
# [PRODUCER] Consumer return: 200 OK
# [PRODUCER] Producing 3...
# xxxxxlalalalalaal
# [CONSUMER] Consuming 3...
# [PRODUCER] Consumer return: 200 OK
# [PRODUCER] Producing 4...
# xxxxxlalalalalaal
# [CONSUMER] Consuming 4...
# [PRODUCER] Consumer return: 200 OK
# [PRODUCER] Producing 5...
# xxxxxlalalalalaal
# [CONSUMER] Consuming 5...
# [PRODUCER] Consumer return: 200 OK
