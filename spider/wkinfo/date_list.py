# -*- coding=utf-8 -*-
import datetime
 
def dateRange(beginDate, endDate):
    dates = []
    dt = datetime.datetime.strptime(beginDate, "%Y-%m-%d")
    date = beginDate[:]
    while date <= endDate:
        dates.append(date)
        dt = dt + datetime.timedelta(1)
        date = dt.strftime("%Y-%m-%d")
    return dates
 
if __name__ == '__main__':
    for date in dateRange('2016-10-01', '2017-01-01'):
        print date
