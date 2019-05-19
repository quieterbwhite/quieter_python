# MySql视图view的使用：创建、修改、删除

 2015年07月13日     5379     声明

视图`view`是基于 SQL 语句的结果集的可视化的表，视图是由查询结果形成的一张虚拟表，视图也包含行和列，就像一个真实的表。使用视图查询可以使查询数据相对安全，通过视图可以隐藏一些敏感字段和数据，从而只对用户暴露安全数据。视图查询也更简单高效，如果某个查询结果出现的非常频繁或经常拿这个查询结果来做子查询，将查询定义成视图可以使查询更加便捷。

1. [MySql创建视图](https://itbilu.com/database/mysql/E1q5C22_.html#create)
2. [MySql视图修改](https://itbilu.com/database/mysql/E1q5C22_.html#update)
3. [MySql视图删除](https://itbilu.com/database/mysql/E1q5C22_.html#drop)

### 1. MySql创建视图

创建视图与创建表语法类似，不同的是创建视图是从一条查询语句创建的。视图创建后，可以像一张表一样使用，但只能用于数据查询，如：可以在一个查询中使用、可以在存储过程中、可以在另一个视图中使用。MySql创建视图语法如下：

```
CREATE VIEW 视图名 AS SELECT 查询语句;
```

现有文章表`article`和文章类别表`articleCategory`，表结构如下：

```
mysql> show columns from article;
+-------------------+---------------+------+-----+---------+----------------+
| Field             | Type          | Null | Key | Default | Extra          |
+-------------------+---------------+------+-----+---------+----------------+
| articleId         | bigint(11)    | NO   | PRI | NULL    | auto_increment |
| articleCategoryId | int(11)       | YES  |     | NULL    |                |
| title             | varchar(255)  | NO   |     | NULL    |                |
| content           | text          | NO   |     | NULL    |                |
| author            | varchar(255)  | NO   |     | NULL    |                |
| published         | tinyint(1)    | NO   |     | 0       |                |
| createdOn         | datetime      | NO   |     | NULL    |                |
| updatedOn         | datetime      | NO   |     | NULL    |                |
+-------------------+---------------+------+-----+---------+----------------+
mysql> show columns from articleCategory;
+-------------------+--------------+------+-----+---------+----------------+
| Field             | Type         | Null | Key | Default | Extra          |
+-------------------+--------------+------+-----+---------+----------------+
| articleCategoryId | bigint(11)   | NO   | PRI | NULL    | auto_increment |
| name              | varchar(255) | NO   |     | NULL    |                |
| displayOrder      | int(11)      | NO   |     | 0       |                |
| createdOn         | datetime     | NO   |     | NULL    |                |
+-------------------+--------------+------+-----+---------+----------------+
```

现在，需要创建一个视图，需要查询`article`表的字段：title、content、author，及`articleCategory`表的字段：name。创建视图语句如下：

```
CREATE VIEW v_article AS SELECT A.title, A.content, A.author, C.name AS categoryName FROM article AS A JOIN articleCategory AS C ON A.articleCategoryId=C.articleCategoryId;
```

### 2. MySql视图修改

已经创建的视图，有时会需要修改其查询字段或查询条件，MySql视图修改语法如下：

```
ALTER VIEW 视图名 AS SELECT 查询语句;
```

现在对上文创建的视图`v_article`进行修改，增加查询文章创建时间字段：createdOn，具只查询发布状态：published 为 true的文章。语句如下：

```
ALTER VIEW v_article AS SELECT A.title, A.content, A.author, C.name AS categoryName, A.createdOn FROM article AS A JOIN articleCategory AS C ON A.articleCategoryId=C.articleCategoryId WHERE A.published=true;
```

### 3. MySql视图删除

MySql视图删除语法与删除表`DROP TABLE`类型，语法如下：

```
DROP VIEW 视图名;
```

上文创建的视图`v_article`已不在需要，删除语句如下：

```
DROP VIEW v_article;
```