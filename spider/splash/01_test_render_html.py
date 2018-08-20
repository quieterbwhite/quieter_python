# -*- coding=utf-8 -*-
# Created Time: 2018年08月15日 星期三 10时54分16秒
# File Name: 01_test_render_html.py

import requests

url = 'http://localhost:8050/render.html?url=http://wenshu.court.gov.cn/list/list/?sorttype=1&number=L9KSR3VJ&guid=d2488742-6230-bef3301e-103bb5c0ec25&conditions=searchWord+2+AJLX++%E6%A1%88%E4%BB%B6%E7%B1%BB%E5%9E%8B:%E6%B0%91%E4%BA%8B%E6%A1%88%E4%BB%B6&conditions=searchWord+002004001024001+AY++%E6%A1%88%E7%94%B1:%E9%87%91%E8%9E%8D%E5%80%9F%E6%AC%BE%E5%90%88%E5%90%8C%E7%BA%A0%E7%BA%B7&conditions=searchWord++CPRQ++%E8%A3%81%E5%88%A4%E6%97%A5%E6%9C%9F:2018-07-01%20TO%202018-07-01&wait=20'

response = requests.get(url)

print(response.text)
