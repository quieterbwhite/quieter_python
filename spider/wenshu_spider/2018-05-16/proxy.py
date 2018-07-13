# -*-encoding:utf-8-*-

"""
获取代理ip
"""

import requests


def process():

    try:
        res = requests.get("http://webapi.http.zhimacangku.com/getip?num=20&type=2&pro=0&city=0&yys=0&port=1&pack=24397&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=2&regions=", timeout=10)
    except Exception as e:
        return None

    data = res.json()
    ip = data["data"][0]["ip"]
    port = data["data"][0]["port"]

    proxy = {"http" : "http://" + ip + ":" + str(port)}

    return proxy


def main():

    proxy = process()

    print(proxy)

if __name__ == "__main__":
    main()