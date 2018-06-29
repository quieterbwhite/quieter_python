# -*- coding=utf-8 -*-
# Created Time: 2018年06月25日 星期一 14时11分59秒
# File Name: 03_test_get_list.py

import time
import requests
from service_mongo import mongo_service

url = "http://law.wkinfo.com.cn/csi/search"

headers = {'cookie': 'CCKF_visitor_id_100847=1099568108; userConfig=%7B%22moduleList%22%3A%5B%5D%2C%22userStaffType%22%3A1%2C%22isIpUser%22%3A0%2C%22parentId%22%3A0%2C%22sourceSiteUrl%22%3Anull%2C%22sourceSiteName%22%3Anull%2C%22clientSource%22%3A%22%E8%87%AA%E4%B8%BB%E6%B3%A8%E5%86%8CV4%E6%94%AF%E4%BB%98%22%2C%22trial%22%3Afalse%7D; autologin=true; username=lhjk; UM_distinctid=164359bc635fbd-0d3c41f654f7f-3a760e5d-1fa400-164359bc636d97; CNZZDATA1261306096=1809375088-1529906399-%7C1529906399; Hm_lvt_fecce484974a74c6d10f421b6d3bd395=1529907759; userInfo=%7B%22username%22%3A%22lhjk%22%2C%22password%22%3A%220x0100000047d3ade62988311a4175867effd2e65372c3bb73c79af56a%22%2C%22email%22%3A%22hongyx%40lhjk.com.cn%22%2C%22groupName%22%3A%22law%22%2C%22libraryCode%22%3A%22%22%2C%22userLang%22%3A%22cn%22%2C%22userPageSize%22%3A25%2C%22isSend%22%3Atrue%2C%22sendLang%22%3A%22cn-en%22%2C%22recieveEmails%22%3A%5B%5D%2C%22userType%22%3A%22normal%22%2C%22licences%22%3A1%2C%22telephone%22%3A%2213537741106%22%2C%22conf%22%3A%22%22%2C%22moduleList%22%3A%5B%5D%2C%22userStaffType%22%3A1%2C%22parentId%22%3A0%2C%22isIpUser%22%3A0%2C%22sourceSiteUrl%22%3Anull%2C%22sourceSiteName%22%3Anull%2C%22clientSource%22%3A%22%E8%87%AA%E4%B8%BB%E6%B3%A8%E5%86%8CV4%E6%94%AF%E4%BB%98%22%2C%22trial%22%3Afalse%7D; loginin=true; connect.sid=s%3An1kzkCsgCvu__vnm-BMTuZLpRWKxA4Ek.B3Tv4LjhN7H6cMXiZHvn6G5HGzzSUL3tOFS8Xr7vFhs; TY_SESSION_ID=434dd123-90f7-4f45-81f2-c5cd91599265; check=valid; loginId=2e92a05e34234afc8dc7eeb83e5c0509; cckf_track_100847_AutoInviteNumber=0; cckf_track_100847_ManualInviteNumber=0; columnconfig_judgment-documents=%7B%22showAbstract%22%3A%22false%22%2C%22isListView%22%3A%22true%22%2C%22mod%22%3A%22%22%7D; cckf_track_100847_LastActiveTime=1530253392; column-maxsize=100'}

payload = {
    "indexId": "law.case",
    "query": {
        "queryString": " (( causeOfAction:01000000000000民事/01040000000000合同、无因管理、不当得利纠纷/01040010000000合同纠纷/01040010240000借款合同纠纷/01040010240010金融借款合同纠纷 )) ",
        "filterQueries": [],
        "filterDates": [
            "judgmentDate:[2018.06.01 TO 2018.06.01]"
        ]
    },
    "searchScope": {
        "treeNodeIds": []
    },
    "relatedIndexQueries": [],
    "sortOrderList": [
        {
            "sortKey": "judgmentDate",
            "sortDirection": "DESC"
        }
    ],
    "pageInfo": {
        "limit": "100",
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

judgements_conn = mongo_service.get_collection("wk01")

for i in range(2):
    time.sleep(5)
    print "Going to page: {}".format(i)
    payload["pageInfo"].update({"offset":i*100})
    r = requests.post(url, headers=headers, json=payload)
    if not r:
        print "No Results"
        break
    
    print "Save me"
    data = r.json()
    docCount = data["searchMetadata"]["docCount"]
    if docCount > 5000:
        
        break
    
    documentList = data["documentList"]
    for doc in documentList:
        # judgements_conn.insert(doc)
        pass
        
print "All Done"
    
