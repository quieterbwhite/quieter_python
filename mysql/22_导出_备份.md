# Mysql 备份，导出数据
> http://c.biancheng.net/cpp/html/1458.html Mysql命令mysqldump：备份数据库  
> https://www.jianshu.com/p/b77dfd6d998b  MySQL数据库备份&还原-LINUX  
>
> https://www.cnblogs.com/liaokaichang/p/8177691.html

## mysqldump命令用来备份数据库
```
mysqldump命令在DOS的[url=file://\\mysql\\bin]\\mysql\\bin[/url]目录下执行。

1) 导出整个数据库(导出文件默认是存在mysql\bin目录下)
    mysqldump -u 用户名 -p 数据库名 > 导出的文件名
    mysqldump -u user_name -p123456 database_name > outfile_name.sql

2) 导出一个表
    mysqldump -u 用户名 -p 数据库名 表名> 导出的文件名
    mysqldump -u user_name -p database_name table_name > outfile_name.sql

3) 导出一个数据库结构
    mysqldump -u user_name -p -d –add-drop-table database_name > outfile_name.sql
    -d 没有数据 –add-drop-table 在每个create语句之前增加一个drop table

4) 带语言参数导出
    mysqldump -uroot -p –default-character-set=latin1 –set-charset=gbk –skip-opt database_name > outfile_name.sql

例如，将aaa库备份到文件back_aaa中：
[root@test1 root]# cd　/home/data/mysql
[root@test1 mysql]# mysqldump -u root -p --opt aaa > back_aaa
```

## 手动备份
```
1. 备份一个数据库
mysqldump -hhostname -uusername -pmypwd databasename > /path to backup/bakname.sql
备份并压缩
mysqldump -hhostname -uusername -pmypwd databasename ｜ gzip > /path to backup/bakname.sql.gz

2. 备份多个数据库
mysqldump -hhostname -uusername -pmypwd databases databasename1 databasename2 databasename3 > /path to backup/bakname.sql

3. 备份数据库一些表
mysqldump -hhostname -uusername -pmypwd databasename table1 table2 table3 > /path to backup/bakname.sql

4. 仅备份数据库结构
mysqldump -no-data -databases databasename1 databasename2 databasename3 > /path to backup/bakname.sql

5. 备份所有数据库
mysqldump -all-databases > /path to backup/bakname.sql
```

## 还原数据库
```
1. 还原无压缩数据库
mysql －hhostname -uuser -pmypwd databasename < /path to backup/bakname.sql

2. 还原压缩数据库
gunzip < /path to backup/bakname.sql.gz | mysql -hhostname -uusername -pmypwd databasename
```

## 迁移到新服务器
```
mysqldump -hhostname -uuser -pmypwd databasename | mysql -hnew_hostname -C databasename
```

## 脚本定时备份
```
创建备份脚本

vim mysql_backup.sh

#!/bin/sh
# This is a mysql datbase backup shell script.

# set mysql info
hostname="localhost"
user="root"
password="my password"

# set database info
database="bak database name"
bakpath="path to backup"
date=$(date +%Y%m%d_%H%M%S)

# backup
mkdir -p $bakpath
mysqldump -h$hostname -u$user -p$password $database | gzip \ 
> $bakpath/$database_$date_sql.gz


创建定时任务

crontab: crontab 是linux系统下的一个任务调度器

crontab定时服务 启动|结束|状态
service crond start | status | stop

# 查看config文件，可以看到定时规则
$ cat /etc/cron

# 添加备份定时任务
$ crontab -e
添加定时计划，例如：每天2点执行
0 2 * * * /path to sh/mysql_backup.sh
保存退出

# 查看当前用户定时任务
$ crontab -l

＃查看定时计划日志
$ tail -f /var/log/cron
```
