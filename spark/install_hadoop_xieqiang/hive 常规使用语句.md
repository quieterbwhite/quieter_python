# hive 常规使用语句

```shell
1，若运行mr时内存不够可通过如下方式设置：

在运行hive sql前加上 ： 
（map） set mapreduce.map.memory.mb=2048 或者 
（reduce） set mapreduce.reduce.memory.mb=2048
2，分组求top 去重

insert into table dw_shixin_new partition (ct="2019-07-13") select id,name,code_num,case_code,age,sexy,gist_id,business_entity,court,area,reg_date,gist_unit,duty,performance,disrupt_type_name,publish_date,ct from (select id,name,code_num,case_code,age,sexy,gist_id,business_entity,court,area,reg_date,gist_unit,duty,performance,disrupt_type_name,publish_date,ct,row_number() over (partition by code_num,case_code order by code_num desc) p_num from dw_shixin where ct='2019-07-13') a where a.p_num =1;



3，进行有事务得操作（删除，修改）时，直接在hive命令行执行：

set hive.input.format=org.apache.hadoop.hive.ql.io.HiveInputFormat;
set hive.support.concurrency=true;
set hive.txn.manager=org.apache.hadoop.hive.ql.lockmgr.DbTxnManager;
```

