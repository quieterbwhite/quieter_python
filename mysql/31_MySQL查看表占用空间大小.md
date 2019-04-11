# MySQL查看表占用空间大小

2018年07月11日 16:42:18 [qq_21683643](https://me.csdn.net/qq_21683643) 阅读数：2137

需求：我们在选购服务器硬盘时，通常需要先估算一下数据量。比如我们现在做的项目，百万级用户，然后在现有的数据结构中插入一万条数据，然后根据相应的需求去计算出实际生产中的数据量。

前言：在mysql中有一个默认的数据表`information_schema`，information_schema这张数据表保存了MySQL服务器所有数据库的信息。如数据库名，数据库的表，表栏的数据类型与访问权限等。再简单点，这台MySQL服务器上，到底有哪些数据库、各个数据库有哪些表，每张表的字段类型是什么，各个数据库要什么权限才能访问，等等信息都保存在information_schema表里面，所以请勿删改此表。

代码：

1，切换数据库

use `information_schema`;

2，查看数据库使用大小

select concat(round(sum(data_length/1024/1024),2),’MB’) as data from tables where table_schema=’DB_Name’ ;

3，查看表使用大小

select concat(round(sum(data_length/1024/1024),2),’MB’) as data from tables where table_schema=’DB_Name’ and table_name=’Table_Name’;