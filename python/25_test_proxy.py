# -*- coding=utf-8 -*-
# Created Time: 2018年09月17日 星期一 10时24分59秒
# File Name: 25_test_proxy.py

"""
阿布云动态代理
"""

import requests

class AbuProxyService:

    # 代理服务器
    proxyHost = "http-dyn.abuyun.com"
    proxyPort = "9020"

    # 代理隧道验证信息
    proxyUser = "H377J1240V4082HD"
    proxyPass = "62AC9DD2CE4401BC"

    http = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
        "host" : proxyHost,
        "port" : proxyPort,
        "user" : proxyUser,
        "pass" : proxyPass
    }

    proxyMeta = {"http": http}

def main():

    print(AbuProxyService.proxyMeta)

    url = "http://www.baidu.com"
    proxies = AbuProxyService.proxyMeta

    res = requests.get(url, proxies=proxies, timeout=2)
    print(res.text)

if __name__ == "__main__":
    main()
