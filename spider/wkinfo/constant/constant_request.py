# -*- coding: utf-8 -*-

"""
抓取用常量
"""

class RequestConstant(object):

    # USERINFO = {"username": "wawa__huahua@163.com", "password": ""} # 18109044347
    USERINFO = {"username": "b__white@163.com", "password": ""}
    # USERINFO = {"username": "lhjk", "password": ""}

    # 登录链接
    LOGIN_URL = "https://m.law.wkinfo.com.cn/csi/account/validate/ex"

    # 搜索链接
    # SEARCH_URL = "http://law.wkinfo.com.cn/csi/search"
    SEARCH_URL = "https://m.law.wkinfo.com.cn/csi/search"

    # 获取结果树链接
    # GET_RESULT_TREE_URL = "http://law.wkinfo.com.cn/csi/filtertree/court?searchId={}"
    GET_RESULT_TREE_URL = "https://m.law.wkinfo.com.cn/csi/filtertree/court?searchId={}"

    # 获取文书 header 链接
    # GET_DOC_HEADER_URL = "http://m.law.wkinfo.com.cn/csi/document/{}?indexId=law.case"
    GET_DOC_HEADER_URL = "https://m.law.wkinfo.com.cn/csi/document/{}?indexId=law.case"

    # 获取文书 body 链接
    # GET_DOC_BODY_URL = "http://m.law.wkinfo.com.cn/csi/document/{}/html?indexId=law.case&print=false&fromType=null&useBalance=true"

    GET_DOC_BODY_URL = "https://m.law.wkinfo.com.cn/csi/document/{}/html?indexId=law.case&print=false&fromType=null&useBalance=true"

    HEADERS = {
            'cookie': 'connect.sid=s%3A05bROq1cbexY-wctGGFjt6PDI_SMk0yk.ohZ%2Bix2R%2Be91YaKNyg1UxAT7AAkpn0Ylg8rlfLoNK5c; Path=/; Expires=Thu, 05 Jul 2018 02:55:49 GMT; HttpOnly'
    }

    # 检测条数用的offset
    OFFSET_TEST_COUNT = 0

    # 获取数据用的offset
    OFFSET_GET_DATA = 100

    # 当前账户结果条数限制
    RESULT_LIMIT = 5000

    # web请求超时
    REQUEST_TIMEOUT = 18

    SEARCH_PARAMS = {
        "indexId": "law.case",
        "query": {
            # "queryString": " (( causeOfAction:01000000000000民事/01040000000000合同、无因管理、不当得利纠纷/01040010000000合同纠纷/01040010240000借款合同纠纷/01040010240010金融借款合同纠纷 )) ",
            "queryString" : "",
            "filterQueries": [],
            "filterDates": [
                # "judgmentDate:[2018.06.02 TO 2018.06.02]"
            ]
        },
        "searchScope": {
            "treeNodeIds": [
                # "courtǁ003000000北京市/002040000北京市第二中级人民法院辖区ǁǂ"
            ]
        },
        "relatedIndexQueries": [],
        "sortOrderList": [
            {
                "sortKey": "judgmentDate",
                "sortDirection": "DESC"
            }
        ],
        "pageInfo": {
            "limit": 100,
            "offset": 0
        },
        "otherOptions": {
            "requireLanguage": "cn",
            "relatedIndexEnabled": False,
            "groupEnabled": False,
            "smartEnabled": True,
            "buy": False,
            "summaryLengthLimit": 100,
            "advanced": True,
            "synonymEnabled": True,
            "isHideBigLib": 0
        },
        "chargingInfo": {
            "useBalance": True
        }
    }
