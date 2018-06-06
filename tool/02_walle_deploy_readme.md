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
		1. 查看配置文件中 user 的值。
			vim /etc/php/7.0/fpm/pool.d/www.conf
				user = www-data
				group = www-data
				
		2. 查看进程
			bwhite@os:/etc/php/7.0/fpm/pool.d$ ps aux | grep php
root     15168  0.0  0.2 279852 21600 ?        Ss   6月05   0:06 php-fpm: master process (/etc/php/7.0/fpm/php-fpm.conf)
www-data 15171  0.0  0.2 286800 19052 ?        S    6月05   0:05 php-fpm: pool www
bwhite   20837  0.0  0.0  15964   968 pts/1    S+   11:01   0:00 grep --color=auto php
www-data 22233  0.0  0.2 282404 16912 ?        S    6月05   0:00 php-fpm: pool www
www-data 22239  0.0  0.2 282420 17116 ?        S    6月05   0:00 php-fpm: pool www

	所以就需要将 www-data 的 public key 添加到 gitlab 中以拉取代码。
	那么我们就要切换到 www-data 用户，在用ssh-keygen生成 key。
	
	修改 /etc/passwd 文件:
        www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
        修改为:
        www-data:x:33:33:www-data:/home/www-data:/bin/bash
        
    创建 /home/www-data 目录并将拥有者修改为 www-data:
    	$ sudo mkdir /home/www-data
    	$ sudo chown -R www-data:www-data /home/www-data
	
	切换用户:
		$ su - www-data
	
	生成 www-data 用户的 ssh key
		$ ssh-keygen
		
	将 ~/.ssh/id_rsa.pub 中的内容添加到 gitlab 项目的 Deploy Keys 中，测试可以拉取代码即可。	
```





















