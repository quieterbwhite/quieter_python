## Java开发



### 搭建环境

```bash
1. 安装操作系统，更换系统源为 aliyun
2. 安装 JDK
3. 安装 Tomcat
	修改默认编码为 utf-8
	vim /home/bwhite/software/apache-tomcat-8.5.30/conf/server.xml
	<Connector port="8080" protocol="HTTP/1.1"
               connectionTimeout="20000"
               redirectPort="8443" URIEncoding="UTF-8" />  # 添加URIEncoding字段
               
    验证 tomcat
    cd /home/bwhite/software/apache-tomcat-8.5.30/bin
    $ ./startup.sh
    
4. maven
	查看版本: mvn -version
	清楚命令: mvn clean
	编译命令: mvn compile
	打包命令: mvn package
	跳过单元测试: mvn clean package -Dmaven.test.skip=true
```

### vsftpd ftp服务器

```bash
vsftpd 是 "very secure FTP daemon" 的缩写，是一个完全免费的开放源代码的ftp服务器软件。
	 
vsftpd 是一款在Linux发行版中最受推崇的FTP服务器程序，小巧轻快，安全易用，支持虚拟用户，支持带宽限制等功能。

**安装**
$ sudo aptitude install vsftpd

/system.slice/vsftpd.service
└─25890 /usr/sbin/vsftpd /etc/vsftpd.conf

**创建虚拟用户**
1. 创建 ftp 文件夹, /home/bwhite/work/ftpfile
2. 添加匿名用户 sudo useradd ftpuser -d /home/bwhite/work/ftpfile -s /sbin/nologin
3. 修改ftpfile权限 sudo chown -R ftpuser:ftpuser /home/bwhite/work/ftpfile
4. 重设ftpuser密码 sudo passwd ftpuser -> 123456

**配置**
1. cd /home/bwhite/work/
2. sudo vim chroot_list
3. 把刚才新增的虚拟用户添加到此配置文件中，后续要引用。就是把 "ftpuser" 写到该文件中
4. sudo vim /etc/selinux/config, 修改为　SELINUX=disabled, 也就是关闭防火墙
	如果验证的时候碰到550拒绝访问请执行:
	sudo setsebool -P ftp_home_dir 1
5. 重启服务器
我没有实现这一部分，现在没人用fpt来处理文件了呀。到时候项目中不处理或用其他方式处理.
```

### Nginx

```
增加防火墙访问权限
1. sudo vim /etc/sysconfig/iptables
2. -A INPUT -p tcp -m state --state NEW -m tcp --dport 80 -j ACCEPT
3. 重启防火墙 sudo service iptables restart
```

### MySQL

```bash
 **字符集设置**
 
 1. vim /etc/mysql/mysql.conf.d/mysqld.cnf
 2. 添加配置，在[mysqld]节点下添加:
	character-set-server=utf8

**防火墙配置**
1. sudo vim /etc/sysconfig/iptables
2. -A INPUT -p tcp -m tcp --dport 3306 -j ACCEPT
	将以上配置添加到防火墙配置中 
3. sudo service iptables restart 重启防火墙

**mysql** 配置
1. 查看目前MySQL用户
	> select user,host from mysql.user;
2. 修改root密码:
	> set password for root@localhost=password('tiger');
3. 插入新用户
	> insert into mysql.user(Host, User, Password) values("localhost", "yourusername", password("yourpassword"));
4. 使操作生效
	> flush privileges;
5. 创建新的database
	> create database 'mmall' default character set utf8 collate utf8_general_ci;
6. 本地用户赋予所有权限
	> grant all privileges on mmall.* to yourusername@localhost identified by 'yourpassword';
7. 给账号开通外网所有权限
	> grant all privileges on mmall.* to 'yourusername'@'%' identified by 'yourpassword';
	根据自己的实际情况决定是否开什么权限
	> grant select,insert,update on mmall.* to yourusername@'192.11.11.11' identified by 'yourpassword';
	# 代码只开通了增改查给指定的账号，并也指定了ip地址
	> flush privileges;
```



















