# -*- coding=utf-8 -*-
# Created Time: 2018年08月07日 星期二 17时10分53秒
# File Name: 01_lua_execute_remote.py

"""

"""

import time
import requests
from urllib.parse import quote

lua = '''
function main(splash, args)
  splash.images_enabled = false
  assert(splash:go("http://wenshu.court.gov.cn/list/list/?sorttype=1&number=UUR9JCAC&guid=4d02a5f7-c85b-3eb788ba-b63bbf8ae2f3&conditions=searchWord+002004001024001+AY++%E6%A1%88%E7%94%B1:%E9%87%91%E8%9E%8D%E5%80%9F%E6%AC%BE%E5%90%88%E5%90%8C%E7%BA%A0%E7%BA%B7&conditions=searchWord++CPRQ++%E8%A3%81%E5%88%A4%E6%97%A5%E6%9C%9F:2018-06-01%20TO%202018-06-01"))
  assert(splash:wait(0.5))
  local vl5x = splash:evaljs("getKey()")
  local cookies = splash:get_cookies()
  return {
    cookies=cookies,
    vl5x=vl5x
    }
end
'''

try:
    vjkl5 = ""
    url = 'http://localhost:8050/execute?lua_source=' + quote(lua)
    response = requests.get(url, timeout=20)
    vl5x = data["vl5x"]
except Exception as ex:
    pass

data = response.json()
for i in data["cookies"]:
    if i["name"] == "vjkl5":
        vjkl5 = i["value"]

if vjkl5 and vl5x:
    print({"vjkl5":vjkl5, "vl5x":vl5x})

return None

