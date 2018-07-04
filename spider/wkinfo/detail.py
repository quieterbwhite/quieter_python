# -*- coding=utf-8 -*-

"""
获取文书详情

header:
    http://law.wkinfo.com.cn/csi/document/MjAyMzc5NjUxNzg=?indexId=law.case

body:
    http://law.wkinfo.com.cn/csi/document/MjAyMzc5NjUxNzg=/html?indexId=law.case&print=false&fromType=null&useBalance=true

header 和 body 提取有用部分合并成一个数据存储

从任务队列中获取任务执行，抓取正文，合并数据，保存mongodb.
失败的情况: 重试3次，还是不行的话重新放入队列。
"""

import re
import time

from common import request_data
from constant.constant_request import RequestConstant
from service.service_mongo import mongo_service


list_data_name = "wk201806"
list_data_conn_name = mongo_service.get_collection(list_data_name)

conn_name = "wkd201806"
conn_name_fail = conn_name + "_fail"
judgements_conn_name = mongo_service.get_collection(conn_name)
judgements_conn_name_fail = mongo_service.get_collection(conn_name_fail)


def get_header(docid):
    """ 获取文书头部 """

    data_json = None
    url = RequestConstant.GET_DOC_HEADER_URL.format(docid)

    for i in range(3):
        data_json = request_data(url, RequestConstant.HEADERS, method="get")
        if data_json:
            time.sleep(1)
            break
        time.sleep(2)

    if not data_json:
        print("获取 header 失败, 记录")
        return None

    # print(data_json)
    print("获取到 header 数据")
    return data_json


def get_body(docid):
    """ 获取文书正文 """

    data_json = None
    url = RequestConstant.GET_DOC_BODY_URL.format(docid)

    for i in range(3):
        data_json = request_data(url, RequestConstant.HEADERS, method="get")
        if data_json: break
        time.sleep(2)

    if not data_json:
        print("获取 body 失败, 记录")
        return None

    # print(data_json)
    print("获取到 body 数据")
    return data_json


def loop_me(docid):

    docid = "MjAyMzU4MTA2NTQ="

    header_json = get_header(docid)
    if not header_json:
        judgements_conn_name_fail.insert({"docid" : docid})
        return

    body_json = get_body(docid)
    if not body_json:
        judgements_conn_name_fail.insert({"docid" : docid})
        return

    cause_of_action = re.sub(r'</?\w+[^>]*>', '', header_json["currentDoc"]["additionalFields"]["causeOfActionText"])
    content = re.sub(r'</?\w+[^>]*>', '', body_json["content"])
    # content = body_json["content"]

    if len(content) < 30:
        print("获取结果失败，账户被封")
        judgements_conn_name_fail.insert({"docid" : docid})
        return

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
    print("保存数据 :)\n")


def get_docid_from_db():
    """ 从数据库获取当月所有docid """

    now = 0
    docid_list = []

    month_data_list = list_data_conn_name.find({})
    for data in month_data_list:
        docid_list.append(data["docId"])

    for docid in docid_list:
        now += 1
        try:
            print("Num: {} - 开始抓取 {} 的详情数据:)".format(now, docid))
            loop_me(docid)
        except Exception as e:
            pass

        time.sleep(3)


def test_reg():

    # str = "<a class=\"contentlink\" href=\"../search/process?collection=case&search_form_breadcrumbs=causeOfAction%C7%8101000000000000%E6%B0%91%E4%BA%8B%C7%81%C7%82%E6%B0%91%E4%BA%8B\">民事</a>><a class=\"contentlink\" href=\"../search/process?collection=case&search_form_breadcrumbs=causeOfAction%C7%8101000000000000%E6%B0%91%E4%BA%8B%2F01040000000000%E5%90%88%E5%90%8C%E3%80%81%E6%97%A0%E5%9B%A0%E7%AE%A1%E7%90%86%E3%80%81%E4%B8%8D%E5%BD%93%E5%BE%97%E5%88%A9%E7%BA%A0%E7%BA%B7%C7%81%C7%82%E5%90%88%E5%90%8C%E3%80%81%E6%97%A0%E5%9B%A0%E7%AE%A1%E7%90%86%E3%80%81%E4%B8%8D%E5%BD%93%E5%BE%97%E5%88%A9%E7%BA%A0%E7%BA%B7\">合同、无因管理、不当得利纠纷</a>><a class=\"contentlink\" href=\"../search/process?collection=case&search_form_breadcrumbs=causeOfAction%C7%8101000000000000%E6%B0%91%E4%BA%8B%2F01040000000000%E5%90%88%E5%90%8C%E3%80%81%E6%97%A0%E5%9B%A0%E7%AE%A1%E7%90%86%E3%80%81%E4%B8%8D%E5%BD%93%E5%BE%97%E5%88%A9%E7%BA%A0%E7%BA%B7%2F01040010000000%E5%90%88%E5%90%8C%E7%BA%A0%E7%BA%B7%C7%81%C7%82%E5%90%88%E5%90%8C%E7%BA%A0%E7%BA%B7\">合同纠纷</a>><a class=\"contentlink\" href=\"../search/process?collection=case&search_form_breadcrumbs=causeOfAction%C7%8101000000000000%E6%B0%91%E4%BA%8B%2F01040000000000%E5%90%88%E5%90%8C%E3%80%81%E6%97%A0%E5%9B%A0%E7%AE%A1%E7%90%86%E3%80%81%E4%B8%8D%E5%BD%93%E5%BE%97%E5%88%A9%E7%BA%A0%E7%BA%B7%2F01040010000000%E5%90%88%E5%90%8C%E7%BA%A0%E7%BA%B7%2F01040010240000%E5%80%9F%E6%AC%BE%E5%90%88%E5%90%8C%E7%BA%A0%E7%BA%B7%C7%81%C7%82%E5%80%9F%E6%AC%BE%E5%90%88%E5%90%8C%E7%BA%A0%E7%BA%B7\">借款合同纠纷</a>"

    # str = "<!--静态化时间:2018.07.03 12:17:54--><div class=\"bookscon\"\r\n\tstyle=\"border: none; border-top: 3px solid #7bb643;\">\r\n<h1 class=\"biao\">利华物贸公司等合同执行裁定书</h1>\r\n<div class=\"zydz-cn\"></div>\r\n<table class=\"metatbl\" cellpadding=\"0\" cellspacing=\"0\" id=\"casemeta\">\r\n    <tr>\r\n        <td class=\"casechmeata\"><span class=\"metaname\" id=\"cchcncourtshow\">审理法院：</span></td> \r\n        <td class=\"casechmeataval\"><span class=\"metaname\" id=\"cchcncourt\">北京市西城区人民法院</span></td>   \r\n    </tr>\r\n    <tr>\r\n\t    <td class=\"casechmeata\"><span class=\"metaname\" id=\"cchcncasenumbershow\">案号：</span></td> \r\n        <td class=\"casechmeataval\"><span class=\"metaname\" id=\"cchcncasenumber\">(2018)京0102执异98号</span></td>   \r\n    </tr>\r\n    <tr>\r\n        <td class=\"casechmeata\"><span class=\"metaname\" id=\"cchcnjudgmentdateshow\">裁判日期：</span></td> \r\n        <td class=\"casechmeataval\"><span class=\"metaname\" id=\"cchcnjudgmentdate\">2018.07.02</span></td>   \r\n    </tr>\r\n    <tr>\r\n        <td class=\"casechmeata\"><span class=\"metaname\" id=\"cchcncauseofactionshow\">案由：</span></td> \r\n        <td class=\"casechmeataval\"><span class=\"metaname\" id=\"cchcncauseofaction\"><a class=\"contentlink\" href=\"../search/process?collection=case&search_form_breadcrumbs=causeOfAction%C7%8101000000000000%E6%B0%91%E4%BA%8B%C7%81%C7%82%E6%B0%91%E4%BA%8B\">民事</a>><a class=\"contentlink\" href=\"../search/process?collection=case&search_form_breadcrumbs=causeOfAction%C7%8101000000000000%E6%B0%91%E4%BA%8B%2F01040000000000%E5%90%88%E5%90%8C%E3%80%81%E6%97%A0%E5%9B%A0%E7%AE%A1%E7%90%86%E3%80%81%E4%B8%8D%E5%BD%93%E5%BE%97%E5%88%A9%E7%BA%A0%E7%BA%B7%C7%81%C7%82%E5%90%88%E5%90%8C%E3%80%81%E6%97%A0%E5%9B%A0%E7%AE%A1%E7%90%86%E3%80%81%E4%B8%8D%E5%BD%93%E5%BE%97%E5%88%A9%E7%BA%A0%E7%BA%B7\">合同、无因管理、不当得利纠纷</a>><a class=\"contentlink\" href=\"../search/process?collection=case&search_form_breadcrumbs=causeOfAction%C7%8101000000000000%E6%B0%91%E4%BA%8B%2F01040000000000%E5%90%88%E5%90%8C%E3%80%81%E6%97%A0%E5%9B%A0%E7%AE%A1%E7%90%86%E3%80%81%E4%B8%8D%E5%BD%93%E5%BE%97%E5%88%A9%E7%BA%A0%E7%BA%B7%2F01040010000000%E5%90%88%E5%90%8C%E7%BA%A0%E7%BA%B7%C7%81%C7%82%E5%90%88%E5%90%8C%E7%BA%A0%E7%BA%B7\">合同纠纷</a>><a class=\"contentlink\" href=\"../search/process?collection=case&search_form_breadcrumbs=causeOfAction%C7%8101000000000000%E6%B0%91%E4%BA%8B%2F01040000000000%E5%90%88%E5%90%8C%E3%80%81%E6%97%A0%E5%9B%A0%E7%AE%A1%E7%90%86%E3%80%81%E4%B8%8D%E5%BD%93%E5%BE%97%E5%88%A9%E7%BA%A0%E7%BA%B7%2F01040010000000%E5%90%88%E5%90%8C%E7%BA%A0%E7%BA%B7%2F01040010240000%E5%80%9F%E6%AC%BE%E5%90%88%E5%90%8C%E7%BA%A0%E7%BA%B7%C7%81%C7%82%E5%80%9F%E6%AC%BE%E5%90%88%E5%90%8C%E7%BA%A0%E7%BA%B7\">借款合同纠纷</a></span></td>   \r\n    </tr>\r\n</table>\r\n\r\n<div class=\"clear\"></div>\r\n<h3 class=\"zhengwen\">正文</h3>\r\n<div class=\"zwcontent\"\r\n\tstyle=\"background: url(../images/fagui-center-bg.gif) repeat-y;\">\r\n<p class=\"zw-topbg\"></p>\r\n<div class=\"faguicon_case\">\r\n<p class=\"cncasetitle\">北京市西城区人民法院</p>\r\n<p class=\"cncasesubtitle\">执行裁定书</p>\r\n<p class=\"doc-A\" align=\"right\">（2018）京0102执异98号</p>\r\n<p class=\"caseDocPart1\">\r\n<span>申请人：润木财富投资管理集团有限公司（以下简称润木公司），住所地北京市经济技术开发区西环南路18号B座123室。</span>\r\n<span>法定代表人：付春玲，经理。</span>\r\n<span>委托诉讼代理人：李威，润木财富投资管理集团有限公司法务专员。</span>\r\n<span>申请执行人：中国工商银行股份有限公司北京南礼士路支行（以下简称南礼士路支行），住所地北京市西城区阜成门外大街8号。</span>\r\n<span>负责人：江波，行长。</span>\r\n<span>委托诉讼代理人：李嘉，中国工商银行股份有限公司北京南礼士路支行职员。</span>\r\n<span>委托诉讼代理人：李民峰，中国工商银行股份有限公司北京南礼士路支行职员。</span>\r\n</p>\r\n<br><p class=\"caseDocPart2\">\r\n<span>本院在审查中国工商银行股份有限公司北京南礼士路支行（以下简称南礼士路支行）申请执行利华物贸公司、中国华通物产集团公司借款合同纠纷一案中，申请人润木财富投资管理集团有限公司（以下简称润木公司）向本院申请变更为本案的申请执行人，并提供了《债权转让协议》等证明材料。</span>\r\n<span>本院查明，本院（2001）西经初字第390号民事判决发生法律效力后，该案原告中国工商银行北京市南礼士支行向本院申请执行，本院予以立案，案号为（2001）西执字第749号。该案的被执行人为利华物贸公司、中国华通物产集团公司。</span>\r\n<span>后，中国工商银行北京市南礼士支行更名为中国工商银行股份有限公司北京南礼士路支行。</span>\r\n<span>2005年7月18日，中国工商银行北京市分行将上述执行案件的债权转让给中国信达资产管理公司北京办事处，2005年7月29日，中国工商银行北京市分行与中国信达资产管理公司北京办事处进行联合公告，对债权转让向利华物贸公司、中国华通物产集团公司进行公告通知并就债权进行催收。2010年，中国信达资产管理公司北京办事处更名为中国信达资产管理股份有限公司北京市分公司。2013年12月3日，中国信达资产管理股份有限公司北京市分公司将上述执行案件的债权转让给中经信投资有限公司。2014年1月29日，中国信达资产管理股份有限公司北京市分公司与中经信投资有限公司进行联合公告，对债权转让向利华物贸公司、中国华通物产集团公司进行公告通知并就债权进行催收。2016年11月21日，中经信投资有限公司将上述执行案件的债权转让给润木公司。2017年10月25日，中经信投资有限公司与润木公司进行联合公告，对债权转让向利华物贸公司、中国华通物产集团公司进行公告通知并就债权进行催收。</span>\r\n<span>本案审理中，南礼士路支行表示同意变更润木公司为（2001）西执字第749号执行案件的申请执行人。</span>\r\n<span>本院认为，因润木公司现已依法取得了南礼士路支行在（2001）西执字第749号执行案件中的合法债权，且南礼士路支行亦同意润木公司的变更申请，故润木公司申请变更为（2001）西执字第749号执行案件的申请执行人的请求事项合法有据，本院应予支持。据此，依照《<a target=\"_blank\" class=\"contentlink\" href=\"../document/show?collection=legislation&aid=MTAxMDAxMjQyNjg%3D&language=中文\">中华人民共和国民事诉讼法</a>》<a target=\"_blank\" class=\"contentlink\" href=\"../document/show?collection=legislation&aid=MTAxMDAxMjQyNjg%3D&language=中文#No576_Z12J5T154\">第一百五十四条第一款第十一项</a>、《最高人民法院关于民事执行变更、追加当事人的若干规定》第九条、第三十条之规定，裁定如下：</span>\r\n<span>变更润木财富投资管理集团有限公司为（2001）西执字第749号执行案件的申请执行人。</span>\r\n<span>如不服本裁定，可以自裁定书送达之日起十日内向北京市第二中级人民法院申请复议。</span>\r\n</p><p class=\"caseDocFooterStyle\">\r\n<p class=\"footerStyle\">审　判　长： 李  　振</p><p class=\"footerStyle\">审　判　员： 许  　波</p><p class=\"footerStyle\">人民陪审员： 葛 根 武</p><p class=\"footerStyle\">二０一八年七 月 二 日</p><p class=\"footerStyle\">书　记　员： 曾  　佳</p>\r\n</p>\r\n<p class=\"doc-A\" align=\"right\"></p>\r\n<p class=\"doc-A\" align=\"right\"></p>\r\n<p class=\"doc-A\" align=\"right\"></p>\r\n<p><span id=\"attchmentContent\"></span></p>\r\n</div>\r\n<div class=\"clear\"></div>\r\n<p class=\"zw-downbg\"></p>\r\n</div>\r\n</div>\r\n<!--hidden data  -->\r\n<input type=\"hidden\" value=\"MjAyMzc5NjUxNzg%3D\" name=\"documentaid\"\r\n\tid=\"documentaid\" />\r\n<input type=\"hidden\" value=\"利华物贸公司等合同执行裁定书\" name=\"documenttitle\"\r\n\tid=\"documenttitle\" />\r\n<input type=\"hidden\"\r\n\tvalue=\"MjAyMzc5NjUxNzg%3D;case;利华物贸公司等合同执行裁定书;;;;default\"\r\n\tname=\"documentcheckThisCol\" id=\"documentcheckThisCol\" />\r\n\r\n<input type=\"hidden\" name=\"collection\" value=\"case\" />\r\n<input id=\"documentshowtype\" type=\"hidden\" name=\"documentshowtype\"\r\n\tvalue=\"\" />"
    # data = re.sub(r'</?\w+[^>]*>', '', str)
    # print(data)

    pass


if __name__ == "__main__":

    # main()
    # test_reg()
    get_docid_from_db()

    # loop_me("fas")