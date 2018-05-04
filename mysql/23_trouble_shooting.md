# Mysql 问题

## Your password does not satisfy the current policy requirements
```
Because of your password. You can see password validate configuration metrics using SHOW VARIABLES LIKE 'validate_password%'; in mysql or you can set the password policy level lower, for example :

SET GLOBAL validate_password_length = 6;
SET GLOBAL validate_password_number_count = 0;
```

## mysql的远程访问
```
安装了MySQL默认是拒绝远程连接的。

首先进入数据库，使用系统数据库mysql。

$mysql -u root -p mysql #回车，然后输入则使用了系统数据库

接着对系统数据库的root账户设置远程访问的密码，与本地的root访问密码并不冲突。

    $grant all privileges on *.* to 'root'@'%' identified by '123456' with grant option; #123456为你需要设置的密码

防火墙设置一下，不然3306端口还是无法访问。

    $iptables -I INPUT -p tcp -m state --state NEW -m tcp --dport 3306 -j ACCEPT

设置完之后，查看一下是否能通过。

    $iptables -L -n

如果想要限制访问。

    $iptables -D INPUT -p tcp -m state --state NEW -m tcp --dport 3306 -j ACCEPT
```
