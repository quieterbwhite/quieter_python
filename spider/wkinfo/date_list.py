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
    

def weekRang(beginDate, endDate):
    week = set()
    for date in dateRange(beginDate, endDate):
        week.add(datetime.date(int(date[0:4]), int(date[5:7]), int(date[8:10])).isocalendar()[0:2])
 
    wk_l = []
    for wl in sorted(list(week)):
        wk_l.append(str(wl[0])+'#'+str(wl[1]))


if __name__ == '__main__':
    for date in dateRange('2016-10-01', '2017-01-01'):
        print date
