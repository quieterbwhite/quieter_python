#### SQL语句技巧

##### 1. 查询存在一个表而不在另一个表中的数据记录

```
方法一(仅适用单个字段)
使用 not in ,容易理解,效率低
select A.ID from A where A.ID not in (select ID from B)

方法二（适用多个字段匹配）
使用 left join...on... , "B.ID isnull" 表示左连接之后在B.ID 字段为 null的记录
select A.ID from A left join B on A.ID=B.ID where B.ID is null 

方法三（适用多个字段匹配）
select * from B where (select count(1) as num from A where A.ID = B.ID) = 0

方法四（适用多个字段匹配）
select * from A where not exists(select 1 from B where A.ID=B.ID)
```

##### 2. mysql如何重置自增长ID
```
方法一，执行SQL：
truncate table test;  (这里假定你的表名test，会删除本表，新插入时ID才重新开始)
这种方法好处是运行速度超快
 
方法二，执行如下SQL: (还是假定表名是test)
delete from test;
alter table `test` auto_increment=1;
这种方法好处是可以从任何值开始，缺点是如果数据量大的话delete from test;非常耗时
```
