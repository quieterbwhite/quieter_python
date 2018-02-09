# max client

## 计算方式 服务器
```
max_client = worker_processes * worker_connections

在 Nginx 充当服务器(例如 Nginx 上面装载 PHP )时, Nginx 可同
时承载的连接数量是最大工作线程×每个线程允许的连接数量


```

## 计算方式 反向代理
```
max_client = worker_processes * worker_connections / 4

    当 Nginx 充当反向代理服务时，其可同时承载的连接数量是
    最大工作线程×每个线程允许的连接数量/4

这里为什么要除以4呢？

有说法是:

    浏览器连接到Nginx, Nginx连接到后端服务器，后端服务器再连接到Nginx，Nginx最后连接
    到浏览器，所以需要除以4.

    但TCP是双向全双工通信，是不需要这样连接的。所以这个说法是错误的。

官方描述是这样的:

    Since a browser opens 2 connections by default to a server and nginx
    uses the fds(file description) from the same pool to connect to the upstream backend.

    也就是，浏览器会建立两条连接到 Nginx(注意两条连接都是浏览器建立的),
    Nginx 也会建立对应的两条连接到后端服务器，这样就是4条连接了。
```
