# -*- coding=utf-8 -*-


class DetailConstant(object):

    res_dict = {
        "docid" : "",                          # 文书id
        "title" : "",                          # 标题
        "trial_round" : "",                    # 审判阶段
        "case_no" : "",                        # 案号
        "law_firm" : "",                       # 法院名称
        "law_firm_province" : "",              # 法院省
        "law_firm_city" : "",                  # 法院市
        "law_firm_county" : "",                # 法院区县
        "trial_date" : "",                     # 裁判日期

        "plaintiff" : [],                      # 原告
        "plaintiff_procurator" : [],           # 原告委托代理人
        "plaintiff_agency" : [],               # 原告委托代理律所

        "defendant" : [],                      # 被告
        "defendant_procurator" : [],           # 被告委托代理人
        "defendant_agency" : [],               # 被告委托代理律所

        "accept_date" : "",                    # 受理日期
        "hear_date" : "",                      # 审理日期
        "exe_date" : "",                       # 立案执行日期
        "exe_ref_case_no" : "",                # 执行依据的案号
        "exe_rule" : "",                       # 执行裁定
        "program_type" : "",                   # 程序类型
        "loan_principal" : [],                 # 借款本金
        "credit_principal" : [],               # 贷款本金
        "bar_fee" : "",                        # 律师费
        "win_over" : "",                       # 胜诉情况
        "verdict" : "",                        # 裁决情况
        "dispute" : "",                        # 争议焦点
        "exe_evidence" : "",                   # 执行依据

        "appellant" : [],                      # 上诉人
        "appellant_law_agency" : [],           # 上诉委托代理

        "appellee" : [],                       # 被上诉人
        "appellee_law_agency" : [],            # 被上诉人委托代理

        "plaintiff_original" : [],             # 原审原告
        "defendant_original" : [],             # 原审被告

        "executor" : [],                       # 申请执行人
        "executor_law_agency" : [],            # 申请执行人代理

        "executed" : [],                       # 被执行人
        "executed_law_agency" : []             # 被执行人代理
    }