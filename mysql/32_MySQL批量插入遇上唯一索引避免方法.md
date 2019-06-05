# MySQL批量插入遇上唯一索引避免方法（避免导入重复数据）

2017年01月06日 10:08:45 [jinmaodao116](https://me.csdn.net/jinmaodao116) 阅读数：6818

 版权声明：本文为博主原创文章，未经博主允许不得转载。 https://blog.csdn.net/jinmaodao116/article/details/54134480

## MySQL批量插入遇上唯一索引避免方法（避免导入重复数据）

未避免导入重复数据，建议建立唯一索引 
防止批量插入时，遇上唯一索引，可以使用以下3种方法避免方法

- （一）导入差异数据，忽略重复数据，IGNORE INTO的使用
- （二）导入并覆盖重复数据，REPLACE INTO 的使用
- （三）导入保留重复数据未指定字段，INSERT INTO ON DUPLICATE KEY UPDATE 的使用

**表 test1**

| id   | user_id | user_name | user_type |
| ---- | ------- | --------- | --------- |
| 1    | 101     | 101       | 1         |
| 2    | 102     | 102       | 2         |
| 3    | 103     | 103       | 3         |

**表 test2**

| id   | user_id | user_name | user_type |
| ---- | ------- | --------- | --------- |
| 1    | 201     | 201       | 1         |
| 2    | 202     | 202       | 2         |
| 3    | 203     | 203       | 3         |
| 4    | 101     | 204       | 4         |

#### （一）使用第一种方式导入，IGNORE INTO的使用：

```
INSERT IGNORE INTO test1(user_id,user_name,user_type) 
SELECT user_id,user_name,user_type FROM test2;
```

表 test1 的结果如下

| id   | user_id | user_name | user_type |
| ---- | ------- | --------- | --------- |
| 1    | 101     | 101       | 1         |
| 2    | 102     | 102       | 2         |
| 3    | 103     | 103       | 3         |
| 4    | 201     | 201       | 1         |
| 5    | 202     | 202       | 2         |
| 6    | 203     | 203       | 3         |

> 表2 中的id=4的记录，则被忽略，不导入。

#### （二）使用第二种方式导入，REPLACE INTO 的使用

```
REPLACE INTO test1(user_id,user_name,user_type) 
SELECT user_id,user_name,user_type FROM test2;
```

表 test1 的结果如下

| id   | user_id | user_name | user_type |
| ---- | ------- | --------- | --------- |
| 2    | 102     | 102       | 2         |
| 3    | 103     | 103       | 3         |
| 4    | 201     | 201       | 1         |
| 5    | 202     | 202       | 2         |
| 6    | 203     | 203       | 3         |
| 7    | 101     | 204       | 4         |

> 从上图可以发现，user_id = 101 的数据发生了变化。如果导入中发现了重复的，先删除再插入。

如果导入时，没有指定列，则未指定的列的数据，将会被替换为(Null)

```
REPLACE INTO test1(user_id,user_name) 
SELECT user_id,user_name FROM test2;
```

表 test1 的结果如下

| id   | user_id | user_name | user_type |
| ---- | ------- | --------- | --------- |
| 2    | 102     | 102       | 2         |
| 3    | 103     | 103       | 3         |
| 4    | 201     | 201       | (Null)    |
| 5    | 202     | 202       | (Null)    |
| 6    | 203     | 203       | (Null)    |
| 7    | 101     | 204       | (Null)    |

#### （三）使用第三种方式导入，INSERT INTO ON DUPLICATE KEY UPDATE 的使用

```
INSERT INTO test1(user_id,user_name,user_type) 
SELECT user_id,user_name,user_type FROM test2 
ON DUPLICATE KEY UPDATE 
test1.user_name = test2.user_name;
```

表 test1 的结果如下

| id   | user_id | user_name | user_type |
| ---- | ------- | --------- | --------- |
| 1    | 101     | 204       | 1         |
| 2    | 102     | 102       | 2         |
| 3    | 103     | 103       | 3         |
| 4    | 201     | 201       | 1         |
| 5    | 202     | 202       | 2         |
| 6    | 203     | 203       | 3         |

> 如上图，只有user_id=101 的 user_name 发生了变化，但是保留 test1 表的 user_type 字段。如果更新多个字段，再后面追加即可。
>
> ```
> INSERT INTO test1(user_id,user_name,user_type) 
> SELECT user_id,user_name,user_type FROM test2 
> ON DUPLICATE KEY UPDATE 
> test1.user_name = test2.user_name,
> test1.user_type = test2.user_type;
> ```