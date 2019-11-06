#### hive删除表和表中的数据

##### hive删除表和表中的数据，以及按分区删除数据
```shell
hive删除表：

    drop table table_name;

hive删除表中数据：

    truncate table table_name;

hive按分区删除数据：

    alter table table_name drop partition (partition_name='分区名')
```

```
背景: 
1、hive表删除数据不能使用DELETE FROM table_name 中SQL语句

2、hive表删除数据要分为不同的粒度：table、partition、partition内

一、有partition表

1. 删除具体partition
   alter table table_name drop partition(partiton_name='value'))
2. 删除partition内的部分信息(INSERT OVERWRITE TABLE）
   INSERT OVERWRITE TABLE table_name PARTITION(dt='v3') 
   SELECT column1,column2 FROM alpha_sales_staff_info
     WHERE dt='v3' AND category is not null;
     重新把对应的partition信息写一遍，通过WHERE 来限定需要留下的信息，没有留下的信息就被删除了。

二、无partiton表
INSERT OVERWRITE TABLE dpc_test SELECT * FROM dpc_test WHERE age is not null;
```





