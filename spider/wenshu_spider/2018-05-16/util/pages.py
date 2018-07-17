# -*- coding=utf-8 -*-

def handle_page(nHits):
    """ 处理分页 """

    total_page = int(nHits / 20)

    if nHits % 20 > 0: total_page += 1

    return total_page