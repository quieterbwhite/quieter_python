# -*- coding=utf-8 -*-

import requests
import random
from logs.mylog import flogger


def get_proxy():

    try:
        res = requests.get("http://120.79.139.89:8001/proxy/send?pwd=tiger")
        data = res.json()
    except Exception as e:
        return ""

    return data


def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))

# your spider code

def getHtml():
    # ....
    retry_count = 5
    proxy = get_proxy()
    while retry_count > 0:
        try:
            html = requests.get('https://www.example.com', proxies={"http": "http://{}".format(proxy)})
            # 使用代理访问
            return html
        except Exception:
            retry_count -= 1
    # 出错5次, 删除代理池中代理
    delete_proxy(proxy)
    return None