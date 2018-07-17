# -*-encoding:utf-8-*-

"""
获取文书详情
"""

from util.service_mongo import mongo_service
from logs.mylog import flogger
from shock import getCourtInfo

import time

conn_name = "ws_201806_foshan"
conn_detail_name = "ws_201806_foshan_d"
wenshu_conn = mongo_service.get_collection(conn_name)
wenshu_detail_conn = mongo_service.get_collection(conn_detail_name)


def get_detail(docid):

    detail_data_flaw = getCourtInfo(docid)
    if not detail_data_flaw: return

    doc = {
        "time" : int(time.time()),
        "docid" : docid,
        "data_flaw" : detail_data_flaw
    }
    wenshu_detail_conn.insert(doc)

    flogger.info("Save Doc Detail")

def loop():

    doc_list = wenshu_conn.find({})
    doc_id_list = []

    flogger.info("Getting doc id")
    for doc in doc_list:
        docid = doc["docid"]
        doc_id_list.append(docid)

    flogger.info("Got doc id list: {}".format(doc_id_list))
    for docid in doc_id_list:
        flogger.info("DOCID: {}".format(docid))
        get_detail(docid)
        time.sleep(3)


def main():

    loop()

if __name__ == "__main__":
    main()