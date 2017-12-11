# -*- coding=utf-8 -*-
# Created Time: 2015年08月10日 星期一 11时01分27秒

'''
json web token
pip install PyJWT
'''

import jwt
import datetime
import time


def token_en(payload, secret, algorithm):
    """ 加密 """

    data = jwt.encode(payload, secret, algorithm=algorithm)
    return data

def token_de(en_data, secret, algorithm, options):
    """ 解密 """

    try:
        data = jwt.decode(en_data, secret, algorithms=[algorithm], options=options)
    except jwt.ExpiredSignatureError:
        return None, 20005
    except jwt.DecodeError:
        return None, 20004
    except jwt.InvalidTokenError:
        return None, 20004
    except:
        return None, 20004

    return data, 0


def main():

    payload = {
        'name':'tiger',
        'age':18,
        'exp':datetime.datetime.utcnow() + datetime.timedelta(seconds=2)
    }
    secret = '55c808909dd4e45ed22382ba'
    algorithm = 'HS256'

    en_data = token_en(payload, secret, algorithm)
    print 'en_data: ', en_data

    # 加密过后
    en_data = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwIjoiZWRlYTY1ZjJhZjlmM2E0N2U4MDliZGU1NDgzNjU3NWYiLCJyIjoxLCJleHAiOjE1MDExNDUxNjIsInNpZCI6MCwibiI6Ilx1NTIxOFx1NmQ5YiIsIm0iOiIxMzgwODAwNjIwNSIsImlkIjoxMDMyNTQ5LCJzdCI6ZmFsc2V9.Irl9H5-nJgg1uxymHpHHZ4WhrvVSp_8xwsQbq9XwfiA'

    # 选项设置
    options = {
       'verify_signature': True,
       'verify_exp': True,
       'verify_nbf': False,
       'verify_iat': False,
       'verify_aud': False,
       'require_exp': False,
       'require_iat': False,
       'require_nbf': False
    }

    # 测试 token 过期
    #time.sleep(3)

    de_data = token_de(en_data, secret, algorithm, options)
    print 'de_data: ', de_data

if __name__ == '__main__':
    main()
