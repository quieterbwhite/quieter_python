# -*- coding=utf-8 -*-

"""
公共方法
"""

import requests
import traceback

from constant.constant_request import RequestConstant


def request_data(url, headers, payload=None, method="post"):
    """ 发起请求获取数据

    :param url
    :param headers
    :param payload

    :return json_data
    """

    try:
        if method == "get":
            res = requests.get(url, headers=headers, timeout=RequestConstant.REQUEST_TIMEOUT)
        else:
            res = requests.post(url, headers=headers, json=payload, timeout=RequestConstant.REQUEST_TIMEOUT)
    except Exception as e:
        print(traceback.format_exc())
        return None

    if not res:
        print("No Results")
        return None

    try:
        json_data = res.json()
    except Exception as e:
        print(traceback.format_exc())
        return None

    return json_data


def handle_page(nHits):
    """ 处理分页 """

    total_page = int(nHits / RequestConstant.OFFSET_GET_DATA)

    if nHits % RequestConstant.OFFSET_GET_DATA > 0: total_page += 1

    return total_page