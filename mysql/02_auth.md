# Mysql 权限管理
> http://blog.720ui.com/2017/mysql_core_06_security/  数据库安全性

```
MySQL 权限控制，分为两个步骤。

第一步骤

    服务器会检查是否允许连接。
    因为创建用户的时候会加上主机限制，可以限制成本地、某个 IP、某个 IP 段等，只允许从配置的指定地方登录。

第二步骤

    如果允许连接，那么 MySQL 会检查发出的每个请求是否有足够的权限执行。
    举个例子，假设需要删除某个表，MySQL 会检查是否对这个表有删除操作权限。

MySQL 为了数据库的安全性，设置了对数据的存取进行控制的语句，对用户授权使用 GRANT 语句，收回所授的权限使用 REVOKE 语句。
```

## windows下开启mysql远程访问
> https://www.cnblogs.com/shihaiming/p/6244305.html
``` 
USE mysql;
SELECT * FROM USER ;

直接修改user=root host=127.0.0.1为%

FLUSH PRIVILEGES;
```

## windows下远程连接Mysql
> https://www.cnblogs.com/fnlingnzb-learner/p/5848405.html
```
1. 使用“Ctrl + R”组合键快速打开cmd窗口，并输入“cmd”命令，打开cmd窗口。
2. 使用“mysql -uroot -proot”命令可以连接到本地的mysql服务。
3. 使用“use mysql”命令，选择要使用的数据库，修改远程连接的基本信息，保存在mysql数据库中，因此使用mysql数据库。
4. 使用“GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'root' WITH GRANT OPTION;”命令可以更改远程连接的设置。
5. 使用“flush privileges;”命令刷新刚才修改的权限，使其生效。
6. 使用“select host,user from user;”查看修改是否成功。

更多: 解决远程连接时防火墙阻止访问
```

## GRANT 授予用户权限
```
授予用户权限，简单格式可概括如下。

    GRANT <权限>

    ON <数据库对象>

    TO <用户>

假设，需要让普通 DBA 管理某个数据库的权限，可以授予这个数据库的所有权限。

    grant select, insert, update, delete on db_name.* to 'dba'@'localhost'

假设，需要让高级 DBA 管理某个数据库的权限，可以授予这个数据库的所有权限。

    grant all on db_name.* to 'dba'@'localhost';

假设，需要让超级管理员管理所有数据库的权限。

    grant all on *.* to 'dba'@'localhost';

假设，需要让超级管理员管理所有数据库的权限，赋予远程权限。

    grant all on *.* to 'dba'@'192.168.244.142' identified by 'mypassword' with grant option;

    grant all privileges on *.* to 'jtsec'@'192.168.8.123' identified by 'jtsec' with grant option;

    select user,host from mysql.user;

    show grants for 'root'@'192.168.8.123';

    show grants for 'root'@'%';
```

### 赋予远程访问权限

```
mysql listen on 0.0.0.0

mysql> grant all privileges on *.* to 'root'@'%' identified by 'yunhe' with grant option;
Query OK, 0 rows affected, 1 warning (0.00 sec)

mysql> flush privileges;
Query OK, 0 rows affected (0.00 sec)

mysql> 
```

## REVOKE 收回用户权限

```
撤销已经赋予给 MySQL 用户权限的权限。

回收用户权限，和授予用户权限类似，只需要把关键字 to 改成 from 即可。

    REVOKE <权限>

    ON <数据库对象>

    FROM <用户>

假设，需要收回普通 DBA 某个数据库的删除权限。

    revoke delete on db_name.* from 'dba'@'localhost';

revoke 跟 grant 的语法差不多, 只需要把关键字 "to" 换成 "from" 即可:

    revoke all on *.* from 'root'@'192.168.0.197';

REVOKE语句只能取消用户的权限，而不可以删除用户。
即使取消了所有的权限，用户仍然可以连接到服务器。
要想彻底的删除用户，必须使用DELETE语句将该用户的记录从MySQL数据库中的user表中删除。
该语句的语法格式如下： 

    Delete from user where user = "user_name" and host = "host_name" ; 

例子：

    mysql; use mysql;
    Database changed

    delete from user where user='sss' and host='localhost';
    flush privileges;

    Query OK, 1 row affected (0.02 sec)

不要让懒惰占据你的大脑，不让要妥协拖跨你的人生。青春就是一张票，能不能赶上时代的快车，你的步伐掌握在你的脚下。
```

## 数据库安全原则
```
对于数据库安全问题，需要遵守几个原则：

    遵守最小特权，授予所需要的最小权限。
    如果用户只需要查询权限，就不要额外授予新增、更新、删除权限，这样可以防止用户干坏事。

    需要定期回收权限或者删除无用用户。

    创建用户的时候限制用户的登录主机，例如限制指定 IP 或内网 IP 网段。
```

## 修改用户名密码
```
格式：mysqladmin -u用户名 -p旧密码 password 新密码

命令行修改root密码：

    mysql> UPDATE mysql.user SET password=PASSWORD(’新密码’) WHERE User=’root’;

    mysql> FLUSH PRIVILEGES;

显示当前的user：

    mysql> SELECT USER();
```

