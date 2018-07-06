# -*- coding=utf-8 -*-

"""
抓取威科先行列表页
"""

import time
from copy import deepcopy

from logs.mylog import flogger
from constant.constant_request import RequestConstant
from search import detect_count, get_task_list, process, save_fail
from util.date_list import dateRange
from login import get_new_session

# TODO 重新登录


def main():

    queryString = " (( causeOfAction:01000000000000民事/01040000000000合同、无因管理、不当得利纠纷/01040010000000合同纠纷/01040010240000借款合同纠纷/01040010240010金融借款合同纠纷 )) "
    begin_date = "2018.03.20"
    end_date = "2018.03.31"
    datetime_range_list = dateRange(begin_date, end_date)

    payload = deepcopy(RequestConstant.SEARCH_PARAMS)
    payload["query"].update({"queryString" : queryString})

    session = get_new_session()

    for the_date in datetime_range_list:
        time.sleep(5)
        day_for_save = the_date.replace(".", "-")
        flogger.info("新的一天: {}".format(the_date))
        judgmentDate = "judgmentDate:[{} TO {}]".format(the_date, the_date)
        payload["query"].update({"filterDates" : [judgmentDate]})

        docCount, searchId = detect_count(session, payload)
        if docCount <= 0:
            flogger.info("当前日期 {} 没有数据".format(the_date))
            continue

        my_task_list = get_task_list(session, docCount, searchId, payload)
        if not my_task_list:
            save_fail(the_date)
            continue

        for task in my_task_list:
            process(session, task["payload"], task["nHits"], day_for_save)


if __name__ == "__main__":
    main()