# -*-encoding:utf-8-*-

import requests
from urllib import parse
import execjs
import json
import time
from checkcode import distinguish
import random
import traceback
from search_param import generate_param
from util.date_list import dateRange
from util.service_mongo import mongo_service
from logs.mylog import flogger
from proxy import process

session = requests.Session()

with open('./params_encryption.js') as fp:
    js = fp.read()
    ctx = execjs.compile(js)


def get_guid():

    # # 原始js版本
    # js1 = '''
    #   function getGuid() {
    #         var guid = createGuid() + createGuid() + "-" + createGuid() + "-" + createGuid() + createGuid() + "-" + createGuid() + createGuid() + createGuid(); //CreateGuid();
    #           return guid;
    #     }
    #     var createGuid = function () {
    #         return (((1 + Math.random()) * 0x10000) | 0).toString(16).substring(1);
    #     }
    # '''
    # ctx1 = execjs.compile(js1)
    # guid = (ctx1.call("getGuid"))
    # return guid

    # 翻译成python
    def createGuid():
        return str(hex((int(((1 + random.random()) * 0x10000)) | 0)))[3:]

    return '{}{}-{}-{}{}-{}{}{}' \
        .format(
        createGuid(), createGuid(),
        createGuid(), createGuid(),
        createGuid(), createGuid(),
        createGuid(), createGuid()
    )


def get_number(guid):

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
    while 1:
        time.sleep(1)
        flogger.info("GETTING-NUMBER")
        try:
            req1 = session.post(codeUrl, data=data, headers=headers, timeout=18)
        except Exception as e:
            flogger.info(traceback.format_exc())
            time.sleep(1)
            continue

        flogger.info("GOT-NUMBER!")
        break

    number = req1.text
    return number


def get_vjkl5(guid, number, Param):
    """ 获取cookie中的vjkl5 """

    url1 = "http://wenshu.court.gov.cn/list/list/?sorttype=1&number=" + number + "&guid=" + guid + "&conditions=searchWord+QWJS+++" + parse.quote(Param)

    headers1 = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Host": "wenshu.court.gov.cn",
        "Proxy-Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36"
    }

    while 1:
        time.sleep(1)
        flogger.info("GETTING - vjkl5")
        try:
            req1 = session.get(url=url1, headers=headers1, timeout=18)
        except Exception as e:
            flogger.info(traceback.format_exc())
            time.sleep(1)
            continue

        flogger.info("GOT - vjk15")
        break

    try:
        vjkl5 = req1.cookies["vjkl5"]
        return vjkl5
    except:
        return get_vjkl5(guid, number, Param)


def get_vl5x(vjkl5):
    """ 根据vjkl5获取参数vl5x """

    vl5x = (ctx.call('vl5x', vjkl5))
    return vl5x


def check_code(checkcode='', isFirst=True):  # 是否传入验证码,是否第一次验证码错误
    """
    验证码识别，参数为checkcode和isFirst，用于标识是否为第一次验证码识别，
    第一次识别需要下载验证码，由于文书验证码验证经常出现验证码正确但
    但会验证码错误情况，所以第一次验证码错误时不会下载新的验证码.
    """

    if checkcode == '':
        check_code_url = 'http://wenshu.court.gov.cn/User/ValidateCode'
        headers = {
            'Host': 'wenshu.court.gov.cn',
            'Origin': 'http://wenshu.court.gov.cn',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
        }
        while 1:
            flogger.info("GETTING CHECKCODE IMG...")
            try:
                req = session.get(check_code_url, headers=headers, timeout=18)
            except Exception as e:
                traceback.format_exc()
                time.sleep(1)
                continue

            flogger.info("GOT CHECKCODE IMG")
            break

        fp = open('./checkCode.jpg', 'wb')
        fp.write(req.content)
        fp.close()

        try:
            checkcode = distinguish('checkCode.jpg')
        except Exception as e:
            traceback.format_exc()
            checkcode = "8888"

    flogger.info('识别验证码为：{0}'.format(checkcode))

    check_url = 'http://wenshu.court.gov.cn/Content/CheckVisitCode'
    headers = {
        'Host': 'wenshu.court.gov.cn',
        'Origin': 'http://wenshu.court.gov.cn',
        'Referer': 'http://wenshu.court.gov.cn/Html_Pages/VisitRemind.html',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
    }
    data = {'ValidateCode': checkcode}
    try:
        req = session.post(check_url, data=data, headers=headers, timeout=18)
    except Exception as e:
        flogger.info(traceback.format_exc())
        check_code(checkcode, False)

    if req.text == '2':
        flogger.info('验证码错误')
        if isFirst:
            check_code(checkcode, False)
        else:
            check_code()


def get_tree_content(Param):
    """ 获取左侧类目分类 """

    guid = get_guid()
    number = get_number(guid)
    vjkl5 = get_vjkl5(guid, number, Param)
    vl5x = get_vl5x(vjkl5)
    url = 'http://wenshu.court.gov.cn/List/TreeContent'
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Host": "wenshu.court.gov.cn",
        "Origin": "http://wenshu.court.gov.cn",
        "Proxy-Connection": "keep-alive",
        "Referer": "http://wenshu.court.gov.cn/list/list/?sorttype=1&number={0}&guid={1}&conditions=searchWord+QWJS+++{2}".format(
            number, guid, parse.quote(Param)),
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }
    data = {
        "Param": Param,
        "vl5x": vl5x,
        "number": number,
        "guid": guid
    }

    while 1:
        flogger.info("GETTING TREE CONTENT...")
        try:
            req = session.post(url, headers=headers, data=data)
        except Exception as e:
            flogger.info(traceback.format_exc())
            time.sleep(1)
            continue

        flogger.info("GOT TREE CONTENT")
        break

    json_data = json.loads(req.text.replace('\\', '').replace('"[', '[').replace(']"', ']'))
    tree_dict = {}
    for type_data in json_data:
        type_name = type_data['Key']
        type_dict = {
            'IntValue': type_data['IntValue'],
            'ParamList': []
        }
        for data in type_data['Child']:
            if data['IntValue']:
                type_dict['ParamList'].append({'Key': data['Key'], 'IntValue': data['IntValue']})
        tree_dict[type_name] = type_dict
    return tree_dict


def get_data(Param, Page, Order, Direction, the_date):

    Index = 1  # 第几页

    guid = get_guid()
    number = get_number(guid)
    vjkl5 = get_vjkl5(guid, number, Param)
    vl5x = get_vl5x(vjkl5)

    while (True):

        time.sleep(4)

        flogger.info('{} ###### 第{}页 ######'.format(the_date, Index))

        # 获取数据
        url = "http://wenshu.court.gov.cn/List/ListContent"
        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Host": "wenshu.court.gov.cn",
            "Origin": "http://wenshu.court.gov.cn",
            "Proxy-Connection": "keep-alive",
            "Referer": "http://wenshu.court.gov.cn/list/list/?sorttype=1&number={0}&guid={1}&conditions=searchWord+QWJS+++{2}".format(
                number, guid, parse.quote(Param)),
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
        }
        # flogger.info(headers["Referer"])
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

        proxy = process()
        flogger.info(proxy)
        try:
            req = session.post(url, headers=headers, data=data, timeout=20, proxies=proxy)
            # req = session.post(url, headers=headers, data=data, timeout=20)
        except requests.ReadTimeout as e:
            flogger.info(traceback.format_exc())
        except requests.exceptions.InvalidHeader as e:
            flogger.info(traceback.format_exc())
        except Exception as e:
            flogger.info(traceback.format_exc())
            guid = get_guid()
            number = get_number(guid)
            continue

        req.encoding = 'utf-8'
        return_data = req.text.replace('\\', '').replace('"[', '[').replace(']"', ']')

        if "remind" in return_data:
            flogger.info('出现验证码')

            check_code()

            guid = get_guid()

            number = get_number(guid)
        else:
            # [{'Count': '721'}]
            json_data = json.loads(return_data)

            count = json_data[0]["Count"]
            flogger.info("{} - Total Count: {}".format(the_date, count))

            if len(json_data) <= 1:
                flogger.info('{} - 采集完成'.format(the_date))
                break
            else:
                data_list = []
                for i in range(1, len(json_data)):
                    trial_seq   = json_data[i]['审判程序'] if '审判程序' in json_data[i] else ''
                    court       = json_data[i]['法院名称'] if '法院名称' in json_data[i] else ''
                    date        = json_data[i]['裁判日期'] if '裁判日期' in json_data[i] else ''
                    number      = json_data[i]['案号'] if '案号' in json_data[i] else ''
                    non_public  = json_data[i]['不公开理由'] if '不公开理由' in json_data[i] else ''
                    original    = json_data[i]['裁判要旨段原文'] if '裁判要旨段原文' in json_data[i] else ''
                    type        = json_data[i]['案件类型'] if '案件类型' in json_data[i] else ''
                    docid       = json_data[i]['文书ID'] if '文书ID' in json_data[i] else ''
                    name        = json_data[i]['案件名称'] if '案件名称' in json_data[i] else ''

                    data_dict = dict(
                        trial_seq  = trial_seq,
                        court      = court,
                        date       = date,
                        number     = number,
                        non_public = non_public,
                        original   = original,
                        type       = type,
                        docid      = docid,
                        name       = name
                    )
                    data_list.append(data_dict)

                save_data(data_list)

            Index += 1

            guid = get_guid()
            number = get_number(guid)


def save_data(data_list):
    """ 数据存储逻辑 """

    conn_name = "ws201802"
    wenshu_conn = mongo_service.get_collection(conn_name)
    wenshu_conn.insert_many(data_list)
    flogger.info("成功插入数据库")


def getCourtInfo(DocID):
    """ 根据文书DocID获取相关信息：标题、时间、浏览次数、内容等详细信息 """

    return_data = None
    url = 'http://wenshu.court.gov.cn/CreateContentJS/CreateContentJS.aspx?DocID={0}'.format(DocID)
    headers = {
        'Host': 'wenshu.court.gov.cn',
        'Origin': 'http://wenshu.court.gov.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
    }

    for i in range(5):
        try:
            req = session.get(url, headers=headers, timeout=20)
        except requests.ReadTimeout as e:
            flogger.info(traceback.format_exc())
            flogger.info("Timeout Exception - Dont Panic - Situation is under control.")
            time.sleep(3)
            continue
        except Exception as e:
            flogger.info(traceback.format_exc())
            flogger.info("Unknown Exception - Retry...")
            time.sleep(3)
            continue

        req.encoding = 'uttf-8'
        return_data = req.text.replace('\\', '')

        if return_data == "服务不可用。":
            flogger.info("China-Judgements-Online returns 服务不可用。")
            flogger.info("Retry...")
            time.sleep(3)
            continue

        break

    return return_data


def download(DocID):
    """ 根据文书DocID下载doc文档 """

    courtInfo = getCourtInfo(DocID)
    url = 'http://wenshu.court.gov.cn/Content/GetHtml2Word'
    headers = {
        'Host': 'wenshu.court.gov.cn',
        'Origin': 'http://wenshu.court.gov.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
    }
    fp = open('content.html', 'r', encoding='utf-8')
    htmlStr = fp.read()
    fp.close()
    htmlStr = htmlStr.replace('court_title', courtInfo[0]).replace('court_date', courtInfo[1]). \
        replace('read_count', courtInfo[2]).replace('court_content', courtInfo[3])
    htmlName = courtInfo[0]
    data = {
        'htmlStr': parse.quote(htmlStr),
        'htmlName': parse.quote(htmlName),
        'DocID': DocID
    }
    req = session.post(url, headers=headers, data=data)
    filename = './download/{}.doc'.format(htmlName)
    fp = open('{}.doc'.format(htmlName), 'wb')
    fp.write(req.content)
    fp.close()
    flogger.info('"{}"文件下载完成...'.format(filename))


def main():

    start_date = "2018-02-01"
    end_date = "2018-02-10"

    datetime_range_list = dateRange(start_date, end_date)
    flogger.info(datetime_range_list)

    for the_date in datetime_range_list:
        flogger.info(the_date)

        Param, Page, Order, Direction = generate_param(the_date)

        get_data(Param, Page, Order, Direction, the_date)

        time.sleep(5)


if __name__ == '__main__':

    main()
