# -*- coding=utf-8 -*-
# File Name: auth_token.py

"""
登录, 权限
"""

from django.conf   import settings
from django.http   import JsonResponse

from utils.tokens  import token_de

from logs.mylog    import flogger


class TokenAuthMiddleware(object):

    def process_request(self, request):

        req_path = request.path
        flogger.info("TokenAuthMiddleware - req_path: %s" % req_path)

        flogger.info(request.body)

        http_token = request.META.get("token", "")

        status, data = TokenAuthMiddleware.auth_token(http_token)

        if not status: return JsonResponse(data)

        return

    @classmethod
    def auth_token(cls, token):
        """ 验证 token 是否合法 """

        res = {"code": 0}

        de_data, err_code = token_de(
            token, settings.JWT_SECRET, settings.JWT_ALGORITHM, settings.JWT_OPTIONS
        )

        if not de_data:
            res.update({"code": err_code})
            return False, res

        return True, de_data