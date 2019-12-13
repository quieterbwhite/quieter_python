#### Python 3 进阶 —— 使用 PyMySQL 操作 MySQL

2018-07-17 

[ Python](https://shockerli.net/categories/python/)

## 文章目录

[安装](https://shockerli.net/post/python3-pymysql/#%E5%AE%89%E8%A3%85)[创建数据库连接](https://shockerli.net/post/python3-pymysql/#%E5%88%9B%E5%BB%BA%E6%95%B0%E6%8D%AE%E5%BA%93%E8%BF%9E%E6%8E%A5)[执行 SQL](https://shockerli.net/post/python3-pymysql/#%E6%89%A7%E8%A1%8C-sql)[获取自增 ID](https://shockerli.net/post/python3-pymysql/#%E8%8E%B7%E5%8F%96%E8%87%AA%E5%A2%9E-id)[查询数据](https://shockerli.net/post/python3-pymysql/#%E6%9F%A5%E8%AF%A2%E6%95%B0%E6%8D%AE)[游标控制](https://shockerli.net/post/python3-pymysql/#%E6%B8%B8%E6%A0%87%E6%8E%A7%E5%88%B6)[设置游标类型](https://shockerli.net/post/python3-pymysql/#%E8%AE%BE%E7%BD%AE%E6%B8%B8%E6%A0%87%E7%B1%BB%E5%9E%8B)[事务处理](https://shockerli.net/post/python3-pymysql/#%E4%BA%8B%E5%8A%A1%E5%A4%84%E7%90%86)[防 SQL 注入](https://shockerli.net/post/python3-pymysql/#%E9%98%B2-sql-%E6%B3%A8%E5%85%A5)[参考资料](https://shockerli.net/post/python3-pymysql/#%E5%8F%82%E8%80%83%E8%B5%84%E6%96%99)

[PyMySQL](https://github.com/PyMySQL/PyMySQL) 是一个纯 Python 实现的 MySQL 客户端操作库，支持事务、存储过程、批量执行等。

PyMySQL 遵循 Python 数据库 API v2.0 规范，并包含了 pure-Python MySQL 客户端库。

## 安装

```
pip install PyMySQL
```

## 创建数据库连接

```
import pymysql

connection = pymysql.connect(host='localhost',
                             port=3306,
                             user='root',
                             password='root',
                             db='demo',
                             charset='utf8')
```

参数列表：

| 参数                 | 描述                                       |
| ------------------ | ---------------------------------------- |
| host               | 数据库服务器地址，默认 localhost                    |
| user               | 用户名，默认为当前程序运行用户                          |
| password           | 登录密码，默认为空字符串                             |
| database           | 默认操作的数据库                                 |
| port               | 数据库端口，默认为 3306                           |
| bind_address       | 当客户端有多个网络接口时，指定连接到主机的接口。参数可以是主机名或IP地址。   |
| unix_socket        | unix 套接字地址，区别于 host 连接                   |
| read_timeout       | 读取数据超时时间，单位秒，默认无限制                       |
| write_timeout      | 写入数据超时时间，单位秒，默认无限制                       |
| charset            | 数据库编码                                    |
| sql_mode           | 指定默认的 SQL_MODE                           |
| read_default_file  | Specifies my.cnf file to read these parameters from under the [client] section. |
| conv               | Conversion dictionary to use instead of the default one. This is used to provide custom marshalling and unmarshaling of types. |
| use_unicode        | Whether or not to default to unicode strings. This option defaults to true for Py3k. |
| client_flag        | Custom flags to send to MySQL. Find potential values in constants.CLIENT. |
| cursorclass        | 设置默认的游标类型                                |
| init_command       | 当连接建立完成之后执行的初始化 SQL 语句                   |
| connect_timeout    | 连接超时时间，默认 10，最小 1，最大 31536000            |
| ssl                | A dict of arguments similar to mysql_ssl_set()’s parameters. For now the capath and cipher arguments are not supported. |
| read_default_group | Group to read from in the configuration file. |
| compress           | Not supported                            |
| named_pipe         | Not supported                            |
| autocommit         | 是否自动提交，默认不自动提交，参数值为 None 表示以服务器为准        |
| local_infile       | Boolean to enable the use of LOAD DATA LOCAL command. (default: False) |
| max_allowed_packet | 发送给服务器的最大数据量，默认为 16MB                    |
| defer_connect      | 是否惰性连接，默认为立即连接                           |
| auth_plugin_map    | A dict of plugin names to a class that processes that plugin. The class will take the Connection object as the argument to the constructor. The class needs an authenticate method taking an authentication packet as an argument. For the dialog plugin, a prompt(echo, prompt) method can be used (if no authenticate method) for returning a string from the user. (experimental) |
| server_public_key  | SHA256 authenticaiton plugin public key value. (default: None) |
| db                 | 参数 database 的别名                          |
| passwd             | 参数 password 的别名                          |
| binary_prefix      | Add _binary prefix on bytes and bytearray. (default: False) |

## 执行 SQL

-   cursor.execute(sql, args) 执行单条 SQL

    ```
    # 获取游标
    cursor = connection.cursor()
        
    # 创建数据表
    effect_row = cursor.execute('''
    CREATE TABLE `users` (
      `name` varchar(32) NOT NULL,
      `age` int(10) unsigned NOT NULL DEFAULT '0',
      PRIMARY KEY (`name`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ''')
        
    # 插入数据(元组或列表)
    effect_row = cursor.execute('INSERT INTO `users` (`name`, `age`) VALUES (%s, %s)', ('mary', 18))
        
    # 插入数据(字典)
    info = {'name': 'fake', 'age': 15}
    effect_row = cursor.execute('INSERT INTO `users` (`name`, `age`) VALUES (%(name)s, %(age)s)', info)
        
    connection.commit()
    ```

-   executemany(sql, args) 批量执行 SQL

    ```
    # 获取游标
    cursor = connection.cursor()
        
    # 批量插入
    effect_row = cursor.executemany(
        'INSERT INTO `users` (`name`, `age`) VALUES (%s, %s) ON DUPLICATE KEY UPDATE age=VALUES(age)', [
            ('hello', 13),
            ('fake', 28),
        ])
        
    connection.commit()
    ```

注意：INSERT、UPDATE、DELETE 等修改数据的语句需手动执行`connection.commit()`完成对数据修改的提交。

## 获取自增 ID

```
cursor.lastrowid
```

## 查询数据

```
# 执行查询 SQL
cursor.execute('SELECT * FROM `users`')

# 获取单条数据
cursor.fetchone()

# 获取前N条数据
cursor.fetchmany(3)

# 获取所有数据
cursor.fetchall()
```

## 游标控制

所有的数据查询操作均基于游标，我们可以通过`cursor.scroll(num, mode)`控制游标的位置。

```
cursor.scroll(1, mode='relative') # 相对当前位置移动
cursor.scroll(2, mode='absolute') # 相对绝对位置移动
```

## 设置游标类型

查询时，默认返回的数据类型为元组，可以自定义设置返回类型。支持5种游标类型：

-   Cursor: 默认，元组类型
-   DictCursor: 字典类型
-   DictCursorMixin: 支持自定义的游标类型，需先自定义才可使用
-   SSCursor: 无缓冲元组类型
-   SSDictCursor: 无缓冲字典类型

无缓冲游标类型，适用于数据量很大，一次性返回太慢，或者服务端带宽较小时。源码注释：

>   Unbuffered Cursor, mainly useful for queries that return a lot of data, or for connections to remote servers over a slow network.
>
>   Instead of copying every row of data into a buffer, this will fetch rows as needed. The upside of this is the client uses much less memory, and rows are returned much faster when traveling over a slow network or if the result set is very big.
>
>   There are limitations, though. The MySQL protocol doesn’t support returning the total number of rows, so the only way to tell how many rows there are is to iterate over every row returned. Also, it currently isn’t possible to scroll backwards, as only the current row is held in memory.

创建连接时，通过 cursorclass 参数指定类型：

```
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='demo',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)
```

也可以在创建游标时指定类型：

```
cursor = connection.cursor(cursor=pymysql.cursors.DictCursor)
```

## 事务处理

-   开启事务 `connection.begin()`
-   提交修改 `connection.commit()`
-   回滚事务 `connection.rollback()`

## 防 SQL 注入

-   转义特殊字符 `connection.escape_string(str)`
-   参数化语句 支持传入参数进行自动转义、格式化 SQL 语句，以避免 SQL 注入等安全问题。

```
# 插入数据(元组或列表)
effect_row = cursor.execute('INSERT INTO `users` (`name`, `age`) VALUES (%s, %s)', ('mary', 18))

# 插入数据(字典)
info = {'name': 'fake', 'age': 15}
effect_row = cursor.execute('INSERT INTO `users` (`name`, `age`) VALUES (%(name)s, %(age)s)', info)

# 批量插入
effect_row = cursor.executemany(
    'INSERT INTO `users` (`name`, `age`) VALUES (%s, %s) ON DUPLICATE KEY UPDATE age=VALUES(age)', [
        ('hello', 13),
        ('fake', 28),
    ])
```

## 参考资料

-   [Python中操作mysql的pymysql模块详解](http://www.cnblogs.com/wt11/p/6141225.html)
-   [Python之pymysql的使用](http://www.cnblogs.com/liubinsh/p/7568423.html)

文章作者 Jioby

上次更新 2018-07-17

许可协议 [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/)

原文链接 <https://shockerli.net/post/python3-pymysql/>