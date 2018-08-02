# centos7中添加zookeeper.service 转

> https://my.oschina.net/u/2499632/blog/916646

[![今天来找bug](https://static.oschina.net/uploads/user/1249/2499632_50.jpg?t=1468545459000)  今天来找bug](https://my.oschina.net/u/2499632) 发布于 2017/06/07 20:01

### 在 

```
/usr/lib/systemd/system
```

### 目录下创建 `zookeeper.service` ,并填写如下内容：

```
[Unit]
Description=zookeeper.service
After=network.target
[Service]
Type=forking
Environment=/opt/zookeeper/
ExecStart=/opt/zookeeper/bin/zkServer.sh start
ExecStop=/opt/zookeeper/bin/zkServer.sh stop
ExecReload=/opt/zookeeper/bin/zkServer.sh restart
[Install]
WantedBy=multi-user.target
```

```
 
```

### 重新加载一下service

```
systemctl daemon-reload
```

# 说明

- [Unit]部分主要是对这个服务的说明，内容包括Description和After，Description用于描述服务，After用于描述服务类别
- [Service]部分是服务的关键，是服务的一些具体运行参数的设置，这里Type=forking是后台运行的形式，PIDFile为存放PID的文件路径，ExecStart为服务的具体运行命令，ExecReload为重启命令，ExecStop为停止命令，PrivateTmp=True表示给服务分配独立的临时空间，注意：[Service]部分的启动、重启、停止命令全部要求使用绝对路径，使用相对路径则会报错！
- [Install]部分是服务安装的相关设置，可设置为多用户的

### 使用：

- 重新加载配置信息：systemctl daemon-reload
- 启动zookeeper：systemctl start zookeeper.service
- 关掉zookeeper：systemctl stop zookeeper.service
- 查看进程状态及日志（重要）：systemctl status zookeeper.service
- 开机自启动：systemctl enable zookeeper.service
- 关闭自启动：systemctl disable zookeeper.service

 