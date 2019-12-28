# imooc nginx

```
nginx.org

各发行版安装方法
nginx.org/en/linux_packages.html#stable

nginx -v  查看版本
nginx -V  查看安装命令
```

```
为什么选择Nginx

IO多路复用 epoll

轻量级

CPU亲和 affinity
    是一种把CPU核心和Nginx工作进程绑定的方式，
    把每个worker进程固定在一个cpu上执行，
    减少切换cpu的cache miss，获得更好的性能。

sendfile

    0拷贝，文件直接在用户空间操作，不需要走一遍内核空间
```

```
安装目录详解

/etc/logrotate.d/nginx

    配置文件
    Nginx日志轮转，用于logrotate服务的日志切割

/etc/nginx/fastcgi_params
/etc/nginx/uwsgi_params
/etc/nginx/scgi_params

    配置文件
    cgi配置相关，fastcgi配置

/etc/nginx/mime.types

    配置文件
    设置http协议的Content-Type与扩展名对应关系
```

```
修改nginx日志信息

vim /etc/nginx/nginx.conf
http {
    log_format main '$remote_addr';
}
```

```
Nginx 模块

编译参数里面的 --with-xx 就是编译进去的模块

通过页面获取nginx简单状态信息

随机主页

--with-http_sub_module HTTP 内容替换
    在nginx里面替换页面内容，没用吧。这东西。

-limit_conn_module  连接频率限制

-limit_req_module   请求频率限制

http1.0 TCP不能复用
http1.1 顺序TCP复用
http2.0 多路复用TCP复用

http 请求建立在一次TCP连接基础上
一次TCP请求至少产生一次HTTP请求

基于IP的访问控制    - http_access_module
基于用户的信任登录   - http_auth_basic_module

对单一ip的限制
针对ip限制并发请求
配置白名单 - 针对特定ip不做请求限制

```

```
http_access_module 局限性

1. 采用别的http头控制访问，如，HTTP_X_FORWARD_FOR
2. 结合geo模块
3. 通过http自定义变量控制
```

```
tcp_nopush
sendfile, 文件传输内核优化, 0拷贝
作用， sendfile 开启的情况下，提高网络包的传输效率。
整合多个包批量发送, 大文件推荐打开

tcp_nodelay
数据包不要等待，实时发送
作用，http keeplive连接下，提高网络包的传输实时性
```