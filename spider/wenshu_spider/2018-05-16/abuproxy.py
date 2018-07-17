#! -*- encoding:utf-8 -*-

import requests

# 代理服务器
proxyHost = "http-dyn.abuyun.com"
proxyPort = "9020"

# 代理隧道验证信息
proxyUser = "H4524SSXO85V103D"
proxyPass = "7C1FFC5CD263FBE2"

proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
  "host" : proxyHost,
  "port" : proxyPort,
  "user" : proxyUser,
  "pass" : proxyPass,
}

abu_proxies = {
    "http"  : proxyMeta
    # "https" : proxyMeta,
}
