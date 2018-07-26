# -*- coding=utf-8 -*-

record_per_page = 5

def handle_page(nHits):
    """ 处理分页 """

    total_page = int(nHits / record_per_page)

    if nHits % record_per_page > 0: total_page += 1

    return total_page