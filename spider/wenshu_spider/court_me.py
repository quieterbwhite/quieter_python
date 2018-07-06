# encoding:utf-8

import time
from urllib import parse

import execjs
import requests
import simplejson
from service_mongo import mongo_service

session = requests.Session()

def get_guid():
    # 获取guid参数

    js1 = '''
		function getGuid() {
	        var guid = createGuid() + createGuid() + "-" + createGuid() + "-" + createGuid() + createGuid() + "-" + createGuid() + createGuid() + createGuid(); //CreateGuid();
	       	return guid;
	    }
	    var createGuid = function () {
	        return (((1 + Math.random()) * 0x10000) | 0).toString(16).substring(1);
	    }
	'''
    ctx1 = execjs.compile(js1)
    guid = (ctx1.call("getGuid"))
    print("Got guid: %s" % guid)
    return guid


def get_number(guid):
    ###获取number

    codeUrl = "http://wenshu.court.gov.cn/ValiCode/GetCode"
    data = {
        'guid': guid
    }
    headers = {
        'Host': 'wenshu.court.gov.cn',
        'Origin': 'http://wenshu.court.gov.cn',
        'Referer': 'http://wenshu.court.gov.cn/',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
    }
    try:
        req1 = session.post(codeUrl, data=data, headers=headers, timeout=20)
    except Exception as e:
        print(e.message)
        return "timeout"

    number = req1.text
    print("Got number: %s" % number)
    return number


def get_vjkl5(guid, number, Param):
    ####获取cookie中的vjkl5
    url1 = "http://wenshu.court.gov.cn/list/list/?sorttype=1&number=" + number + "&guid=" + guid + "&conditions=searchWord+QWJS+++" + parse.quote(
        Param)

    headers1 = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Host": "wenshu.court.gov.cn",
        "Proxy-Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36"
    }
    try:
        req1 = session.get(url=url1, headers=headers1, timeout=20)
    except Exception as e:
        print(e.message)
        return "timeout"

    try:
        vjkl5 = req1.cookies["vjkl5"]
        print("Got vjkl5: %s" % vjkl5)
        return vjkl5
    except:
        return get_vjkl5(guid, number, Param)


def get_vl5x(vjkl5):
    # 根据vjkl5获取参数vl5x
    js = ""
    fp1 = open('./sha1.js')
    js += fp1.read()
    fp1.close()
    fp2 = open('./md5.js')
    js += fp2.read()
    fp2.close()
    fp3 = open('./base64.js')
    js += fp3.read()
    fp3.close()
    fp4 = open('./vl5x.js')
    js += fp4.read()
    fp4.close()
    ctx2 = execjs.compile(js)
    vl5x = (ctx2.call('vl5x', vjkl5))
    return vl5x


def get_data(Param, Index, Page, Order, Direction):

    print("Going to page: %s" % Index)
    guid = get_guid()

    number = get_number(guid)
    if number == "timeout": return "exception"

    vjkl5 = get_vjkl5(guid, number, Param)
    if vjkl5 == "timeout": return "exception"

    vl5x = get_vl5x(vjkl5)

    # 获取数据
    url2 = "http://wenshu.court.gov.cn/List/ListContent"
    headers2 = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Host": "wenshu.court.gov.cn",
        "Origin": "http://wenshu.court.gov.cn",
        "Proxy-Connection": "keep-alive",
        # "Referer":Referer1,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }
    data = {
        "Param": Param,
        "Index": Index,
        "Page": Page,
        "Order": Order,
        "Direction": Direction,
        "vl5x": vl5x,
        "number": number,
        "guid": guid
    }
    try:
        req2 = session.post(url=url2, headers=headers2, params=data, timeout=20)
    except Exception as e:
        print(e.message)
        return "exception"

    data = req2.text
    # print(data)
    print("type of data: %s" % type(data))
    print("length of data: %s" % len(data))

    if "remind" in data:
        print(data)
        print("Last Page, No more data here")
        return None

    data_list = eval(simplejson.loads(data))
    print("type of data_list: %s" % type(data_list))
    # print(data_list)

    data_list_len = len(data_list)
    print("Length of data_list: %s" % data_list_len)
    if data_list_len <= 1:
        print("No more data..")
        return None

    return data_list[1:]


def process(start_date, end_date, index):
    # 搜索条件

    Param = "案由:金融借款合同纠纷,裁判日期:{} TO {}".format(start_date, end_date)
    Page = 20  # 每页几条
    Order = "法院层级"  # 排序标准
    Direction = "asc"  # asc正序 desc倒序

    data_list = get_data(Param, index, Page, Order, Direction)
    return data_list


def main():

    start_time = int(time.time())

    judgements_conn = mongo_service.get_collection("judgements_2018_01_07")
    start_date = "2018-01-01"
    end_date = "2018-06-28"
    index = 1

    while True:
        data_list = process(start_date, end_date, index)
        if not data_list:
            break

        if data_list == "exception":
            print("Exception continue")
            continue

        print("Gotcha Bitch.")
        for data in data_list:
            # print(data)
            judgements_conn.insert(data)

        time.sleep(10)
        index += 1

    end_time = int(time.time())

    print("Costs: %s seconds." % (end_time - start_time))


if __name__ == '__main__':
    main()
