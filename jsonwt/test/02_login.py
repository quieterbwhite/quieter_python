# -*- coding=utf-8 -*-
# Created Time: 2015年08月04日 星期二 18时05分34秒
# File Name: 01_auth_ticket.py

'''
登录
'''

import requests
import json
url = "http://localhost:8000/user/login"

post_data = '''
{
    "username":"bwhite",
    "password":"tiger"
}
'''

r = requests.post(url, data=post_data)
print 'status_code: ', r.status_code
#print r.text
j = r.json()
print json.dumps(j, ensure_ascii=False)


