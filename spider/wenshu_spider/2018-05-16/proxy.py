# -*-encoding:utf-8-*-

"""
获取代理ip
"""

import requests
from logs.mylog import flogger


proxy_list = []


def process():

    if proxy_list:
        flogger.info("提取一个本地代理")
        return proxy_list.pop()

    flogger.info("从芝麻代理获取一批代理..")
    try:
        # res = requests.get("http://webapi.http.zhimacangku.com/getip?num=20&type=2&pro=0&city=0&yys=0&port=1&pack=24397&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=2&regions=", timeout=10)
        res = requests.get("http://webapi.http.zhimacangku.com/getip?num=20&type=2&pro=0&city=0&yys=0&port=1&pack=24397&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=", timeout=10)
    except Exception as e:
        return ""

    if res:
        data = res.json()
        if data["code"] != 0:
            return ""

        for d in data["data"]:
            proxy_list.append({"http" : "http://" + d["ip"] + ":" + str(d["port"])})

    flogger.info(proxy_list)
    return proxy_list.pop()


def get_xdaili():

    if proxy_list:
        return proxy_list.pop()

    res = requests.get("http://api.xdaili.cn/xdaili-api//greatRecharge/getGreatIp?spiderId=a7961de8da864577bf92fd3ae8b15acd&orderno=MF2018716215489Yuna&returnType=2&count=10")
    if res:
        data = res.json()
        if data["ERRORCODE"] != "0":
            return ""

        for d in data["RESULT"]:
            proxy_list.append({"http": "http://" + d["ip"] + ":" + str(d["port"])})

    return proxy_list.pop()


def crawl_xdaili():

    print("invoke xdaili...")

    url = 'http://www.baidu.com'
    html = requests.get(url)
    if html:
        for proxy in range(3):
            print("yield")
            # yield proxy


def main():

    # proxy = process()
    # print(proxy)

    print(crawl_xdaili())
    print(crawl_xdaili())
    print(crawl_xdaili())
    print(crawl_xdaili())

if __name__ == "__main__":
    main()