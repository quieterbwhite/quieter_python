# -*- coding=utf-8 -*-
# Created Time: 2017年08月29日 星期二 22时07分21秒
# File Name: server.py


"""
在消费队列的时候，我们使用asyncio的sleep用于模拟耗时的io操作。
以前有一个短信服务，需要在协程中请求远程的短信api，此时需要是需要使用aiohttp进行异步的http请求。大致代码如下：

/接口表示短信接口，/error表示请求/失败之后的报警。
"""

import time
from flask import Flask, request

app = Flask(__name__)

@app.route('/<int:x>')
def index(x):
    time.sleep(x)
    return "{} It works".format(x)

@app.route('/error')
def error():
    time.sleep(3)
    return "error!"

if __name__ == '__main__':
    app.run(debug=True)

