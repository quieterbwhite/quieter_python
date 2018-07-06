# -*- coding=utf-8 -*-
# Created Time: 2018年07月06日 星期五 10时01分28秒
# File Name: download.py

import requests


def download(conditions, docids):
    """  """

    url = "http://wenshu.court.gov.cn/CreateContentJS/CreateListDocZip.aspx?action=1"
    payload = {
        "conditions" : conditions,
        "docIds" : docids
    }

    headers = {
        "Content-Type" : "application/x-www-form-urlencoded",
        "Accept"       : "*/*",
        "Accept-Encoding" : "gzip, deflate",
        "Accept-Language" : "zh-CN,zh;q=0.9,en;q=0.8",
        "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
    }

    res = requests.post(url, headers=headers, data=payload, timeout=20)

    #print(res.text)

    with open("./{}.zip".format(conditions), "wb") as sfile:
        sfile.write(res.content)

def main():

    conditions = "案由为金融借款合同纠纷且裁判日期为2018-07-03 TO 2018-07-03"
    docids = "71bba864-2864-4bad-b18a-a914009ea9a1|秦渝、中国银行股份有限公司郑州新区支行金融借款合同纠纷再审审查与审判监督民事裁定书|2018-07-03,59a4e000-46b4-4205-93d5-a913009227f0|中国邮政储蓄银行股份有限公司张家港市支行与陈婷、赵宾金融借款合同纠纷一审民事裁定书|2018-07-03,f8688662-4201-48ef-95c3-a9140010bfc3|隆化县农村信用合作联社与贾玉芝、黄学生金融借款合同纠纷一审民事裁定书|2018-07-03"

    download(conditions, docids)

if __name__ == "__main__":
    main()
