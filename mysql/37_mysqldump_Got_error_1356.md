#### mysqldump: Got error: 1356 mysqldump的重要参数--force

2014-10-22 10:10:09 [lwei_998](https://me.csdn.net/lwei_998) 阅读数 9295 收藏 更多

分类专栏： [MySQL](https://blog.csdn.net/lwei_998/category_1186352.html)

版权声明：本文为博主原创文章，遵循[ CC 4.0 BY-SA ](http://creativecommons.org/licenses/by-sa/4.0/)版权协议，转载请附上原文出处链接和本声明。本文链接：https://blog.csdn.net/lwei_998/article/details/40372117

一个mysql的备份突然变小了很多，但实际的数据量却一直在增长。备份脚本也没有调整过。为什么呢？

重现了一下备份过程，发现备份中遇到了如下错误：
mysqldump: Got error: 1356: View 'wordpress.v_t1' references invalid table(s) or column(s) or function(s) or definer/invoker of view lack rights to use them when using LOCK TABLES

**原因:** 视图引用的表不存在。

**原理**：mysqldump在备份时要对表加读锁，加锁失败的时候。备份就终止了。

**解决方法：**在备份时加上--force参数


模拟测试如下：

**正常情况：**

**
***1.创建表t1并插入数据
*CREATE TABLE `t1` (
   `a` int(11) NOT NULL,
   `b` int(11) DEFAULT NULL,
   `c` int(11) DEFAULT NULL,
   PRIMARY KEY (`a`),
   UNIQUE KEY `b` (`b`)
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
  
  
insert into t1 values(1,3,5);  

*2.基于表t1创建视图
*create view v_t1 as select * from t1;

*3.模拟备份，可以正常备份出数据
*mysqldump -ubkpuser -ps3cret  wordpress>wordpress.sql


**模拟视图引用的表被删除：**

*1.删除表t1
*mysql> drop table t1;
Query OK, 0 rows affected

mysql> select * from v_t1;
1356 - View 'wordpress.v_t1' references invalid table(s) or column(s) or function(s) or definer/invoker of view lack rights to use them

*2. 模拟备份，失败
*$mysqldump -ubkpuser -ps3cret  wordpress >wordpress1.sql
Warning: Using a password on the command line interface can be insecure.
mysqldump: Got error: 1356: View 'wordpress.v_t1' references invalid table(s) or column(s) or function(s) or definer/invoker of view lack rights to use them when using LOCK TABLES

**3. 增加force参数后，虽然有错误，但不影响备份**
$mysqldump -ubkpuser -ps3cret ***\*--force\**** wordpress >wordpress1.sql
Warning: Using a password on the command line interface can be insecure.
mysqldump: Got error: 1356: View 'wordpress.v_t1' references invalid table(s) or column(s) or function(s) or definer/invoker of view lack rights to use them when using LOCK TABLES
mysqldump: Couldn't execute 'SHOW FIELDS FROM `v_t1`': View 'wordpress.v_t1' references invalid table(s) or column(s) or function(s) or definer/invoker of view lack rights to use them (1356)