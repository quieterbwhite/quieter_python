# -*- coding=utf-8 -*-
# Created Time: 2016年02月13日 星期六 11时47分46秒
# File Name: 01_trouble_shooting.py

'''
Mongodb trouble shooting
'''

'''
安装 mongodb 3.0.4:
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
echo "deb http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-org/3.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.0.list
sudo apt-get update
latest version: sudo apt-get install -y mongodb-org
name a version: sudo apt-get install -y mongodb-org=3.0.4 mongodb-org-server=3.0.4 mongodb-org-shell=3.0.4 mongodb-org-mongos=3.0.4 mongodb-org-tools=3.0.4

安装完成过后运行 mongo 时报错:
mongoone@mongoOne:~$ mongo
Failed global initialization: BadValue Invalid or no user locale set. Please ensure LANG and/or LC_* environment variables are set correctly.
解决方案:
export LANGUAGE=en_US.UTF-8
export.UTF-8
export LC_ALL=en_US.UTF-8

locale-gen en_US.UTF-8
dpkg-reconfigure locales

当通过mongo shell来插入日期类型数据时，使用new Date()和使用Date()是不一样的：
> db.tianyc04.insert({mark:1, mark_time:new Date()})
> db.tianyc04.insert({mark:2, mark_time:Date()})
> db.tianyc04.find()
{ "_id" : ObjectId("5126e00939899c4cf3805f9b"), "mark" : 1, "mark_time" : ISODate("2013-02-22T03:03:37.312Z") }
{ "_id" : ObjectId("5126e00c39899c4cf3805f9c"), "mark" : 2, "mark_time" : "Fri Feb 22 2013 11:03:40 GMT+0800" }
>
我们看：使用new Date()，插入的是一个isodate类型；而使用Date()插入的是一个字符串类型。
那isodate是什么日期类型的？我们看这2个值，它比字符串大概少了8小时。这是由于mongo中的date类型以UTC（Coordinated Universal Time）存储，就等于GMT（格林尼治标准时）时间。
而我当前所处的是+8区，所以mongo shell会将当前的GMT+0800时间减去8，存储成GMT时间。
如果通过get函数来获取，那么mongo会自动转换成当前时区的时间

报错:
[root@iZ282143ukzZ mytool]# mongo
MongoDB shell version: 2.4.12
connecting to: test
Mon Sep 21 14:23:50.358 Error: couldn't connect to server 127.0.0.1:27017 at src/mongo/shell/mongo.js:145
exception: connect failed
解决方法:
sudo rm /var/lib/mongodb/mongod.lock
sudo service mongodb restart
查看   mongodb 日志:
tail -f /var/log/mongodb/mongodb.log
'''
