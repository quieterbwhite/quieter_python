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

