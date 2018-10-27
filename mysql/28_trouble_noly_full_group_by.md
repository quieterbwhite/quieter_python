#### [MYSQL5.7版本sql_mode=only_full_group_by问题](https://www.cnblogs.com/anstoner/p/6414440.html)

**目录**

- [ 具体出错提示：](https://www.cnblogs.com/anstoner/p/6414440.html#my_inner_label0)
- [    1、查看sql_mode](https://www.cnblogs.com/anstoner/p/6414440.html#my_inner_label1)
- [    查询出来的值为：](https://www.cnblogs.com/anstoner/p/6414440.html#my_inner_label2)
- [ 2、去掉ONLY_FULL_GROUP_BY，重新设置值。](https://www.cnblogs.com/anstoner/p/6414440.html#my_inner_label3)
- [    3、上面是改变了全局sql_mode，对于新建的数据库有效。对于已存在的数据库，则需要在对应的数据下执行：](https://www.cnblogs.com/anstoner/p/6414440.html#my_inner_label4)
- [ 解决办法大致有两种：](https://www.cnblogs.com/anstoner/p/6414440.html#my_inner_label5)
- [    二：修改my.cnf（windows下是my.ini）配置文件，删掉only_full_group_by这一项](https://www.cnblogs.com/anstoner/p/6414440.html#my_inner_label6)

下载安装的是最新版的mysql5.7.x版本，默认是开启了 `only_full_group_by` 模式的，但开启这个模式后，原先的 `group by`语句就报错，然后又把它移除了。

一旦开启 `only_full_group_by` ，感觉，`group by` 将变成和 `distinct` 一样，只能获取受到其影响的字段信息，无法和其他未受其影响的字段共存，这样，`group by` 的功能将变得十分狭窄了

`only_full_group_by` 模式开启比较好。

因为在 `mysql` 中有一个函数： `any_value(field)` 允许，非分组字段的出现（和关闭 `only_full_group_by` 模式有相同效果）。

 

##### 具体出错提示：

[Err] 1055 - Expression #1 of ORDER BY clause is not in GROUP BY clause and contains nonaggregated column 'information_schema.PROFILING.SEQ' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by

##### 1、查看sql_mode

##### 查询出来的值为：

ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION

##### 2、去掉ONLY_FULL_GROUP_BY，重新设置值。

##### 3、上面是改变了全局sql_mode，对于新建的数据库有效。对于已存在的数据库，则需要在对应的数据下执行：

　　

##### 解决办法大致有两种：

**一：在sql查询语句中不需要group by的字段上使用any_value()函数**

###### **这种对于已经开发了不少功能的项目不太合适，毕竟要把原来的sql都给修改一遍**

##### 二：修改my.cnf（windows下是my.ini）配置文件，删掉only_full_group_by这一项

若我们项目的mysql安装在ubuntu上面，找到这个文件打开一看，里面并没有sql_mode这一配置项，想删都没得删。

当然，还有别的办法，打开mysql命令行，执行命令

这样就可以查出sql_mode的值，复制这个值，在my.cnf中添加配置项（把查询到的值删掉only_full_group_by这个选项，其他的都复制过去）：

如果 [mysqld] 这行被注释掉的话记得要打开注释。然后重重启mysql服务

注：使用命令

这样可以修改一个会话中的配置项，在其他会话中是不生效的。　　 

------

One may fall in love with many people during the lifetime. When you finally get your own happiness, you will understand the previous sadness is kind of treasure, which makes you better to hold and cherish the people you love.

一个人一生可以爱上很多的人，等你获得真正属于你的幸福之后，你就会明白一起的伤痛其实是一种财富，它让你学会更好地去把握和珍惜你爱的人。



==================================================================================



升级到mysql 5.7后，但进行一些group by 查询时，比如下面的

SELECT *, count(id) as count FROM `news` GROUP BY `group_id` ORDER BY `inputtime` DESC LIMIT 20

就会报如下错误：

SELECT list is not in GROUP BY clause and contains nonaggregated column ‘news.id’ which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by.

原因是mysql 5.7 模式中。默认启用了ONLY_FULL_GROUP_BY。

ONLY_FULL_GROUP_BY是MySQL提供的一个sql_mode，通过这个sql_mode来提供SQL语句GROUP BY合法性的检查。

http://dev.mysql.com/doc/refman/5.7/en/sql-mode.html#sqlmode_only_full_group_by

 

`this is incompatible with sql_mode=only_full_group_by`这句话提示了这违背了mysql的规则，only fully group by，也就是说在执行的时候先分组，根据查询的字段（select的字段）在分组的内容中取出，所以查询的字段全部都应该在group by分组条件内；一种情况例外，查询字段中如果含有聚合函数的字段不用包含在group by中，就像我上面的count（id）。
 后来发现Order by排序条件的字段也必须要在group by内，排序的字段也是从分组的字段中取出。 不明白的可以去看一下。

解决办法：

1.set @@sql_mode=’STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION’;

去掉ONLY_FULL_GROUP_BY即可正常执行sql.

\2. 不去ONLY_FULL_GROUP_BY, 时 select字段必须都在group by分组条件内（含有函数的字段除外）。（如果遇到order by也出现这个问题，同理，order by字段也都要在group by内）。

3.利用ANY_VALUE()这个函数　https://dev.mysql.com/doc/refman/5.7/en/miscellaneous-functions.html#function_any-value

This function is useful for `GROUP BY` queries when the [`ONLY_FULL_GROUP_BY`](https://dev.mysql.com/doc/refman/5.7/en/sql-mode.html#sqlmode_only_full_group_by) SQL mode is enabled, for cases when MySQL rejects a query that you know is valid for reasons that MySQL cannot determine. The function return value and type are the same as the return value and type of its argument, but the function result is not checked for the [`ONLY_FULL_GROUP_BY`](https://dev.mysql.com/doc/refman/5.7/en/sql-mode.html#sqlmode_only_full_group_by) SQL mode.

 

如上面的sql语句可写成

SELECT ANY_VALUE(id)as id,ANY_VALUE(uid) as uid ,ANY_VALUE(username) as username,ANY_VALUE(title) as title,ANY_VALUE(author) as author,ANY_VALUE(thumb) as thumb,ANY_VALUE(description) as description,ANY_VALUE(content) as content,ANY_VALUE(linkurl) as linkurl,ANY_VALUE(url) as url,ANY_VALUE(group_id) as group_id,ANY_VALUE(inputtime) as inputtime, count(id) as count FROM `news` GROUP BY `group_id` ORDER BY ANY_VALUE(inputtime） DESC LIMIT 20

我选用的是第３种方法。



​    1.关闭5.7的 only_full_group_by 。(可以兼容5.6版本，但是如果用5.7 ，必须记得关闭)

​    2.使用5.7 的any_value函数 (5.6 不兼容)

```
select any_value(id),any_value(school_id),any_value(max(school_year)) FROM org_school_grade GROUP BY id
```

====================================================================================