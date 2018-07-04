# -*- coding=utf-8 -*-

"""

"""

import time
from copy import deepcopy

from constant.constant_request import RequestConstant
from handle_single_search import detect_count, get_task_list, process, save_fail
from util.date_list import dateRange


def main():

    queryString = " (( causeOfAction:01000000000000民事/01040000000000合同、无因管理、不当得利纠纷/01040010000000合同纠纷/01040010240000借款合同纠纷/01040010240010金融借款合同纠纷 )) "
    begin_date = "2018.04.01"
    end_date = "2018.04.30"
    datetime_range_list = dateRange(begin_date, end_date)

    payload = deepcopy(RequestConstant.SEARCH_PARAMS)
    payload["query"].update({"queryString" : queryString})

    for the_date in datetime_range_list:
        time.sleep(4)
        day_for_save = the_date.replace(".", "-")
        print("新的一天: {}".format(the_date))
        judgmentDate = "judgmentDate:[{} TO {}]".format(the_date, the_date)
        payload["query"].update({"filterDates" : [judgmentDate]})

        docCount, searchId = detect_count(payload)
        if docCount <= 0:
            print("当前日期 {} 没有数据".format(the_date))
            continue

        my_task_list = get_task_list(docCount, searchId, payload)
        if not my_task_list:
            save_fail(the_date)
            continue

        for task in my_task_list:
            process(task["payload"], task["nHits"], day_for_save)


if __name__ == "__main__":
    main()