# -*- coding=utf-8 -*-
# Created Time: 2016年08月17日 星期三 14时29分11秒
# File Name: 02_wipe_off_html_in_str.py

"""
去除网页文本中的所有 html 标签
"""

"""
1.

import re
str = "<img /><a>srcd</a >hello</br><br/>"
str = re.sub(r'</?\w+[^>]*>','',str)
print str

"""


"""

ref: https://gist.github.com/dndn/859717

"""