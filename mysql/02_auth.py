# Mysql 安装 及 权限管理

## 修改用户名密码
```
格式：mysqladmin -u用户名 -p旧密码 password 新密码

命令行修改root密码：
    mysql> UPDATE mysql.user SET password=PASSWORD(’新密码’) WHERE User=’root’;
    mysql> FLUSH PRIVILEGES;

显示当前的user：
    mysql> SELECT USER();
```

## Install mysql
```
apt-get update

apt-get install mysql-server

Now we’ll instruct MySQL to create its database directory structure: mysql_install_db

And now let’s secure MySQL by removing the test databases and anonymous user created by default: mysql_secure_installation

Then, assuming you set a strong root password, go ahead and enter n at the following prompt:

    Change the root password? [Y/n] n
    Remove anonymous users, Y:
    Remove anonymous users? [Y/n] Y
    Disallow root logins remotely, Y:
    Disallow root login remotely? [Y/n] Y
    Remove test database and access to it, Y:
    Remove test database and access to it? [Y/n] Y
    And reload privilege tables, Y:
    Reload privilege tables now? [Y/n] Y

You can check the version of the MySQL installation with the following command:  mysql -V

mysql>

Exit the command line with the following command:  exit
To stop MySQL:  service mysql stop
To start MySQL:  service mysql start
To check the status of MySQL:  service mysql status
To restart MySQL:  service mysql restart

安装 Mysql workbench: sudo apt-get install mysql-workbench

服务器连接错误Host 'XXX' is not allowed to connect to this MySQL server:

本地计算机ip：192.168.1.100
远程计算机ip：192.168.1.244
 远程计算机打开 mysql 服务器：#/etc/init.d/mysql.server start
   本地计算机连接远程 mysql服务器：./mysql -h "192.168.1.244" -u root -p
   发生以下错误：
   ERROR 1130 (HY000): Host '192.168.1.100' is not allowed to connect to this MySQL server

出现这种情况是因为mysql服务器出于安全考虑，默认只允许本地登录数据库服务器。
解决方法：
1，远程计算机(ip:192.168.1.244)执行如下：
   开启服务器：/etc/init.d/mysql.server start
   登陆服务器：bin/mysql -u root -p
   使用服务器：mysql> use mysql
   创建远程登陆用户并授权 :
   mysql> grant all PRIVILEGES on test.* to andy@'192.168.1.100' identified by '123456';
上面的语句表示将 test 数据库的所有权限授权给 andy 这个用户，允许 andy 用户在 192.168.1.100这个 IP 进行远程登陆，并设置 andy 用户的密码为 123456 。
下面逐一分析所有的参数：
all PRIVILEGES 表示赋予所有的权限给指定用户，这里也可以替换为赋予某一具体的权限，例如：select,insert,update,delete,create,drop 等，具体权限间用“,”半角逗号分隔。
test.* 表示上面的权限是针对于哪个表的，test 指的是数据库，后面的 * 表示对于所有的表，由此可以推理出：对于全部数据库的全部表授权为“*.*”，对于某一数据库的全部表授权为“数据库名.*”，对于某一数据库的某一表授权为“数据库名.表名”。
andy 表示你要给哪个用户授权，这个用户可以是存在的用户，也可以是不存在的用户
192.168.1.100 表示允许远程连接的 IP 地址，如果想不限制链接的 IP 则设置为“%”即可
123456 为用户的密码
执行了上面的语句后，再执行下面的语句，方可立即生效。
    > flush privileges;
2，本地计算机(ip:192.168.1.100)：
   执行如下：./mysql -h 192.168.1.244 -u andy -p 123456

例如，你想myuser使用mypassword从任何主机连接到mysql服务器的话。
GRANT ALL PRIVILEGES ON *.* TO 'myuser'@'%' IDENTIFIED BY 'mypassword' WITH GRANT OPTION;
FLUSH   PRIVILEGES;
如果你想允许用户myuser从ip为192.168.1.6的主机连接到mysql服务器，并使用mypassword作为密码
GRANT ALL PRIVILEGES ON *.* TO 'myuser'@'192.168.1.3' IDENTIFIED BY 'mypassword' WITH GRANT OPTION;
FLUSH   PRIVILEGES;
如果你想允许用户myuser从ip为192.168.1.6的主机连接到mysql服务器的dk数据库，并使用mypassword作为密码
GRANT ALL PRIVILEGES ON dk.* TO 'myuser'@'192.168.1.3' IDENTIFIED BY 'mypassword' WITH GRANT OPTION;
FLUSH   PRIVILEGES;
```
