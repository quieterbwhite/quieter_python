# -*- coding=utf-8 -*-

"""
解析正文内容
"""

import re
import time
import execjs
import simplejson
import traceback
from pyquery import PyQuery as pq
from util.service_mongo import mongo_service

from shame import (
    first_round_plaintiff,
    first_round_defendant,
    second_round_plaintiff,
    extract_executor_info
)

from purify import (
    extract_accept_date,
    extract_program_type,
    extract_verdict,
    extract_hear_date,
    extract_loan_principal,
    extract_credit_principal,
    extract_bar_fee,
    extract_win_over,
    extract_dispute,
    extract_exe_evidence
)
from constant.detail_constant import DetailConstant
from copy import deepcopy

from logs.mylog import flogger

conn_detail_name = "wsd201801"
conn_detail_a_name = "wsda201801"
wenshu_detail_conn = mongo_service.get_collection(conn_detail_name)
wenshu_detail_a_conn = mongo_service.get_collection(conn_detail_a_name)


def extract(content):
    """ 解析正文内容 """

    res_dict = deepcopy(DetailConstant.res_dict)
    varcaseinfo_res = {}
    trial_date = ""
    dirData_dict = {}
    content_res = {}
    word_res = {}

    res_varcaseinfo = re.findall(r'JSON.stringify\((.*)\);\$\(document', content)
    if res_varcaseinfo:
        varcaseinfo = simplejson.loads(res_varcaseinfo[0])
        varcaseinfo_res = handle_varcaseinfo(varcaseinfo)
        print(varcaseinfo_res)
        res_dict.update(varcaseinfo_res)

    res_dir_data = re.findall(r'dirData = (.*)if', content)
    if res_dir_data:
        flogger.info("got res_dir_data")
        dir_data = res_dir_data[0]

        ctx1 = execjs.compile("dirData=" +dir_data)
        dirData_dict = ctx1.eval("dirData")
        trial_date = handle_dir_data(dirData_dict)

    res_json_html_data = re.findall(r'jsonHtmlData = "(.*)";', content)
    if res_json_html_data:
        flogger.info("got res_json_html_data")
        json_html_data = simplejson.loads(res_json_html_data[0])
        # print(json_html_data)
        html = json_html_data["Html"]
        word = re.sub(r'</?\w+[^>]*>', '', html)
        # print(word)
        word_res = handle_word(res_dict, word)
        content_res = handle_content(res_dict, html)
    else:
        print("no res_json_html_data")

    print("###########")

    res_dict.update(word_res)
    res_dict.update(content_res)
    res_dict.update({"trial_date" : trial_date})

    print(res_dict)
    # wenshu_detail_a_conn.insert(res_dict)


def handle_varcaseinfo(varcaseinfo):
    """ 处理案件基本信息 """

    varcaseinfo_res = {
        "docid"             : varcaseinfo["文书ID"],
        "title"             : varcaseinfo["案件名称"],
        "trial_round"       : varcaseinfo["审判程序"],
        "case_no"           : varcaseinfo["案号"],
        "law_firm"          : varcaseinfo["法院名称"],
        "law_firm_province" : varcaseinfo["法院省份"],
        "law_firm_city"     : varcaseinfo["法院地市"],
        "law_firm_county"   : varcaseinfo["法院区县"]
    }

    return varcaseinfo_res

def handle_dir_data(law_data):
    """ 处理案件涉及的法律法规信息 """

    trial_date = ""
    RelateInfo = law_data["RelateInfo"]
    for i in RelateInfo:
        if i["key"] == "trialDate":
            trial_date = i["value"]

    return trial_date


def handle_word(res_dict, word):
    """ 用正则提取正文内容 """

    flogger.info("用正则提取正文内容")

    accept_date = extract_accept_date(word)
    hear_date = extract_hear_date(word)
    program_type = extract_program_type(word)
    loan_principal = extract_loan_principal(word)
    credit_principal = extract_credit_principal(word)
    bar_fee = extract_bar_fee(word)
    win_over = extract_win_over(word)
    verdict = extract_verdict(word)
    dispute = extract_dispute(word)
    exe_evidence = extract_exe_evidence(word)

    word_res = {
        "accept_date" : accept_date,
        "hear_date" : hear_date,
        "program_type" : program_type,
        "loan_principal" : loan_principal,
        "credit_principal" : credit_principal,
        "bar_fee" : bar_fee,
        "win_over" : win_over,
        "verdict" : verdict,
        "dispute" : dispute,
        "exe_evidence" : exe_evidence
    }

    return word_res


def handle_content(res_dict, html):
    """ 处理这帮犯罪分子 """

    doc = pq(html)
    content_list = doc('div')
    content_res = {}

    print(res_dict["trial_round"])

    if res_dict["trial_round"] == "一审":
        flogger.info("一审案件 - 处理原告被告")
        # 原告
        plaintiff_res, plaintiff_index = first_round_plaintiff(content_list, 0)
        # 被告
        defendant_res, defendant_index = first_round_defendant(content_list, plaintiff_index)

        content_res.update(plaintiff_res)
        content_res.update(defendant_res)

    if res_dict["trial_round"] == "二审":
        flogger.info("二审案件 - 处理上诉人等")
        second_round_res = second_round_plaintiff(content_list)
        content_res.update(second_round_res)

    if "执行裁定书" in res_dict["title"]:
        flogger.info("执行裁定书 - 处理执行人等")
        executor_res = extract_executor_info(content_list)
        content_res.update(executor_res)

    return content_res

def main():

    doc_list = wenshu_detail_conn.find({}).limit(90)
    doc_detail_list = []

    flogger.info("Getting doc id")
    for doc in doc_list:
        doc_detail_list.append(doc)

    index = 0
    for doc in doc_detail_list:
        flogger.info("Going index: {}".format(index))
        try:
            extract(doc["data_flaw"])
        except Exception as e:
            traceback.format_exc()

        time.sleep(2)

def test_one():

    content = """
    
    $(function(){$("#con_llcs").html("浏览：93次")});$(function(){var caseinfo=JSON.stringify({"法院ID":"1290","案件基本情况段原文":"","附加原文":"","审判程序":"二审","案号":"（2018）闽01民终1237号","不公开理由":"","法院地市":"福州市","法院省份":"福建","文本首部段落原文":"","法院区域":"","文书ID":"c6b8457a-b54b-4e9b-a53b-a8d400af6c7e","案件名称":"中国银行股份有限公司福州华林路支行、王浩翔金融借款合同纠纷二审民事裁定书","法院名称":"福建省福州市中级人民法院","裁判要旨段原文":"","法院区县":"","补正文书":"2","DocContent":"","文书全文类型":"1","诉讼记录段原文":"上诉人中国银行股份有限公司福州华林路支行（下称“中行华林路支行”）因与被上诉人王浩翔、福建省华建融资担保有限公司（下称“华建公司”）金融借款合同纠纷一案，不服福建省福州市鼓楼区人民法院（2017）闽0102民初1424号民事裁定，向本院提起上诉。本院于2018年1月8日立案后，依法组成合议庭适用第二审程序进行了审理。本案现已审理终结","判决结果段原文":"","文本尾部原文":"","上传日期":"/Date(1525190400000)/","案件类型":"2","诉讼参与人信息部分原文":"","结案方式":null,"裁判日期":null,"文书类型":null,"效力层级":null});$(document).attr("title","中国银行股份有限公司福州华林路支行、王浩翔金融借款合同纠纷二审民事裁定书");$("#tdSource").html("中国银行股份有限公司福州华林路支行、王浩翔金融借款合同纠纷二审民事裁定书 （2018）闽01民终1237号");$("#hidDocID").val("c6b8457a-b54b-4e9b-a53b-a8d400af6c7e");$("#hidCaseName").val("中国银行股份有限公司福州华林路支行、王浩翔金融借款合同纠纷二审民事裁定书");$("#hidCaseNumber").val("（2018）闽01民终1237号");$("#hidCaseInfo").val(caseinfo);$("#hidCourt").val("福建省福州市中级人民法院");$("#hidCaseType").val("2");$("#HidCourtID").val("1290");$("#hidRequireLogin").val("0");});$(function(){var dirData = {Elements: ["RelateInfo", "LegalBase"],RelateInfo: [{ name: "审理法院", key: "court", value: "福建省福州市中级人民法院" },{ name: "案件类型", key: "caseType", value: "民事案件" },{ name: "案由", key: "reason", value: "金融借款合同纠纷" },{ name: "审理程序", key: "trialRound", value: "二审" },{ name: "裁判日期", key: "trialDate", value: "2018-01-01" },{ name: "当事人", key: "appellor", value: "中国银行股份有限公司福州华林路支行,王浩翔,福建省华建融资担保有限公司" }],LegalBase: [{法规名称:'《中华人民共和国民事诉讼法》',Items:[{法条名称:'第一百七十条',法条内容:'第一百七十条   系统尚未收录或引用有误&amp;#xA;'}]}]};if ($("#divTool_Summary").length > 0) {$("#divTool_Summary").ContentSummary({ data: dirData });}});$(function() {
    var jsonHtmlData = "{"Title":"中国银行股份有限公司福州华林路支行、王浩翔金融借款合同纠纷二审民事裁定书","PubDate":"2018-05-02","Html":"<a type='dir' name='WBSB'></a><div style='TEXT-ALIGN: center; LINE-HEIGHT: 25pt; MARGIN: 0.5pt 0cm; FONT-FAMILY: 宋体; FONT-SIZE: 22pt;'>福建省福州市中级人民法院</div><div style='TEXT-ALIGN: center; LINE-HEIGHT: 30pt; MARGIN: 0.5pt 0cm; FONT-FAMILY: 仿宋; FONT-SIZE: 26pt;'>民 事 裁 定 书</div><div style='TEXT-ALIGN: right; LINE-HEIGHT: 30pt; MARGIN: 0.5pt 0cm;  FONT-FAMILY: 仿宋;FONT-SIZE: 16pt; '>（2018）闽01民终1237号</div><a type='dir' name='DSRXX'></a><div style='LINE-HEIGHT: 25pt;TEXT-ALIGN:justify;TEXT-JUSTIFY:inter-ideograph; TEXT-INDENT: 30pt; MARGIN: 0.5pt 0cm;FONT-FAMILY: 仿宋; FONT-SIZE: 16pt;'>上诉人（原审原告）：中国银行股份有限公司福州华林路支行，住所地福建省福州市鼓楼区华林路242号一层08号店面，统一社会信用代码9135010079378254VY。</div><div style='LINE-HEIGHT: 25pt;TEXT-ALIGN:justify;TEXT-JUSTIFY:inter-ideograph; TEXT-INDENT: 30pt; MARGIN: 0.5pt 0cm;FONT-FAMILY: 仿宋; FONT-SIZE: 16pt;'>主要负责人：翁齐林。</div><div style='LINE-HEIGHT: 25pt;TEXT-ALIGN:justify;TEXT-JUSTIFY:inter-ideograph; TEXT-INDENT: 30pt; MARGIN: 0.5pt 0cm;FONT-FAMILY: 仿宋; FONT-SIZE: 16pt;'>委托诉讼代理人：郁年、严丽清，福建世好律师事务所律师。</div><div style='LINE-HEIGHT: 25pt;TEXT-ALIGN:justify;TEXT-JUSTIFY:inter-ideograph; TEXT-INDENT: 30pt; MARGIN: 0.5pt 0cm;FONT-FAMILY: 仿宋; FONT-SIZE: 16pt;'>被上诉人（原审被告）：王浩翔，男，1991年11月10日出生，汉族，住江西省。</div><div style='LINE-HEIGHT: 25pt;TEXT-ALIGN:justify;TEXT-JUSTIFY:inter-ideograph; TEXT-INDENT: 30pt; MARGIN: 0.5pt 0cm;FONT-FAMILY: 仿宋; FONT-SIZE: 16pt;'>被上诉人（原审被告）：福建省华建融资担保有限公司，住所地福建省福州市鼓楼区五四路252号附属楼4楼A单元，统一社会信用代码91350100681954474H。</div><div style='LINE-HEIGHT: 25pt;TEXT-ALIGN:justify;TEXT-JUSTIFY:inter-ideograph; TEXT-INDENT: 30pt; MARGIN: 0.5pt 0cm;FONT-FAMILY: 仿宋; FONT-SIZE: 16pt;'>法定代表人：施益玲。</div><a type='dir' name='SSJL'></a><div style='LINE-HEIGHT: 25pt;TEXT-ALIGN:justify;TEXT-JUSTIFY:inter-ideograph; TEXT-INDENT: 30pt; MARGIN: 0.5pt 0cm;FONT-FAMILY: 仿宋; FONT-SIZE: 16pt;'>上诉人中国银行股份有限公司福州华林路支行（下称“中行华林路支行”）因与被上诉人王浩翔、福建省华建融资担保有限公司（下称“华建公司”）金融借款合同纠纷一案，不服福建省福州市鼓楼区人民法院（2017）闽0102民初1424号民事裁定，向本院提起上诉。本院于2018年1月8日立案后，依法组成合议庭适用第二审程序进行了审理。本案现已审理终结。</div><a type='dir' name='AJJBQK'></a><div style='LINE-HEIGHT: 25pt;TEXT-ALIGN:justify;TEXT-JUSTIFY:inter-ideograph; TEXT-INDENT: 30pt; MARGIN: 0.5pt 0cm;FONT-FAMILY: 仿宋; FONT-SIZE: 16pt;'>中行华林路支行上诉请求：撤销一审裁定，指令一审法院审理本案。事实与理由：一、双方当事人签订的案涉合同及相关文件，均系当事人真实意思表示，双方之间形成金融借款及担保法律关系。上诉人提起本案诉讼，应属于人民法院受理民事诉讼的范围。二、当事人行为涉嫌经济犯罪，与本案民事纠纷的审理并不冲突相悖，且案涉合同并不存在合同无效法定情形，一审法院适用《关于审理经济纠纷案件中涉及经济犯罪若干问题的规定》第十一条规定裁定驳回上诉人的起诉系适用法律错误。</div><div style='LINE-HEIGHT: 25pt;TEXT-ALIGN:justify;TEXT-JUSTIFY:inter-ideograph; TEXT-INDENT: 30pt; MARGIN: 0.5pt 0cm;FONT-FAMILY: 仿宋; FONT-SIZE: 16pt;'>被上诉人王浩翔、华建公司未作答辩。</div><div style='LINE-HEIGHT: 25pt;TEXT-ALIGN:justify;TEXT-JUSTIFY:inter-ideograph; TEXT-INDENT: 30pt; MARGIN: 0.5pt 0cm;FONT-FAMILY: 仿宋; FONT-SIZE: 16pt;'>中行华林路支行向一审法院起诉请求：1.王浩翔立即偿还中行华林路支行借款本金828800.44元，利息56979.61元、分期付款手续费93000元及滞纳金30274.82元（上述利息暂计至2016年12月29日，该日之后新发生的利息按《信用卡领用合约》约定按日万分之五，按月计收复利标准计算至债务全部清偿之日止）；2.王浩翔赔偿中行华林路支行为实现本案债权所支付的律师代理费用9800元人民币；3.华建公司对王浩翔上述债务承担连带清偿责任；4、判令本案的诉讼费用由王浩翔、福建省华建融资担保有限公司承担。</div><div style='LINE-HEIGHT: 25pt;TEXT-ALIGN:justify;TEXT-JUSTIFY:inter-ideograph; TEXT-INDENT: 30pt; MARGIN: 0.5pt 0cm;FONT-FAMILY: 仿宋; FONT-SIZE: 16pt;'>一审法院认定事实：2017年2月至今，一审法院已累计受理了77件中行华林路支行诉不同个人及华建公司住房装修消费贷款合同纠纷案。其中到庭参加诉讼的当事人均表示其系受华建公司蒙骗以他们个人的名义向中行华林路支行申请住房装修贷款，实际上他们没有该装修项目。信用卡申请、贷款的放发及还款均由华建公司的员工负责，他们只在申请信用卡时签过字，没有收到信用卡，更没有用到所贷款项。包括本案在内所有当事人所借的5000多万元款项均通过POS机刷卡消费的形式转到福建华凯建设工程公司账户。另查：其中有13件案件当事人在向中行华林路支行申请住房装修贷时向该行提供的房产证系伪造的产权证明；其余的64件案件当事人也不是他们向该行提供的住房装修合同中所涉的房屋的产权人或购房人；即一审法院受理的77件借款合同中诉争的个人住房装修项目均为虚构。一审法院认为，包括本案在内的77件系列金融借款合同纠纷案件不属经济纠纷而有经济犯罪嫌疑。根据《最高人民法院关于在审理经济纠纷案件中涉及经济犯罪嫌疑若干问题的规定》第十一条关于“人民法院作为经济纠纷受理的案件，经审理认为不属经济纠纷案件而有经济犯罪嫌疑的，应当裁定驳回起诉，将有关材料移送公安机关或检察机关。”之规定，本案应当移送公安机关处理。裁定：驳回中国银行股份有限公司福州华林路支行的起诉，本案移送公安机关处理。</div><a type='dir' name='CPYZ'></a><div style='LINE-HEIGHT: 25pt;TEXT-ALIGN:justify;TEXT-JUSTIFY:inter-ideograph; TEXT-INDENT: 30pt; MARGIN: 0.5pt 0cm;FONT-FAMILY: 仿宋; FONT-SIZE: 16pt;'>本院认为，本案及类似系列案件中所涉住房装修贷款，相关当事人通过伪造房产证、住房装修合同，虚构个人住房装修项目的方式骗取银行贷款，所涉款项均汇入特定公司账户，涉案金额高达5000余万元，相关当事人的行为已涉嫌骗取贷款或贷款诈骗等经济犯罪。并且，本案当事人在办理案涉贷款过程中是否存在过错及其责任之认定，均与涉嫌经济犯罪的事实密切相关，不能分开独立审理。故原审认定包括本案在内的77件系列案件不属经济纠纷而有经济犯罪嫌疑，并适用《最高人民法院关于在审理经济纠纷案件中涉及经济犯罪嫌疑若干问题的规定》第十一条规定裁定驳回中行华林路支行的起诉并移送公安机关处理，是正确的。综上，依照《中华人民共和国民事诉讼法》第一百七十条第一款第一项的规定，裁定如下：</div><a type='dir' name='PJJG'></a><div style='LINE-HEIGHT: 25pt;TEXT-ALIGN:justify;TEXT-JUSTIFY:inter-ideograph; TEXT-INDENT: 30pt; MARGIN: 0.5pt 0cm;FONT-FAMILY: 仿宋; FONT-SIZE: 16pt;'>驳回上诉，维持原裁定。</div><div style='LINE-HEIGHT: 25pt;TEXT-ALIGN:justify;TEXT-JUSTIFY:inter-ideograph; TEXT-INDENT: 30pt; MARGIN: 0.5pt 0cm;FONT-FAMILY: 仿宋; FONT-SIZE: 16pt;'>本裁定为终审裁定。</div><a type='dir' name='WBWB'></a><div style='TEXT-ALIGN: right; LINE-HEIGHT: 25pt; MARGIN: 0.5pt 72pt 0.5pt 0cm;FONT-FAMILY: 仿宋; FONT-SIZE: 16pt;'>审判长　　陈光卓</div><div style='TEXT-ALIGN: right; LINE-HEIGHT: 25pt; MARGIN: 0.5pt 72pt 0.5pt 0cm;FONT-FAMILY: 仿宋; FONT-SIZE: 16pt;'>审判员　　魏　昀</div><div style='TEXT-ALIGN: right; LINE-HEIGHT: 25pt; MARGIN: 0.5pt 72pt 0.5pt 0cm;FONT-FAMILY: 仿宋; FONT-SIZE: 16pt;'>审判员　　王燕燕</div><br/><div style='TEXT-ALIGN: right; LINE-HEIGHT: 25pt; MARGIN: 0.5pt 72pt 0.5pt 0cm;FONT-FAMILY: 仿宋; FONT-SIZE: 16pt;'>二〇一八年一月三十一日</div><div style='TEXT-ALIGN: right; LINE-HEIGHT: 25pt; MARGIN: 0.5pt 72pt 0.5pt 0cm;FONT-FAMILY: 仿宋; FONT-SIZE: 16pt;'>书记员　　温丽钰</div>"}";
    var jsonData = eval("(" + jsonHtmlData + ")");
    $("#contentTitle").html(jsonData.Title);
    $("#tdFBRQ").html("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;发布日期：" + jsonData.PubDate);
    var jsonHtml = jsonData.Html.replace(/01lydyh01/g, "'");
    $("#DivContent").html(jsonHtml);

    //初始化全文插件
    Content.Content.InitPlugins();
    //全文关键字标红
    Content.Content.KeyWordMarkRed();
});
    
    """

    extract(content)


if __name__ == "__main__":

    # main()

    test_one()