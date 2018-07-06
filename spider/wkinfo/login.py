# -*- coding=utf-8 -*-

"""
登录
"""

from constant.constant_request import RequestConstant
from common import request_login
from logs.mylog import flogger

import requests
import time


def get_new_session():
    """ 获取新的 session.  """

    flogger.info("获取新的 session. ")
    session = requests.Session()
    login_wk(session)
    flogger.info("成功获取到新的 session. ")
    return session


def login_wk(session):

    while 1:

        flogger.info("尝试登录...")
        user_data = request_login(session, RequestConstant.LOGIN_URL, payload=RequestConstant.USERINFO)

        if user_data == "Exception":
            flogger.info("登录失败 :( , 继续尝试登录..60s.")
            time.sleep(60)
            continue
        elif user_data == "no_user_available":
            flogger.info("暂时没有可用用户..等待继续尝试. 60s")
            time.sleep(180)
            continue
        elif user_data == "relogin":
            flogger.info("登录过期需要重新登录..60s")
            time.sleep(60)
            continue
        else:
            if user_data["userName"] == RequestConstant.USERINFO["username"]:
                flogger.info("登录成功 :)")
            break


"""
{'code': 'C_001_012', 'message': '当前用户被限制访问，初级警告'}

{'code': 'C_001_014', 'message': '当前用户所有接口被限制访问'}

{'code': 'C_001_004', 'message': '防盗采：用户分钟超标'}

{"code": "C_002_001", "message": "用户并发超标"}

{
    "userName":"b__white@163.com",
    "bold_user":null,
    "createTime":1530670129497,
    "operatorId":null,
    "telephone":"15202897835",
    "libraryCode":"",
    "approvalId":null,
    "errorFlag":0,
    "userEmail":"b__white@163.com",
    "ipaddressFirst":"",
    "zipCode":null,
    "deleteFlag":0,
    "firstName":"-",
    "group":"2",
    "activeFlag":1,
    "corpBinding":false,
    "industryId":null,
    "siteSourceCode":null,
    "moduleList":[],
    "post":null,
    "saleInfo":"[]",
    "corp":false,
    "gender":null,
    "shipTo":null,
    "companySizeId":null,
    "companyName":"\u6210\u90fd\u79be\u4e91\u4fe1\u606f\u6280\u672f\u6709\u9650\u516c\u53f8",
    "parentId":0,
    "sourceSiteUrl":null,
    "clientSource":"\u81ea\u4e3b\u6ce8\u518c",
    "updateTime":1530670129497,
    "moveBoldUsers":null,
    "needApproval":null,
    "id":"1000117841",
    "lastName":"-",
    "licences":1,
    "companyTypeId":null,
    "userType":0,
    "userProducts":null,
    "currentGroupName":"law",
    "middleName":null,
    "ipaddressLast":"",
    "mailAlertFlag":null,
    "province":null,
    "ship_to":null,
    "sourceSiteName":null,
    "password":"0x01000000f4cbf860476fd789d961454aec9bb074aa1bfdfa10c71208",
    "activeCode":"Qdi4sbwvVPttfBlAiiNqcyku",
    "mailAlertDays":null,
    "address":null,
    "hasLawPermit":true,
    "groupName":"law",
    "department":null,
    "registerFlag":1,
    "isIpUser":0,
    "siteSource":10,
    "code":"01BE01",
    "provinceId":26,
    "trial":true,
    "sendSubUserMail":null
}
"""

