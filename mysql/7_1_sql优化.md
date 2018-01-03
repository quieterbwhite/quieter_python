# SQL查询优化

```
如何设计最优的数据库表结构
如果建立最好的索引
如何扩展数据库的查询
```

## 如何获取有性能问题的sql
```
1. 通过用户反馈
2. 通过慢查日志获取存在性能问题的sql
3. 实时获取存在性能问题的sql
```

## 慢查日志
```
slow_query_log 启动停止记录慢查日志， 默认是不启动的，也可以动态设置
slow_query_log_file 指定慢查日志的存储路径及文件
long_query_time 指定记录慢查日志sql执行时间的阈值，默认值10s，通知1ms比较合适
log_queries_not_using_indexes 是否记录未使用索引的sql
```

## 常用的慢查日志分析工具
```
mysqldumpslow, 随mysql安装

    汇总除查询条件外其他完全相同的sql
    并将分析结构按照参数中所指定的顺序输出

    mysqldumpslow -s r -t 10 slow-mysql.log

    -s order (c, t, l, r...)

    -t top
    指定取前几条作为结果输出
```

```
pt-query-digest \
--explain h=127.0.0.1,u=root,p=p@password \
slow-mysql.log

最好使用从服务器
```

## 如何实时获取有性能问题的sql
```
利用 information_schema 下的 PROCESSLIST 表

select if, `user`, `host`, DB, command, `time`, state, info, FROM
information_schema.PROCESSLIST
WHERE TIME >= 60;
```

## 查询速度为什么会慢
```
mysql服务器处理查询请求的过程:

    1. 客户端发送sql请求给服务器
    2. 服务器检查是否可以在查询缓存中命中该sql
    3. 服务器端执行sql解析，预处理，再由优化器生成对应的执行计划
    4. 根据执行计划，调用存储引擎api来查询数据
    5. 将结果返回给客户端
```

## 查询缓存
```
对于一个读写频繁的系统使用查询缓存很可能会降低查询处理的效率

所以在这种情况下建议大家不要使用查询缓存

query_cache_type  设置查询缓存是否可用(off)

query_cache_size  设置查询缓存内存大小(0)

query_cache_limit  设置查询缓存可用存储的最大值

query_cache_wlock_invalidate  设置数据表被锁后是否返回缓存中的数据

query_cache_min_res_unit  设置查询缓存分配的内存块最小单位
```

```
mysql 依照这个执行计划和存储引擎进行交互

这个阶段包括多个子过程:

    解析sql， 预处理， 优化sql执行计划

    语法解析阶段是通过关键字对MySQL语句进行解析

    并生成一颗对应的解析树

会造成MySQL生成错误的执行计划的原因

    统计信息不正确

    执行计划中的成本估算并不等同于实际的执行计划的成本

    mysql优化器所认为的最优可能与你所认为的最优不一样
    基于其成本模型选择最优的执行计划

    mysql从不考虑其他并发查询，这可能会影响当前查询的速度

    MySQL有时也会基于一些固定的规则来生成执行计划

    * mysql优化器可优化的SQL类型
```

## 如何确定查询处理各个阶段所消耗的时间
```
减少查询消耗的时间，加快查询的响应速度

使用 profile

    set profiling = 1;

    执行查询

    show profiles;
    查看每一个查询所消耗的总时间的信息

    show profile for query N;
    查询某个阶段所消耗的时间

    show warnings;

使用 performance_schema, since v5.5

    // 启动监控项
    UPDATE `setup_instruments` SET enabled='YES', TIMED='YES' WHERE NAME LIKE 'stage%';

    UPDATE `setup_consumers` SET enabled='YES' WHERE NAME LIKE 'events%';

    开启 performance_schema 是全局有效的

    // 没写出来，需要再到网上去找
    一条语句可以查询执行中各个阶段所消耗的时间
```

## 特定sql的查询优化
```
如何获取一个存在性能问题的sql

如何度量一个SQL在执行的各个阶段所消耗的时间

接下来就该优化SQL语句了

大表的数据修改最好分批进行
    1000万行数据的表中删除/更新100万行记录一次只删除/更新5000行记录
    暂停几秒(给主从复制一定时间)

如何修改大表的结构
    对表中的列的字段类型进行修改
    改变字段的宽度时还是会锁表
    无法解决主从数据库延迟的问题

    // mysql shell 下直接执行修改
    alter table sbtest4 modify c varchar(150) not null default '';

    // 专业工具修改 大表结构
    pt-online-schema-change \
    --alter="MODIFY c VARCHAR(150) NOT NULL DEFAULT ''" \
    --user=root --password=Password D=imooc,t=sbtest4 \
    --charset=utf8 --execute

    所做的事情就是建立新表，拷贝旧表数据到新表，删除旧表，重命名新表

如何优化 not in 和 <> 查询

    // 原始语句
    select customer_id, first_name, last_name, email from customer
    where customer_id not in (select customer_id from payment) // payment 表会被多次查询

    // 改写
    select a.customer_id, a.first_name, a.last_name, a.email from customer a
    LEFT JOIN payment b ON a.customer_id = b.customer_id
    WHERE b.customer_id IS NULL

使用汇总表优化查询

    select count(*) from product_comment where product_id = 99;

    汇总表就是提前把要统计的数据进行汇总并记录到表中以备后续查询使用

    // 建立汇总表
    create table product_comment_cnt(product_id INT, cnt INT);
    // 每天凌晨统计前一天的数据存储到表中

    // 前面所有的加上当天的评论数
    select sum(cnt) from (
        select cnt from product_comment_cnt where product_id=99
        uniont all 
        select count(*) from product_comment where product_id = 99
        and timestr > DATE(NOW())
    ) a

```

