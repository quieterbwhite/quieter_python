# -*- coding=utf-8 -*-

import simplejson
import traceback
from util.service_mongo import mongo_service

conn_detail_a_name = "wsda201801"
wenshu_detail_a_conn = mongo_service.get_collection(conn_detail_a_name)


res_dict = {
        "title" : 0,                          # 标题
        "trial_round" : 0,                    # 审判阶段
        "case_no" : 0,                        # 案号
        "law_firm" : 0,                       # 法院名称
        "law_firm_province" : 0,              # 法院省
        "law_firm_city" : 0,                  # 法院市
        "law_firm_county" : 0,                # 法院区县
        "trial_date" : 0,                     # 裁判日期

        "plaintiff" : 0,                      # 原告
        "plaintiff_procurator" : 0,           # 原告委托代理人
        "plaintiff_agency" : 0,               # 原告委托代理律所

        "defendant" : 0,                      # 被告
        "defendant_procurator" : 0,           # 被告委托代理人
        "defendant_agency" : 0,               # 被告委托代理律所

        "accept_date" : 0,                    # 受理日期
        "hear_date" : 0,                      # 审理日期
        "program_type" : 0,                   # 程序类型
        "loan_principal" : 0,                 # 借款本金
        "credit_principal" : 0,               # 贷款本金
        "bar_fee" : 0,                        # 律师费
        "win_over" : 0,                       # 胜诉情况
        "verdict" : 0,                        # 裁决情况
        "dispute" : 0                         # 争议焦点
    }


def main():

    doc_list = wenshu_detail_a_conn.find({"trial_round" : "一审"})
    doc_detail_list = []

    for doc in doc_list:
        doc_detail_list.append(doc)

    index = 0
    for doc in doc_detail_list:
        print("Going index: {}".format(index))

        if doc["title"]: res_dict["title"] += 1
        if doc["trial_round"]: res_dict["trial_round"] += 1
        if doc["case_no"]: res_dict["case_no"] += 1
        if doc["law_firm"]: res_dict["law_firm"] += 1
        if doc["law_firm_province"]: res_dict["law_firm_province"] += 1
        if doc["law_firm_city"]: res_dict["law_firm_city"] += 1
        if doc["law_firm_county"]: res_dict["law_firm_county"] += 1
        if doc["trial_date"]: res_dict["trial_date"] += 1
        if doc["plaintiff"]: res_dict["plaintiff"] += 1
        if doc["plaintiff_procurator"]: res_dict["plaintiff_procurator"] += 1
        if doc["plaintiff_agency"]: res_dict["plaintiff_agency"] += 1
        if doc["defendant"]: res_dict["defendant"] += 1
        if doc["defendant_procurator"]: res_dict["defendant_procurator"] += 1
        if doc["defendant_agency"]: res_dict["defendant_agency"] += 1
        if doc["accept_date"]: res_dict["accept_date"] += 1
        if doc["hear_date"]: res_dict["hear_date"] += 1
        if doc["program_type"]: res_dict["program_type"] += 1
        if doc["loan_principal"]: res_dict["loan_principal"] += 1
        if doc["credit_principal"]: res_dict["credit_principal"] += 1
        if doc["win_over"]: res_dict["win_over"] += 1
        if doc["verdict"]: res_dict["verdict"] += 1
        if doc["dispute"]: res_dict["dispute"] += 1

    print(res_dict)

if __name__ == "__main__":

    main()