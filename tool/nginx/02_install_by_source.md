# Nginx install

## 源码安装目录
```
$ wget http://nginx.org/download/nginx-1.8.0.tar.gz

$ tar -zxvf ./nginx-1.8.0.tar.gz

$ cd ./nginx-1.8.0

$ ./configure --prefix=/usr/nginx-1.8.0

    如果使用 prefix 设置了安装目标目录，那么可能还需要设置环境变量

$ make && make install
```

## apt 安装
```
$ sudo apt install nginx
```

## 常用命令
```
nginx 启动nginx
nginx -t 检查配置文件
nginx -s reload 重新加载/重启
nginx -s stop 停止
```
