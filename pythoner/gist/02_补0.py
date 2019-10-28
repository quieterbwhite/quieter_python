def get_asset_code(auction_id, source):
    """
    生成合适的ID
    规则：
        总共13位的数字，首位代表来源+1的数字，后面为id不够的用0填充
    :param auction_id:
    :param source: 来源 0 来自taobao 1 来自京东 2 来自公拍网
    """
    head = stringtoint(source)
    return "{}{:0>12}".format(head + 1, auction_id)
