# -*- coding=utf-8 -*-

"""
根据条件搜索列表，翻页并保存
"""

import cgitb
import time
import traceback

import requests

from constant.constant_request import RequestConstant
from service.service_mongo import mongo_service
from common import request_data, handle_page

# cgitb.enable(format='text')

conn_name = "wk201804"
conn_name_fail = conn_name + "_fail"
judgements_conn_name = mongo_service.get_collection(conn_name)
judgements_conn_name_fail = mongo_service.get_collection(conn_name_fail)


def download_result_tree(searchId):
    """ 下载结果树

    :param searchId string : f7260f61ba4f4ed5ba00c42ba2df5fdc

    :return task_list list 任务列表
    """

    url = RequestConstant.GET_RESULT_TREE_URL.format(searchId)

    data_json = request_data(url, RequestConstant.HEADERS, method="get")
    if not data_json:
        print("没有获取到搜索结果树")
        return None

    time.sleep(2)
    task_list = data_json["children"]
    return task_list


def detect_count(payload):
    """ 检测结果条数是否超过限制

    如果没超过限制，交给下载方法
    如果超过限制，获取结果树，构造任务列表
    """

    print("开始检测该搜索条件的结果数...")
    data_json = request_data(RequestConstant.SEARCH_URL, RequestConstant.HEADERS, payload=payload, method="post")
    if not data_json:
        print("检测结果条数失败，没有获取到结果")
        return 0, ""

    docCount = data_json["searchMetadata"]["docCount"]
    searchId = data_json["searchMetadata"]["searchId"]
    print("检测到当前日期的记录条数 docCount == {}".format(docCount))

    return docCount, searchId


def get_task_list(docCount, searchId, payload):
    """ 处理任务列表 """

    if docCount > RequestConstant.RESULT_LIMIT:
        print("检测到一级搜索结果数大于限制，准备分批处理, 生成任务")
        task_list = download_result_tree(searchId)
        # print(task_list)
        if not task_list: return None
        my_task_list = handle_task(task_list, payload)
    else:
        print("检测到一级搜索结果数小于限制，将直接处理")
        my_task_list = [{"payload": payload, "nHits": docCount}]

    return my_task_list


def handle_task(task_list, payload):
    """ 任务处理

    递归处理任务列表
    当前任务结果数小于限制，交付抓取
    当前任务结果数大于限制，将子任务添加到任务列表中继续下一次判断, 直到结果数小于限制数交付抓取
    """

    my_task_num = 0
    my_task_list = []

    for node in task_list:
        nodeId, nHits = node["nodeId"], node["nHits"]

        if nHits > RequestConstant.RESULT_LIMIT:
            if node["children"] == None:
                pass
            else:
                handle_task(node["children"], payload)
        else:
            print("添加新的抓取任务")
            payload["searchScope"]["treeNodeIds"] = [nodeId]
            my_task_list.append({"payload" : payload, "nHits" : nHits})
            # print(nHits)
            # print(nodeId)
            my_task_num += nHits

    print("my_task_num: {}".format(my_task_num))
    return my_task_list


def process(payload, nHits, day_for_save):
    """ 执行最终的抓取 """

    # 处理分页
    total_page = handle_page(nHits)

    # 分页抓取
    for offset in range(total_page):
        time.sleep(3)
        payload["pageInfo"].update({"offset": offset * RequestConstant.OFFSET_GET_DATA})

        data_json = request_data(RequestConstant.SEARCH_URL, RequestConstant.HEADERS, payload=payload, method="post")
        if not data_json:
            print("请求结果为空, 下一页")
            continue

        for doc in data_json["documentList"]:
            doc.update({"day" : day_for_save})
            judgements_conn_name.insert(doc)
        print("Insert Result.")

def save_fail(day):

    print("save failed day data")
    judgements_conn_name_fail.insert({"day" : day})


if __name__ == "__main__":

    total_page = handle_page(20)
    print(total_page)
    print(range(total_page))

