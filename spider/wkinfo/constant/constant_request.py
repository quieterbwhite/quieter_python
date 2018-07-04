# -*- coding: utf-8 -*-

"""
抓取用常量
"""

class RequestConstant(object):

    # 搜索链接
    SEARCH_URL = "http://law.wkinfo.com.cn/csi/search"

    # 获取结果树链接
    GET_RESULT_TREE_URL = "http://law.wkinfo.com.cn/csi/filtertree/court?searchId={}"

    # 获取文书 header 链接
    # GET_DOC_HEADER_URL = "http://m.law.wkinfo.com.cn/csi/document/{}?indexId=law.case"
    GET_DOC_HEADER_URL = "https://m.law.wkinfo.com.cn/csi/document/{}?indexId=law.case"

    # 获取文书 body 链接
    # GET_DOC_BODY_URL = "http://m.law.wkinfo.com.cn/csi/document/{}/html?indexId=law.case&print=false&fromType=null&useBalance=true"

    GET_DOC_BODY_URL = "https://m.law.wkinfo.com.cn/csi/document/{}/html?indexId=law.case&print=false&fromType=null&useBalance=true"

    HEADERS = {
        'cookie': 'CCKF_visitor_id_100847=1099568108; UM_distinctid=164359bc635fbd-0d3c41f654f7f-3a760e5d-1fa400-164359bc636d97; Hm_lvt_fecce484974a74c6d10f421b6d3bd395=1529907759; TY_SESSION_ID=24764074-0722-451d-af9e-192ee606a6ab; cckf_track_100847_LastActiveTime=1530693403; cckf_track_100847_AutoInviteNumber=0; cckf_track_100847_ManualInviteNumber=0; connect.sid=s%3ATEq1-KiASEFzUzVZbFF-qKOhIt6WgpLk.Ewagp9oyb68RknBFCB%2Bf5NcJJ9Arspk5H0ojgTXRPyw; userConfig=%7B%22moduleList%22%3A%5B%5D%2C%22userStaffType%22%3A0%2C%22isIpUser%22%3A0%2C%22parentId%22%3A0%2C%22sourceSiteUrl%22%3Anull%2C%22sourceSiteName%22%3Anull%2C%22clientSource%22%3A%22%E8%87%AA%E4%B8%BB%E6%B3%A8%E5%86%8C%22%7D; autologin=true; username=b__white%40163.com; loginId=3d47ca6d452f438984b4250524f17a49; userInfo=%7B%22id%22%3A%22%22%2C%22username%22%3A%22b__white%40163.com%22%2C%22password%22%3A%220x01000000f4cbf860476fd789d961454aec9bb074aa1bfdfa10c71208%22%2C%22email%22%3A%22b__white%40163.com%22%2C%22userLang%22%3A%22cn%22%2C%22userPageSize%22%3A25%2C%22isSend%22%3Atrue%2C%22sendLang%22%3A%22cn-en%22%2C%22recieveEmails%22%3A%5B%5D%2C%22userType%22%3A%22normal%22%2C%22groupName%22%3A%22law%22%2C%22libraryCode%22%3A%22%22%2C%22licences%22%3A1%2C%22telephone%22%3A%2215202897835%22%2C%22conf%22%3A%22%7B%5C%22legislationViewType%5C%22%3A%5C%22group%5C%22%2C%5C%22lawExpressViewType%5C%22%3A%5C%22list%5C%22%2C%5C%22mLegislationViewType%5C%22%3A%5C%22list%5C%22%2C%5C%22mLawExpressViewType%5C%22%3A%5C%22list%5C%22%7D%22%7D'
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