# -*- coding=utf-8 -*-
# Created Time: 2017年04月26日 星期三 16时54分33秒
# File Name: zheng.py

import re

temp = u"abc尼玛xyz您们"

xx = u"([\u4e00-\u9fff]+)"

pattern = re.compile(xx)

results = pattern.findall(temp)

for result in results:
    print result
