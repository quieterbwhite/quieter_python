# -*- coding=utf-8 -*-
# Created Time: 2017年12月21日 星期四 11时27分26秒
# File Name: app.py

from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    count = redis.incr('hits')
    return 'Hello World! hits: {}'.format(count)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
