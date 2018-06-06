## 部署 Walle

> http://walle-web.io/docs/installation.html  walle 安装
>
> https://yq.aliyun.com/ziliao/54266   linux中给PHP进程用户noboby创建ssh-key并建立信任



### 1. 安装 LNMP 环境

```
操作系统: Ubuntu 16.04

数据库: Mysql 5.7

	$ sudo apt install mysql-server mysql-client

反向代理: Nginx

	$ sudo apt install nginx

PHP环境: PHP7.0

	$ sudo aptitude install php7.0 php7.0-fpm php7.0-dev
	
也可以使用 LNMP 一键安装包:

	https://lnmp.org/
	
```

### 2. 安装 Walle

```
1. 下载源码:
	$ mkdir -p /home/bwhite/work/walle && cd /home/bwhite/work/walle
	$ git clone git@github.com:meolu/walle-web.git
	
2. 修改数据库连接:
	$ cd /home/bwhite/work/walle/walle-web
	$ vim config/local.php
	
	# 修改数据库部分为你当前环境
	'db' => [
            'dsn' => isset(...) ? $_ENV['...']  : 'mysql:host=127.0.0.1;dbname=数据库名',
            'username'  => isset($_ENV['...']) ? $_ENV['...'] : '用户名',
            'password'  => isset($_ENV['...']) ? $_ENV['...'] : '密码',
        ],
```

### 3. 安装composer，如果已安装跳过

```
$ curl -sS https://getcomposer.org/installer | php
$ sudo mv composer.phar /usr/local/bin/composer
```

### 4. 安装vendor

```
方法一:
	$ cd walle-web
	$ composer install --prefer-dist --no-dev --optimize-autoloader -vvvv

方法二:
	下载解压到 walle-web 目录
	https://pan.baidu.com/s/1kU6gdZD
```

### 5. 初始化项目

```
$ cd walle-web
$ ./yii walle/setup
```

### 6. 配置 nginx

```
walle.conf

server {
    listen       8002;
    server_name  172.16.0.121; # 改你的host
    root /home/bwhite/work/walle/walle-web/web; # 根目录为web
    index index.php;

    # 建议放内网
    # allow 192.168.0.0/24;
    # deny all;

    location / {
        try_files $uri $uri/ /index.php$is_args$args;
    }

    location ~ \.php$ {
            include fastcgi.conf;
            include fastcgi_params;
            fastcgi_pass unix:/run/php/php7.0-fpm.sock;
    }
}
```

### 7. 访问

```
访问 http://172.16.0.121:8002 就能看到 walle 的登录页面

默认用户:
	
	admin : admin
	demo : demo
```

### 8. 使用 Walle - 检测项目

```
项目创建完成之后，在项目配置列表页可以对刚刚创建的项目进行检测。
大概就是 宿主机-测试环境-开发环境-Gitlab的连通性测试。

1. 建立机器之间的信任: 

	通过将宿主机的id_rsa.pub添加到其他环境中即可
	
2. PHP进程用户和Gitlab机器的ssh信任:

	通过WEB系统（基于PHP）操作git，也要建立PHP进程用户和Gitlab机器的ssh信任。
	
	有两种方式查看当前PHP进程用什么用户在运行:
		1. 
```





















