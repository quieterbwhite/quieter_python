# Jira安装破解
> https://www.jianshu.com/p/0da8a0a615da  
> https://www.jianshu.com/p/52656bbc1757  Confluence安装破解  

## 环境
```
ubuntu16.04
atlassian-jira-software-7.8.0-x64.bin
mysql-connector-java-5.1.45.tar.gz 需解压提取 jar 文件
相关文件在我的百度云 /installer/jira 里面
```

## 安装
```
下载bin包

    地址：https://www.atlassian.com/software/jira/download

安装

$ chmod +x atlassian-jira-software-7.8.0-jira-7.8.0-x64.bin
$ ./atlassian-jira-software-7.8.0-jira-7.8.0-x64.bin

This will install JIRA Software 7.8.0 on your computer.
OK [o, Enter], Cancel [c]
按o安装

Choose the appropriate installation or upgrade option.
Please choose one of the following:
Express Install (use default settings) [1], Custom Install (recommended for advanced users) [2, Enter], Upgrade an existing JIRA installation [3]
按1默认安装，按2定制安装路径和端口

Details on where JIRA Software will be installed and the settings that will be used.
Installation Directory: /opt/atlassian/jira
Home Directory: /var/atlassian/application-data/jira
HTTP Port: 8080
RMI Port: 8005
Install as service: Yes
Install [i, Enter], Exit [e]
按i安装
```

## 安装mysql
```
安装mysql

    参见：http://www.jianshu.com/p/17ca1b54b41c

创建jira数据库

    > CREATE DATABASE jira CHARACTER SET utf8 COLLATE utf8_bin;
```

## MySQL JDBC driver安装
```
下载二进制包

    地址：http://dev.mysql.com/downloads/connector/j/

安装

    $ tar -xzvf mysql-connector-java-5.1.38.tar.gz
    $ cp mysql-connector-java-5.1.38/mysql-connector-java-5.1.38-bin.jar /opt/atlassian/jira/lib/

重启jira

    $ /etc/init.d/jira stop

    $ /etc/init.d/jira start
```

## jira初始化
```
访问http://ip:8080， 填选以下信息

I’ll set it up myself
My Own Database
填写数据库信息
填写网站信息
注册License
填写管理员信息
......

中间会让填注册码，我们没有。
就照他的提示去他的网站上注册，输入刚填写的应用名称生成一个试用版注册码。
后文会有破解步骤。
```

## jira破解
```
安装破解包

$ cp atlassian-extras-3.2.jar /opt/atlassian/jira/atlassian-jira/WEB-INF/lib/
$ /etc/init.d/jira stop
$ /etc/init.d/jira start

我百度云上的破解文件解压过后是 3.1.2 版本，只需把破解文件重命名到 3.2 版本就可以了。
```
