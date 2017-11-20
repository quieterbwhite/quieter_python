# -*- coding=utf-8 -*-
# Created Time: 2017年11月20日 星期一 23时39分41秒
# File Name: 04_mitmproxy.py

"""

注意:

    还有https的问题需要解决

http://docs.mitmproxy.org/en/latest/mitmproxy.html

https://mitmproxy.org/

https://segmentfault.com/q/1010000000094520

https://blog.heckel.xyz/2013/07/01/how-to-use-mitmproxy-to-read-and-modify-https-traffic-of-your-phone/

使用场景转向 Android/Webview
mitmproxy 是个命令行下查看/修改 http 请求的交互式工具


sudo apt-get install python-dev libffi-dev libxml2-dev libxslt-dev python3-pip

sudo pip3 install mitmproxy


ubuntu 上启动 mitmproxy
mitmproxy --host

手机 设置 -> WLAN -> 代理
主机名: ubuntu 的 ip
端口: 8080

然后访问网络就会在 mitmproxy 里看到请求记录(如截图)


快捷键
j,k 上下移动
enter 进入
tab 切换 request/response

参考
http://mitmproxy.org/doc/mitmproxy.html
http://blog.philippheckel.com/2013/07/01/how-to-use-mitmproxy-to-read-and-modify-https-traffic-of-your-phone/

"""
