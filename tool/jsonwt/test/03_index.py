# -*- coding=utf-8 -*-
# Created Time: 2015年08月04日 星期二 18时05分34秒
# File Name: 01_auth_ticket.py

'''
用户中心
'''

import requests
import json
url = "http://localhost:8000/user/index"

headers = {
    "token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImJ3aGl0ZSIsIm1vYmlsZSI6IjE1MjAyODk3ODM1IiwidWlkIjoiNTVjODA4OTA5ZGQ0ZTQ1ZWQyMjM4MmJhIiwiZXhwIjoxNDM5MjA4NzcyfQ.RWZ1KhZTsl05gsMVJy7lJZDXO_ISpv4H80qLBYpGp5c"
}

post_data = '''
{}
'''

r = requests.post(url, data=post_data, headers=headers)
print 'status_code: ', r.status_code
#print r.text
j = r.json()
print json.dumps(j, ensure_ascii=False)


