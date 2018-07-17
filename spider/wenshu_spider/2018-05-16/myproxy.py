# -*- coding=utf-8 -*-

import requests
import random
from logs.mylog import flogger


def get_proxy():

    res = requests.get("http://127.0.0.1:8000/?types=0&count=50&protocol=0")
    data = res.json()
    len_data = len(data)
    if len_data > 0:
        index = random.randint(0, len(data))
        ip = data[index][0]
        port = data[index][1]
    else:
        flogger.info("### Run out of proxy ip:port")
        return ""

    return {"http": "http://{}:{}".format(ip, port)}


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