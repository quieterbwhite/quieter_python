# -*- coding=utf-8 -*-

import requests
import random

def get_proxy():
    seq = random.randint(0, 20)
    res = requests.get("http://127.0.0.1:8000/?types=0&count=50&protocol=0")
    data = res.json()

    try:
        ip = data[seq][0]
        port = data[seq][1]
    except:
        ip = "127.0.0.1"
        port = "8888"

    return ip+":"+str(port)

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