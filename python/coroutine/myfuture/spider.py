# -*- coding=utf-8 -*-
# Created Time: 2018年03月08日 星期四 17时58分17秒
# File Name: spider.py

from time import time

def fetch(url):
    request = AsyncRequest('www.baidu.com', url, 80)
    data = yield from request.process()
    return data

def get_page(url):
    page = yield from fetch(url)
    return page

def get_test():

    a = yield from range(1, 3)
    return a

def async_way():
    ev_loop = get_event_loop()
    ev_loop.run_until_complete([
        # get_page('/s?wd={}'.format(i)) for i in range(100)
        get_page('/s?wd=1')
    ])

start = time()

# async_way() # Cost 3.534296989440918 seconds

end = time()

print ('Cost {} seconds'.format(end - start))

if __name__ == '__main__':

    alist = [get_test()]

    for i in alist:
        print(i)