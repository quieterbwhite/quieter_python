# -*- coding=utf-8 -*-
# Created Time: 2015年09月30日 星期三 16时11分51秒
# File Name: err_mess.py

"""
返回处理中间件
"""

import json

from utils.errors import errs
from logs.mylog   import flogger


class AddErrMsgMiddleware(object):

    def process_response(self, request, response):

        if response.status_code == 404:
            return self.return_404(response)

        try:
            c = json.loads(response.content)
            c["msg"] = errs[c["code"]]
        except:
            # 返回的内容不是json, 有可能是需要直接返回页面
            return response

        response.content = json.dumps(c)

        flogger.info("Return:")
        flogger.info(response.content)
        return response

    def return_404(self, response):
        err_dict = {
                "code" : 404,
                "msg"  : "not found"
            }
        response.content = json.dumps(err_dict)
        return response





