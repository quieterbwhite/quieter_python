# Mysql 性能优化建议
> https://coolshell.cn/articles/1846.html  MYSQL性能优化的最佳20+条经验  

## 1. 为查询缓存优化你的查询
```
大多数的MySQL服务器都开启了查询缓存。
这是提高性最有效的方法之一，而且这是被MySQL的数据库引擎处理的。
当有很多相同的查询被执行了多次的时候，这些查询结果会被放到一个缓存中，
这样，后续的相同的查询就不用操作表而直接访问缓存结果了。

// 查询缓存不开启
$r = mysql_query("SELECT username FROM user WHERE signup_date >= CURDATE()");
 
// 开启查询缓存
$today = date("Y-m-d");
$r = mysql_query("SELECT username FROM user WHERE signup_date >= '$today'");

上面两条SQL语句的差别就是 CURDATE() ，MySQL的查询缓存对这个函数不起作用。
所以，像 NOW() 和 RAND() 或是其它的诸如此类的SQL函数都不会开启查询缓存，
因为这些函数的返回是会不定的易变的。
所以，你所需要的就是用一个变量来代替MySQL的函数，从而开启缓存。
```

## 2. EXPLAIN 你的 SELECT 查询
```
使用 EXPLAIN 关键字可以让你知道MySQL是如何处理你的SQL语句的。
这可以帮你分析你的查询语句或是表结构的性能瓶颈。

EXPLAIN 的查询结果还会告诉你你的索引主键被如何利用的，你的数据表是如何被搜索和排序的。
```
