# -*- coding=utf-8 -*-
# Created Time: 2016年07月23日 星期六 14时47分00秒
# File Name: dbmng.py

'''
数据库相关
'''

class GenQuerySQL(object):

    def __init__(self, table):
        self.table = table
        self.group_by_fields = ""
        self.where_conditions = "1=1"
        self.fields = ""
        self.order_by_fields = ""

    def where(self, where_condition):
        if where_condition:
            where_condition = " and ".join(where_condition)
            self.where_conditions += " and " + where_condition
        return self

    def add_field(self, fields):
        self.fields += " " + fields
        return self

    def group_by(self, group_by_field):
        self.group_by_fields = group_by_field
        return self

    def order_by(self, order_by_field):
        self.order_by_fields = order_by_field
        return self

    def sql_select(self):
        '''  '''

        SQL = 'SELECT' + self.fields + ' FROM ' + self.table + ' WHERE ' + self.where_conditions

        if self.group_by_fields:
            SQL += ' GROUP BY ' + self.group_by_fields

        if self.order_by_fields:
            SQL += ' ORDER BY ' + self.order_by_fields

        SQL += ';'
        return SQL

    def sql_update(self):
        '''  '''

        pass

    def sql_insert(self):
        '''  '''

        pass

    def sql_delete(self):
        '''  '''

        pass


def main():

    select, where = [], []

    select.extend(['1','2'])

    print 'select: ', select
    query_select = ','.join(select)

    print 'query_select: ', query_select

    packt = 'packt'
    sid   = 1

    if packt:
        where.append('packt = %s')

    if sid:
        where.append('sid = %s')

    where.extend(['created between %s and %s'])

    print 'where: ', where

    query_where = ' and '.join(where)

    print 'query_where: ', query_where
    group_by_fields = 'sid'
    order_by_fields = '-created'

    archive_statistics = GenQuerySQL('USER')
    # raw_sql = archive_statistics.add_field(query_select).where(query_where).sql()
    raw_sql = archive_statistics.add_field(query_select).where(query_where).group_by(group_by_fields).order_by(order_by_fields).sql()

    print 'raw_sql: ', raw_sql

if __name__ == '__main__':

    main()
