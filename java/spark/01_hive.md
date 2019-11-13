#### Hive

[使用说明](#使用说明)

[hive之间导数据](#hive之间导数据)

##### 环境
```
web:
    http://172.16.0.82:50070

相关命令:

    hive目录: /bigdata/hive-2.3.5/bin

    进入hive命令行: ./beeline -u jdbc:hive2://

    导入数据到表:

        0: jdbc:hive2://> load data local inpath '/root/datas/sifa/sifa_2019-07-19.json' into table ods_sifa partition(ct='2017-01-04');

    查询数据量:

        0: jdbc:hive2://> seclect count(*) from ods_shixin;
```

##### 使用说明
```
1. 登录服务器

    参考[正式环境]内容

2. 进入 hive shell

    $ cd /root/software/hive-2.3.5/bin

    $ ./beeline -u jdbc:hive2://

3. 使用 hive 查询内容

    > show databases;

    > use dp;

    > show tables;

        表名解释:
            ods_lian_tmp, tmp结尾的为临时表, 无用.

            ods_ 开头的是原始数据

            dw_ 开头的是清洗过后的数据

    # 查看表结构
    > describe dw_pochan;

    # 查询, 使用方法和mysql类似, ct为日期字段代表当日插入的数据
    > select * from dw_pochan where ct='2019-07-16' limit 1;

4. 备注

    使用中有任何问题可以咨询数据平台同事
```

##### hive之间导数据
```
1. 从原hive中导出数据, 使用hadoop命令从hdfs拉取数据到本地文件系统

    hadoop fs -get /user/hive/warehouse/dp.db/ods_sifa /tmp/data/sifa

2. scp发送数据到新的服务器

3. 使用hadoop命令将文件导入到hdfs相应目录

    hadoop fs -put /tmp/data/sifa /user/hive/warehouse/dp.db/ods_sifa

4. 使用hive命令修复表

    第一种情况：一层分区的情况

        建表
        执行 MSCK REPAIR TABLE table_name;

    第二种情况：多层分区情况

        建表
        执行 set hive.msck.path.validation=ignore;
        MSCK REPAIR TABLE table_name;
```
