# -*- coding=utf-8 -*-

"""
获取文书详情

header:
    http://law.wkinfo.com.cn/csi/document/MjAyMzc5NjUxNzg=?indexId=law.case

body:
    http://law.wkinfo.com.cn/csi/document/MjAyMzc5NjUxNzg=/html?indexId=law.case&flogger.info=false&fromType=null&useBalance=true

header 和 body 提取有用部分合并成一个数据存储

从任务队列中获取任务执行，抓取正文，合并数据，保存mongodb.
失败的情况: 重试3次，还是不行的话重新放入队列。
"""

import re
import time

from common import request_data
from constant.constant_request import RequestConstant
from service.service_mongo import mongo_service
from login import get_new_session
from logs.mylog import flogger

list_data_name = "wk201806"
list_data_conn_name = mongo_service.get_collection(list_data_name)

conn_name = "wkd201806"
conn_name_fail = conn_name + "_fail"
judgements_conn_name = mongo_service.get_collection(conn_name)
judgements_conn_name_fail = mongo_service.get_collection(conn_name_fail)


def get_header(session, docid):
    """ 获取文书头部 """

    data_json = None
    url = RequestConstant.GET_DOC_HEADER_URL.format(docid)

    for i in range(3):
        data_json = request_data(session, url, RequestConstant.HEADERS, method="get")
        if data_json == "relogin":
            return "relogin"

        if data_json:
            break

        time.sleep(2)

    if not data_json:
        flogger.info("获取 header 失败, 记录")
        return None

    # flogger.info(data_json)
    flogger.info("获取到 header 数据")
    return data_json


def get_body(session, docid):
    """ 获取文书正文 """

    data_json = None
    url = RequestConstant.GET_DOC_BODY_URL.format(docid)

    for i in range(3):
        data_json = request_data(session, url, RequestConstant.HEADERS, method="get")

        if data_json == "relogin":
            return "relogin"

        if data_json: break
        time.sleep(2)

    if not data_json:
        flogger.info("获取 body 失败, 记录")
        return None

    # flogger.info(data_json)
    flogger.info("获取到 body 数据")
    return data_json


def loop_me(session, docid):

    header_json = get_header(session, docid)
    if header_json == "relogin":
        return "relogin"

    if not header_json:
        judgements_conn_name_fail.insert({"docid" : docid})
        return None

    body_json = get_body(session, docid)
    if body_json == "relogin":
        return "relogin"

    if not body_json:
        judgements_conn_name_fail.insert({"docid" : docid})
        return None

    cause_of_action = re.sub(r'</?\w+[^>]*>', '', header_json["currentDoc"]["additionalFields"]["causeOfActionText"])
    content = re.sub(r'</?\w+[^>]*>', '', body_json["content"])
    # content = body_json["content"]

    if len(content) < 30:
        flogger.info("获取结果失败，账户被封")
        judgements_conn_name_fail.insert({"docid" : docid})
        return None

    # 解析数据
    my_doc = {
        "docid" : docid,
        "title" : header_json["currentDoc"]["title"],
        "court" : header_json["currentDoc"]["additionalFields"]["courtText"],
        "cause_of_action" : cause_of_action,
        "doc_number" : header_json["currentDoc"]["additionalFields"]["documentNumber"],
        "judgment_date" : header_json["currentDoc"]["additionalFields"]["judgmentDate"],
        "content" : content
    }

    judgements_conn_name.insert(my_doc)
    flogger.info("保存数据 :)\n")


def get_docid_from_db():
    """ 从数据库获取当月所有docid """

    now = 0
    # docid_list = ["MjAyMzU4MTA2NTQ="]
    docid_list = []

    month_data_list = list_data_conn_name.find({})
    for data in month_data_list:
        docid_list.append(data["docId"])

    session = get_new_session()

    for docid in docid_list:

        now += 1

        try:
            flogger.info("Num: {} - 开始抓取 {} 的详情数据:)".format(now, docid))
            data = loop_me(session, docid)
            if data == "relogin":
                session = get_new_session()
        except Exception as e:
            pass

        time.sleep(3)


if __name__ == "__main__":

    get_docid_from_db()