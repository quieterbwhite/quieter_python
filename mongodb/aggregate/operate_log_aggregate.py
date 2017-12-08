# -*- coding=utf-8 -*-
# File Name: module_service.py

'''
模块统计相关服务
'''

import logging
import operator

from AppBackend.settings import mongo_db
from utils.formatter import dumps_ident
from statistics.name_map import sub_name_map

app_backend = mongo_db['klicendata']
output_logger = logging.getLogger("output")


class ModuleService(object):
    """ 模块统计相关服务 """

    @staticmethod
    def module_visit_stats(body):
        """ pv, uv 统计

            使用 mongodb 聚合功能统计
        """

        match, time_type = ModuleService.handle_module_visit_params(body)

        view_num = app_backend.operate_log.aggregate([

            {"$match" : match},

            {"$group" : {
                "_id" : {
                    "module_link" : "$module_link",
                    "user_id" : "$user_id",
                    "time" : "$" + time_type
                },
                "pv" : {"$sum" : 1}
            }},

            {"$group" : {
                "_id" : {
                    "module_link": "$_id.module_link",
                    "time": "$_id.time"
                },
                "pv" : {
                    "$sum" : "$pv"
                },
                "uv" : {
                    "$sum" : 1
                }
            }},

            {"$sort" : {"_id.time" : 1}}

        ])

        data_list = list(view_num)
        output_logger.info("data_list: %s" % data_list)

        result_list = ModuleService.handle_module_visit_stats(data_list)

        return result_list

    @staticmethod
    def handle_module_visit_params(body):
        """ 查询参数处理

        :returns
            match: 就是mongodb的查询条件
            time_type: 时间维度, 用作分组条件, day, week, month
        """

        match = {}

        user_type = body.get("user_type", 2)
        platform_type = body.get("platform_type", "all")
        version = body.get("version", "")
        begin_time = body.get("begin_time", "")
        end_time = body.get("end_time", "")
        time_type = body.get("time_type", "day")

        if user_type < 2:
            match.update({"is_vip" : user_type})

        if platform_type != "all":
            match.update({"os" : platform_type})

        if version:
            match.update({"version_sub" : version})

        match.update({"day" : {"$gte" : begin_time, "$lte" : end_time}})

        output_logger.info(dumps_ident(match))

        return match, time_type

    @staticmethod
    def handle_module_visit_stats(data_list):
        """ 处理统计的原始数据为客户端友好

        :return
            [
                {
                    "name": "首页-组队开车",
                    "pv": 4,
                    "time": "2017-10-10",
                    "uv": 1
                },
                {}
            ]
        """

        result_list = []

        # 循环两百次
        for data in data_list:
            tmp = {
                "pv"   : data.get("pv", 0),
                "uv"   : data.get("uv", 0),
                "name" : sub_name_map.get(data.get("_id", {}).get("module_link", "")),
                "time" : data.get("_id", {}).get("time", "")
            }
            result_list.append(tmp)

        return result_list

    @staticmethod
    def handle_order(result_list, order_type):
        """ 结果按 pv, uv 排序 """

        if order_type == "pv_up":
            sorted_result_list = sorted(result_list, key=operator.itemgetter("pv"))
        elif order_type == "pv_down":
            sorted_result_list = sorted(result_list, key=operator.itemgetter("pv"), reverse=True)
        elif order_type == "uv_up":
            sorted_result_list = sorted(result_list, key=operator.itemgetter("uv"))
        else:
            sorted_result_list = sorted(result_list, key=operator.itemgetter("uv"), reverse=True)

        return sorted_result_list