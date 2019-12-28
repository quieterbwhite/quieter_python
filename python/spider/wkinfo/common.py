# -*- coding=utf-8 -*-

"""
公共方法
"""

import traceback
from logs.mylog import flogger
from constant.constant_request import RequestConstant


def request_data(session, url, payload=None, method="post"):
    """ 发起请求获取数据

    :param url
    :param headers
    :param payload

    :return json_data
    """

    try:
        if method == "get":
            res = session.get(url, timeout=RequestConstant.REQUEST_TIMEOUT)
        else:
            res = session.post(url, json=payload, timeout=RequestConstant.REQUEST_TIMEOUT)
    except Exception as e:
        flogger.info(traceback.format_exc())
        return None

    if res.status_code == 502:
        return None

    if res.status_code == 400:
        flogger.info("返回错误码: {}".format(res.status_code))
        flogger.info(res.json())
        return "relogin"

    if not res:
        flogger.info("No Results")
        return "relogin"

    json_data = res.json()
    return json_data


def request_login(session, url, payload):
    """ 发起登录 """

    try:
        res = session.post(url, json=payload, timeout=RequestConstant.REQUEST_TIMEOUT)
    except Exception as e:
        flogger.info(traceback.format_exc())
        return "Exception"

    if res.status_code != 200:
        flogger.info("返回错误码: {}".format(res.status_code))
        flogger.info(res.json())
        return "relogin"

    if not res:
        flogger.info("No Results")
        return "relogin"

    try:
        user_data = res.json()
    except Exception as e:
        flogger.info(traceback.format_exc())
        return "Exception"

    return user_data


def handle_page(nHits):
    """ 处理分页 """

    total_page = int(nHits / RequestConstant.OFFSET_GET_DATA)

    if nHits % RequestConstant.OFFSET_GET_DATA > 0: total_page += 1

    return total_page