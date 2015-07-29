# -*- coding=utf-8 -*-
# Created Time: Tue 28 Jul 2015 10:15:29 PM CST
# File Name: 01_test_expiration.py

'''
测试 json web token expiration
'''

import datetime
import time
import jwt

options = {
   'verify_signature': True,
   'verify_exp': True
}

jwt_payload = jwt.encode({
    'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=5),
    'name':'tiger'
}, 'secret', algorithm='HS256')

time.sleep(6)

res = jwt.decode(jwt_payload, 'secret', options=options)

print 'res: ', res
