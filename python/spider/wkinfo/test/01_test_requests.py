# -*- coding=utf-8 -*-
# Created Time: 2018年06月25日 星期一 14时11分59秒
# File Name: 01_test_requests.py

import requests

url = "http://law.wkinfo.com.cn/csi/document/MjAyMzcwMDI4Mjk=?indexId=law.case"

headers = {'cookie': 'connect.sid=s%3AONEUgu7J16GVGyvPoQZ1_gy973b65KnB.GNClzUB3LSmSpITOAY5M2DhaGWBWlslmVaJZu9qB2W8; TY_SESSION_ID=1526e6ad-95fc-4b03-a58e-cc28aa336ca4; CCKF_visitor_id_100847=1099568108; cckf_track_100847_AutoInviteNumber=0; cckf_track_100847_ManualInviteNumber=0; userConfig=%7B%22moduleList%22%3A%5B%5D%2C%22userStaffType%22%3A1%2C%22isIpUser%22%3A0%2C%22parentId%22%3A0%2C%22sourceSiteUrl%22%3Anull%2C%22sourceSiteName%22%3Anull%2C%22clientSource%22%3A%22%E8%87%AA%E4%B8%BB%E6%B3%A8%E5%86%8CV4%E6%94%AF%E4%BB%98%22%2C%22trial%22%3Afalse%7D; autologin=true; username=lhjk; userInfo=%7B%22id%22%3A%22%22%2C%22username%22%3A%22lhjk%22%2C%22password%22%3A%220x0100000047d3ade62988311a4175867effd2e65372c3bb73c79af56a%22%2C%22email%22%3A%22hongyx%40lhjk.com.cn%22%2C%22userLang%22%3A%22cn%22%2C%22userPageSize%22%3A25%2C%22isSend%22%3Atrue%2C%22sendLang%22%3A%22cn-en%22%2C%22recieveEmails%22%3A%5B%5D%2C%22userType%22%3A%22normal%22%2C%22groupName%22%3A%22law%22%2C%22libraryCode%22%3A%22%22%2C%22licences%22%3A1%2C%22telephone%22%3A%2213537741106%22%2C%22conf%22%3A%22%7B%5C%22legislationViewType%5C%22%3A%5C%22group%5C%22%2C%5C%22lawExpressViewType%5C%22%3A%5C%22list%5C%22%2C%5C%22mLegislationViewType%5C%22%3A%5C%22list%5C%22%2C%5C%22mLawExpressViewType%5C%22%3A%5C%22list%5C%22%7D%22%7D; loginId=db149f8395704a2b86f08ee34ac9904f; cckf_track_100847_LastActiveTime=1529906296'}

r = requests.get(url, headers=headers)

print(r.text)
