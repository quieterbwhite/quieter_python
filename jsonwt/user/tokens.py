# -*- coding=utf-8 -*-
# Created Time: 2015年08月10日 星期一 11时01分27秒

'''
json web token
'''

import jwt
import datetime
import time


def token_en(payload, secret, algorithm):
    ''' 加密 '''

    data = jwt.encode(payload, secret, algorithm=algorithm)
    return data


def token_de(en_data, secret, algorithm, options):
    ''' 解密 '''

    try:
        data = jwt.decode(en_data, secret, algorithms=[algorithm], options=options)
    except jwt.ExpiredSignatureError:
        print 'ExpiredSignatureError'
        return None, 10009
    except jwt.DecodeError:
        print 'DecodeError'
        return None, 10008
    except jwt.InvalidTokenError:
        print 'InvalidTokenError'
        return None, 10007
    except:
        print 'Error'
        return None, 10006

    return data, 10000


def main():

    payload = {
        'name':'tiger',
        'age':18,
        'exp':datetime.datetime.utcnow() + datetime.timedelta(seconds=2)
    }
    secret = 'bwhite'
    algorithm = 'HS256'

    en_data = token_en(payload, secret, algorithm)
    print 'en_data: ', en_data

    # 加密过后
    #en_data = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhZ2UiOjI2LCJuYW1lIjoidGlnZXIifQ.pSFrqIgjiA17BKA16bSmm-m2t8ahnHobqz5zW7kr-b0'

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
    time.sleep(3)

    de_data = token_de(en_data, secret, algorithm, options)
    print 'de_data: ', de_data

if __name__ == '__main__': main()
