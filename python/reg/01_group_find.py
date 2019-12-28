# -*- coding=utf-8 -*-
# Created Time: 2016年07月07日 星期四 22时41分41秒
# File Name: 01_group_find.py

'''
正则表达式， 简单查找
'''

import re

text = 'hello_world window.QRLogin.code = 200; window.QRLogin.uuid = "tiger_uuid"; and what do you think.'

regx = r'window.QRLogin.code = (\d+); window.QRLogin.uuid = "(\S+?)";'
# 我们可以看到返回的量是上述的格式，括号内的内容被提取了出来
data = re.search(regx, text)
if data:
	print 'code: ', data.group(1)
	print 'uuid: ', data.group(2)
else:
	print '404'
