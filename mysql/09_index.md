# Mysql 索引
> http://blog.720ui.com/2017/mysql_core_03_how_use_index/  如何设计索引  
> https://www.cnblogs.com/zz-tt/p/6609828.html

改善性能最好的方式，就是通过数据库中合理地使用索引，换句话说，索引是提高 MySQL 数据库查询性能的主要手段。
在下面的章节中，介绍了索引类型、强制索引、全文索引。  

## 基本索引类型
```
MySQL 索引可以分为单列索引、复合索引、唯一索引、主键索引等。这里，将为读者介绍这几种索引的特点。
```

## 单列索引
```
单列索引：单列索引是最基本的索引，它没有任何限制。

创建一个单列索引，例如：

    create index index_name on tbl_name(index_col_name);

同时，也可以通过修改表结构的方式添加索引，例如：

    alter table tbl_name add index index_name on (index_col_name);
```

## 复合索引
```
复合索引：

    复合索引是在多个字段上创建的索引。

    复合索引遵守“最左前缀”原则，即在查询条件中使用了复合索引的第一个字段，索引才会被使用。

    因此，在复合索引中索引列的顺序至关重要。

创建一个复合索引，例如：

    create index index_name on tbl_name(index_col_name,...);

同时，也可以通过修改表结构的方式添加索引，例如：

    alter table tbl_name add index index_name on (index_col_name,...);
```

## 唯一索引
```
唯一索引：

    唯一索引和单列索引类似，主要的区别在于，唯一索引限制列的值必须唯一，但允许有空值。对于多个字段，唯一索引规定列值的组合必须唯一。
    
    CREATE UNIQUE INDEX unique_keyword ON task_maid(keyword);

创建一个复合索引，例如：

    create unique index index_name on tbl_name(index_col_name,...);

同时，也可以通过修改表结构的方式添加索引，例如：

    alter table tbl_name add unique index index_name on (index_col_name,...);

搜索重复的数据:
    SELECT trail_no, count(*) FROM wenshu_maid
    GROUP BY trial_seq, trail_no, case_name
    HAVING COUNT(*) > 1;
    
删除重复的数据:
    DELETE FROM wenshu_maid WHERE
    trail_no IN (SELECT trail_no
                 FROM (SELECT trail_no, COUNT(*)
                       FROM wenshu_maid
                       GROUP BY trial_seq, trail_no, case_name
                       HAVING COUNT(*) > 1) as a);
                       
创建唯一索引:
    alter table wenshu_maid add unique index uni_record(trial_seq, trail_no, case_name);
    
ref: 

    https://blog.csdn.net/Alice_qixin/article/details/73163570
    
    http://www.runoob.com/mysql/mysql-handling-duplicates.html
```

## 主键索引
```
主键索引：

    主键索引是一种特殊的唯一索引，不允许有空值。此外， CREATE INDEX 不能创建主键索引，需要使用 ALTER TABLE 代替，例如：

    alter table tbl_name add primary key(index_col_name);
```

## 强制索引
```
有时，因为使用 MySQL 的优化器机制，原本应该使用索引的优化器，反而选择执行全表扫描或者执行的不是预期的索引。
此时，可以通过强制索引的方式引导优化器采取正确的执行计划。

使用强制索引，SQL 语句只使用建立在 index_col_name 上的索引，而不使用其它的索引。

    select * from tbl_name force index (index_col_name) …

切记，不要滥用强制索引，因为 MySQL 的优化器会同时评估 I/O 和 CPU 的成本，一般情况下，可以自动分析选择最合适的索引。

如果优化器成本评估错误，因而没有选择最佳方案，最好的方法应该是将合适的索引修改得更好。

如果某个 SQL 语句使用强制索引，需要在系统迭代开发过程中时时维护强制索引，一方面，需要保证使用的强制索引最优，另外一面，需要保证所使用的强制索引不能被误删，不然将导致 SQL 报错。

因此，如果某个 SQL 语句必须要使用强制索引，建议在团队内部开展严格地评审后才可以使用。
```

## 全文索引
```
在一般情况下，模糊查询都是通过 like 的方式进行查询。
但是，对于海量数据，这并不是一个好办法，在 like “value%” 可以使用索引，
但是对于 like “%value%” 这样的方式，执行全表查询，这在数据量小的表，不存在性能问题，
但是对于海量数据，全表扫描是非常可怕的事情,所以 like 进行模糊匹配性能很差。

这种情况下，需要考虑使用全文搜索的方式进行优化。
全文搜索在 MySQL 中是一个 FULLTEXT 类型索引。 
FULLTEXT 索引在 MySQL 5.6 版本之后支持 InnoDB，而之前的版本只支持 MyISAM 表。

假设，有一张应用全文索引表。

    CREATE TABLE IF NOT EXISTS `app_full_text` (
      `app_id` bigint(20) NOT NULL,
      `app_name_full_text` text NOT NULL,
      `introduce_full_text` text NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;

现在需要对应用的名称创建全文索引，可以这么设计。

    alter table `app_full_text` add fulltext key `app_name_intro` (`app_name_full_text`);

默认 MySQL 不支持中文全文检索，对此，网上的方案很多，

    例如添加 MySQL 扩展，

    或者将内容转换成拼音的方式存储在索引表，

    或者使用 IKAnalyzer 分词库等，

其效果都不是非常的理想。

使用拼音分词，虽然可以查询到内容，但是如果拼音相同的情况，是非常致命的，而且分词的粒度也是个很可怕的问题。

使用 IKAnalyzer 分词库，效果也不是很好。

因为业务的需要，命中率也是非常重要的，有的关键字没有进行分词导致查询不到的问题。

事实上，MySQL 全文搜索只是一个临时方案，对于全文搜索场景，更专业的做法是使用全文搜索引擎，例如 ElasticSearch 或 Solr。
```
