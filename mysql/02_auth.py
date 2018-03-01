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
```

## REVOKE 收回用户权限
```
回收用户权限，和授予用户权限类似，只需要把关键字 to 改成 from 即可。

    REVOKE <权限>

    ON <数据库对象>

    FROM <用户>

假设，需要收回普通 DBA 某个数据库的删除权限。

    revoke delete on db_name.* from 'dba'@'localhost';
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

