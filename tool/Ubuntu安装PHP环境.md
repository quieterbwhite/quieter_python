# Ubuntu 安装 PHP 环境

## 安装
```
安装 PHP7.0和php7.0-fpm

    $ sudo aptitude install php7.0 php7.0-fpm php7.0-dev
```

## 安装扩展 mysql
```
$ sudo aptitude install php7.0-mysql

源码编译扩展

    1. 首先下载[mysql扩展](https://git.php.net/?p=pecl/database/mysql.git;a=summary)

    2. 解压

        $ tar zxvf mysql.tar.gz

    3. 编译

        $ phpize
        $ ./configure
        $ make

        在 modules 目录下生成了一个 mysql.so 文件
        
    4. php 配置文件添加mysql扩展

        sudo vim /etc/php/7.0/fpm/php.ini

        # 添加一行
        extension=/path/to/mysql.so

        # 重启 php-fpm
        sudo systemctl restart php7.0-fpm
```

## 安装扩展 gd
```
$ sudo aptitude install php7.0-gd
```

## 修改 php.ini 开启扩展
```
$ sudo vim /etc/php/7.0/fpm/php.ini

开启:
    extension=php_mysql.dll
    extension=php_mysqli.dll
    extension=php_gd2.dll

添加:
    extension=/path/to/mysql.so
```

## Nginx 配置文件
```
server {

    listen 80;

    server_name localhost;

    root /home/bwhite/Downloads/yunhe_web;

    index index.php;

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











