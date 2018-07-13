# -*- coding=utf-8 -*-

"""
处理文书正文中原告被告信息
"""

from logs.mylog import flogger


def first_round_plaintiff(content_list, index=0):
    """ 解析一审原告信息

    :param content_list list 内容列表
    :param index int 开始读取数据的索引

    res = {
        "plaintiff" : [
            "原告：广发银行股份有限公司广州分行，住所地广州市天河区珠江新城临江大道57号南雅中和广场首层、24-28层，统一社会信用代码：91440101890476659Y。",
            ""
        ],
        "procurator" : [
            "",
            ""
        ],
        "agency" : [
            "",
            ""
        ]
    }
    """

    new_index = 0
    res = {
        "plaintiff"   : [],       # 原告
        "plaintiff_procurator"  : [],       # 代理律师
        "plaintiff_agency"      : []        # 代理律所
    }

    for foo in content_list[index:]:
        if not foo.text:
            new_index += 1
            continue

        bar = foo.text
        if bar.startswith("原告"):
            res["plaintiff"].append(bar)
        elif bar.startswith("委托"):
            if "律师" in bar:
                res["plaintiff_procurator"].append(bar)
            else:
                res["plaintiff_agency"].append(bar)
        elif bar.startswith("被告"):
            break

        new_index += 1

    flogger.info(res)
    flogger.info("index: {}".format(new_index))
    return res, new_index


def first_round_defendant(content_list, index):
    """ 解析一审被告信息

    :param content_list list 内容列表
    :param index int 开始读取数据的索引

    res = {
        "defendant" : [
            {
                "title" : "被告：付玉林，男，1986年7月25日出生，汉族，住福建省漳平市。",
                "stype" : "个人"
            }
            {}
        ],
        "procurator" : [
            "",
            ""
        ],
        "agency" : [
            "",
            ""
        ]
    }
    """

    new_index = 0
    res = {
        "defendant"   : [],       # 原告
        "defendant_procurator"  : [],       # 代理律师
        "defendant_agency"      : []        # 代理律所
    }

    for foo in content_list[index:]:

        if not foo.text:
            new_index += 1
            continue

        bar = foo.text

        if "审查" in bar or "审理" in bar:
            break

        if bar.startswith("被告"):
            you = {"title" : bar, "stype" : "公司"}
            if ("族" in bar or "出生" in bar) and ("男" in bar or "女" in bar): you["stype"] = "个人"
            res["defendant"].append(you)
        elif bar.startswith("委托"):
            if "律师" in bar:
                res["defendant_procurator"].append(bar)
            else:
                res["defendant_agency"].append(bar)
        else:
            pass

        new_index += 1

    flogger.info(res)
    return res, new_index


def second_round_plaintiff(content_list):
    """ 解析二审原告信息

    :param content_list list 原告等信息

    res = {
        "appellant" : [
            {
                "title" : "上诉人（原审原告）：中国银行股份有限公司福州华林路支行，住所地福建省福州市鼓楼区华林路242号一层08号店面，统一社会信用代码9135010079378254VY。",
                "stype" : "个人"/"公司"
            }
        ],
        "appellee" : [
            {
                "title" : "上诉人（原审原告）：中国银行股份有限公司福州华林路支行，住所地福建省福州市鼓楼区华林路242号一层08号店面，统一社会信用代码9135010079378254VY。",
                "stype" : "个人"/"公司"
            }
        ],
        "plaintiff_original" : [
            {
                "title" : "上诉人（原审原告）：中国银行股份有限公司福州华林路支行，住所地福建省福州市鼓楼区华林路242号一层08号店面，统一社会信用代码9135010079378254VY。",
                "stype" : "个人"/"公司"
            }
        ],
        "defendant_original" : [
            {
                "title" : "上诉人（原审原告）：中国银行股份有限公司福州华林路支行，住所地福建省福州市鼓楼区华林路242号一层08号店面，统一社会信用代码9135010079378254VY。",
                "stype" : "个人"/"公司"
            }
        ],
        "appellant_law_agency" :[
            {
                "title" : "委托诉讼代理人：李立成，北京市闻泽律师事务所律师",
                "stype" : "个人"/"公司"
            },
            {
                "title" : "委托诉讼代理人：王绪，男，该分行工作人员。",
                "stype" : "个人"/"公司"
            }
        ],
        "appellee_law_agency" :[
            {
                "title" : "委托诉讼代理人：李立成，北京市闻泽律师事务所律师",
                "stype" : "个人"/"公司"
            },
            {
                "title" : "委托诉讼代理人：王绪，男，该分行工作人员。",
                "stype" : "个人"/"公司"
            }
        ]
    }
    """

    agency_type = "appellant"    # 代理类型，是上诉人代理还是被上诉人代理

    res = {
        "appellant"            : [],  # 上诉人
        "appellee"             : [],  # 被上诉人
        "plaintiff_original"   : [],  # 原审原告
        "defendant_original"   : [],  # 原审被告
        "appellant_law_agency" : {"procurator":[], "agency":[]},  # 上诉人委托代理
        "appellee_law_agency"  : {"procurator":[], "agency":[]}   # 被上诉人委托代理
    }

    for foo in content_list:

        if not foo.text:
            continue

        bar = foo.text

        if "审查" in bar or "审理" in bar:
            break

        if bar.startswith("上诉人（原审被告）"):
            you = {"title" : bar, "stype" : "公司"}
            if ("族" in bar or "出生" in bar) and ("男" in bar or "女" in bar): you["stype"] = "个人"
            res["appellant"].append(you)
        if bar.startswith("上诉人（原审原告）"):
            you = {"title" : bar, "stype" : "公司"}
            if ("族" in bar or "出生" in bar) and ("男" in bar or "女" in bar): you["stype"] = "个人"
            res["appellant"].append(you)
        elif bar.startswith("被上诉人（原审原告）"):
            agency_type = "appellee"
            you = {"title" : bar, "stype" : "公司"}
            if ("族" in bar or "出生" in bar) and ("男" in bar or "女" in bar): you["stype"] = "个人"
            res["appellee"].append(you)
        elif bar.startswith("被上诉人（原审被告）"):
            agency_type = "appellee"
            you = {"title" : bar, "stype" : "公司"}
            if ("族" in bar or "出生" in bar) and ("男" in bar or "女" in bar): you["stype"] = "个人"
            res["appellee"].append(you)
        elif bar.startswith("原审原告"):
            you = {"title" : bar, "stype" : "公司"}
            if ("族" in bar or "出生" in bar) and ("男" in bar or "女" in bar): you["stype"] = "个人"
            res["plaintiff_original"].append(you)
        elif bar.startswith("原审被告"):
            you = {"title" : bar, "stype" : "公司"}
            if ("族" in bar or "出生" in bar) and ("男" in bar or "女" in bar): you["stype"] = "个人"
            res["defendant_original"].append(you)
        elif bar.startswith("委托"):
            if agency_type == "appellant":
                if "律师" in bar:
                    res["appellant_law_agency"]["procurator"].append(bar)
                else:
                    res["appellant_law_agency"]["agency"].append(bar)
            else:
                if "律师" in bar:
                    res["appellee_law_agency"]["procurator"].append(bar)
                else:
                    res["appellee_law_agency"]["agency"].append(bar)
        else:
            pass

    flogger.info(res)
    return res


def extract_executor_info(content_list):
    """ 解析 执行人 等信息 """

    agency_type = "executor"    # 代理类型，是执行人代理还是被执行人代理

    res = {
        "executor"            : [],  # 执行人
        "executed"             : [],  # 被执行人
        "executor_law_agency" : {"procurator":[], "agency":[]},  # 执行人委托代理
        "executed_law_agency"  : {"procurator":[], "agency":[]}   # 被执行人委托代理
    }

    for foo in content_list:

        if not foo.text:
            continue

        bar = foo.text

        if "审查" in bar or "审理" in bar:
            break

        if bar.startswith("申请执行人"):
            you = {"title" : bar, "stype" : "公司"}
            if ("族" in bar or "出生" in bar) and ("男" in bar or "女" in bar): you["stype"] = "个人"
            res["executor"].append(you)
        elif bar.startswith("被执行人"):
            agency_type = "executed"
            you = {"title" : bar, "stype" : "公司"}
            if ("族" in bar or "出生" in bar) and ("男" in bar or "女" in bar): you["stype"] = "个人"
            res["executed"].append(you)
        elif bar.startswith("委托"):
            if agency_type == "executor":
                if "律师" in bar:
                    res["executor_law_agency"]["procurator"].append(bar)
                else:
                    res["executor_law_agency"]["agency"].append(bar)
            else:
                if "律师" in bar:
                    res["executed_law_agency"]["procurator"].append(bar)
                else:
                    res["executed_law_agency"]["agency"].append(bar)
        else:
            pass

    print(res)
    return res


def main():

    content_list = ["上诉人（原审被告）：王全辉，男，1969年9月12日出生，汉族，住广东省佛山市南海区。",
        "被上诉人（原审原告）：渣打银行（中国）有限公司佛山分行，住所地广东省佛山市南海区。",
        "负责人：岑卫明，该行行长。",
        "原审被告：佛山市中铭电子实业有限公司，住所地广东省佛山市南海区。",
        "法定代表人：王全辉。",
        "原审被告：王晓梅，女，1982年5月4日出生，汉族，住广东省佛山市南海区。",
        "上诉人王全辉因与被上诉人渣打银行（中国）有限公司佛山分行、原审被告佛山市中铭电子实业有限公司、王晓梅金融借款合同纠纷一案，不服广东省佛山市南海区人民法院（2017）粤0605民初16214号之一民事裁定，向本院提出上诉。",
        "上诉人上诉称，被上诉人向法院提交的《渣打银行中小企业无抵押小额贷款条款和条件》没有被上诉人的签章，故该《渣打银行中小企业无抵押小额贷款条款和条件》尚未生效，其中关于约定管辖的第15条无效。又因被上诉人具有涉外因素，故本案应由广东省佛山市中级人民法院管辖。现上诉请求二审法院撤销原审裁定，裁定将本案移送广东省佛山市中级人民法院审理。"
    ]

    second_round_plaintiff(content_list)

if __name__ == "__main__":
    main()