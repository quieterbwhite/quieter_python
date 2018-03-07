# Mysql 遇到的问题
> https://dzer.me/2016/05/04/ubuntu-%E5%BC%80%E5%90%AFmysql%E8%BF%9C%E7%A8%8B%E8%BF%9E%E6%8E%A5/  

## dns名称解析
```
mysql默认开启了dns名称解析的一项功能，会影响连接时间，可以通过关闭这个功能，实现跳过解析，从而加快连接请求。

可以看到似于这样的警告信息: “150713 14:15:14 [Warning] IP address ‘...‘ could not be resolved: Name or service not known” 。

在my.cnf配置文件中[mysqld]下增加 skip-name-resolve , 然后重启服务。

查看是否生效

    show variables like '%name%';
```

## 数据库用户表host字段请不要出现非ip的类型
```
值得注意的地方是，如果开启了这个功能，数据库用户表host字段请不要出现非ip的类型，否则会出现类似如下错误（比如有localhost）

/data/mysql/bin/mysqladmin: connect to server at ‘localhost’ failed
error: ‘Access denied for user ‘root’@’localhost’ (using password: YES)’
```

## 授权访问
```
授权访问，用root身份登录到mysql，使用grant命令分配权限，
如果操作所有库就把 database_name.* 改成 *.* ,user_name是用户名，%是所有ip地址可访问，如果限制固定ip访问就改成ip，user_password是密码

mysql -uroot -p
mysql> grant all on database_name.* to user_name@'%' identified by 'user_password';
mysql> flush privileges;     #让权限立即生效
```
