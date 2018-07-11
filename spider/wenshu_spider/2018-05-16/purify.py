# -*- coding=utf-8 -*-

"""
处理文书正文中原告被告信息

时间那部分用正则处理还不严谨。不同的文书格式可能不同。
第一版本先这样，已经满足需求方的格式要求。
"""

from logs.mylog import flogger

import re


def extract_program_type(word):
    """ 解析程序类型 """

    if "普通程序" in word: return "普通程序"

    if "简易程序" in word: return "简易程序"

    d = re.findall(r'适用(.*)程序', word)
    if d: return d[0] + "程序"

    return "未知"

def extract_accept_date(word):
    """ 解析 受理日期 用正则"""

    d = re.findall(r'于(.*)日立案', word)
    if d:
        return d[0] + "日"
    else:
        return ""


def extract_exe_date(word):
    """ 解析 立案执行日期 用正则"""

    d = re.findall(r'于(.*)日立案执行', word)
    if d: return d[0] + "日"

    d = re.findall(r'于(.*)日申请执行', word)
    if d: return d[0] + "日"

    d = re.findall(r'于(.*)日申请强制执行', word)
    if d: return d[0] + "日"

    return ""


def extract_hear_date(word):
    """ 解析 审理日期 用正则 """

    d = re.findall(r'于(.*)日公开开庭', word)
    if d:
        return d[0]
    else:
        return ""

def extract_loan_principal(word):
    """ 解析 借款本金 用正则 """

    d = re.findall(r'借款本金([\d\.]*)元', word)
    if d:
        return d
    else:
        return ""

def extract_credit_principal(word):
    """ 解析 贷款本金 用正则 """

    d = re.findall(r'贷款本金([\d\.]*)元', word)
    if d:
        return d
    else:
        return ""

def extract_bar_fee(word):
    """ 解析 律师费 用正则 """

    d = re.findall(r'律师费([\d\.]*)元', word)
    if d:
        return d[0]
    else:
        return ""

def extract_win_over(word):
    """ 解析胜诉情况 有多种描述方法,逐一匹配，哪个最长用哪个

    案件受理费2520元，由原告广发银行股份有限公司广州分行承担170元，由被告陈尚武承担2350元。

    案件受理费2480元，由被告陈王德承担。
    """

    res = ""
    res_len = len(res)

    d = re.findall(r'受理费(.*)[负担,承担]', word)
    if d:
        foo = "本案受理费" + d[0] + "承担"
        if len(foo) >= res_len:
            res = foo
            res_len = len(foo)

    d = re.findall(r'受理费(.*)元。', word)
    if d:
        bar = "本案受理费" + d[0] + "元。"
        if len(bar) >= res_len:
            res = bar
            res_len = len(bar)

    return res


def extract_verdict(word):
    """ 判决或裁决情况 """

    flogger.info("Get verdict info.")
    d = re.findall(r'裁定如下(.*)审　判　长', word)
    if d: return "裁定如下" + d[0]

    d = re.findall(r'判决如下(.*)审　判　长', word)
    if d: return "判决如下" + d[0]

    d = re.findall(r'裁定如下(.*)审判长', word)
    if d: return "裁定如下" + d[0]

    d = re.findall(r'判决如下(.*)审判长', word)
    if d: return "判决如下" + d[0]

    ########

    d = re.findall(r'裁定如下(.*)执　行　长', word)
    if d: return "裁定如下" + d[0]

    d = re.findall(r'判决如下(.*)执　行　长', word)
    if d: return "裁定如下" + d[0]

    d = re.findall(r'裁定如下(.*)执行长', word)
    if d: return "裁定如下" + d[0]

    d = re.findall(r'判决如下(.*)执行长', word)
    if d: return "裁定如下" + d[0]

    return ""

def extract_dispute(word):
    """ 获取争议焦点 """

    d = re.findall(r'争议焦点(.*)。', word)
    if d:
        return "争议焦点" + d[0]
    else:
        return ""

def extract_exe_evidence(word):
    """ 获取执行依据 """

    d = re.findall(r'本院作出的(.*)民事判决', word)
    if d:
        return d[0]
    else:
        return ""


def main():

    s = "本院于2017年1月18日立案受理后"

    b = "于2017年5月4日公开开庭进行了审理"

    c = "你满这帮借款本金24324.4元，气质这么多但不是你们的借款本金998元。"

    print(extract_accept_date(s))

    print(extract_hear_date(b))

    loan_principal = extract_loan_principal(c)
    print(loan_principal)

if __name__ == "__main__":
    main()