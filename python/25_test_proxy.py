# -*- coding=utf-8 -*-
# Created Time: 2018年09月17日 星期一 10时24分59秒
# File Name: 25_test_proxy.py

import requests

proxies = {"http": "http://10.2.4.15:8899"}

res = requests.get("http://www.baidu.com")
print(res.status_code)

res = requests.get("http://www.baidu.com", proxies=proxies)

print(res.text)
