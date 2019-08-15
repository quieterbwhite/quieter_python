# [ docker 安装部署 redis（配置文件启动）](https://segmentfault.com/a/1190000014091287)

- [docker](https://segmentfault.com/t/docker/blogs)
- [redis](https://segmentfault.com/t/redis/blogs)

## 安装 docker

[修订]docker 已分为 ce/ee 直接yum版本较低 请使用下方安装最新版

docker-ce yum 安装：[https://www.cnblogs.com/Peter...](https://www.cnblogs.com/Peter2014/p/7704306.html)（转）或使用 daocloud 安装：[http://get.daocloud.io/#insta...](http://get.daocloud.io/#install-docker)

```
# 2019-1-24 注明：
#安装 docker
yum install docker -y

systemctl start docker.service
```

## 获取 redis 镜像

```
docker search redis

docker pull redis:latest

docker images
```

## 创建容器

创建宿主机 redis 容器的数据和配置文件目录

```
# 这里我们在 /home/docker 下创建
mkdir /home/docker/redis/{conf,data} -p
cd /home/docker/redis
```

获取 redis 的默认配置模版

```
# 获取 redis 的默认配置模版
# 这里主要是想设置下 redis 的 log / password / appendonly
# redis 的 docker 运行参数提供了 --appendonly yes 但没 password
wget https://raw.githubusercontent.com/antirez/redis/4.0/redis.conf -O conf/redis.conf

# 直接替换编辑
sed -i 's/logfile ""/logfile "access.log"/' conf/redis.conf
sed -i 's/# requirepass foobared/requirepass 123456/' conf/redis.conf
sed -i 's/appendonly no/appendonly yes/' conf/redis.conf

# 这里可能还需配置一些 bind protected-mode
```

> protected-mode 是在没有显示定义 bind 地址（即监听全网断），又没有设置密码 requirepass
> 时，protected-mode 只允许本地回环 127.0.0.1 访问。
> 也就是说当开启了 protected-mode 时，如果你既没有显示的定义了 bind 监听的地址，同时又没有设置 auth 密码。那你只能通过 127.0.0.1 来访问 redis 服务。

创建并运行一个名为 myredis 的容器

```
# 创建并运行一个名为 myredis 的容器
docker run \
-p 6379:6379 \
-v $PWD/data:/data \
-v $PWD/conf/redis.conf:/etc/redis/redis.conf \
--privileged=true \
--name myredis \
-d redis redis-server /etc/redis/redis.conf

# 命令分解
docker run \
-p 6379:6379 \ # 端口映射 宿主机:容器
-v $PWD/data:/data:rw \ # 映射数据目录 rw 为读写
-v $PWD/conf/redis.conf:/etc/redis/redis.conf:ro \ # 挂载配置文件 ro 为readonly
--privileged=true \ # 给与一些权限
--name myredis \ # 给容器起个名字
-d redis redis-server /etc/redis/redis.conf # deamon 运行容器 并使用配置文件启动容器内的 redis-server 
```

查看活跃的容器

```
# 查看活跃的容器
docker ps
# 如果没有 myredis 说明启动失败 查看错误日志
docker logs myredis
# 查看 myredis 的 ip 挂载 端口映射等信息
docker inspect myredis
# 查看 myredis 的端口映射
docker port myredis
```

## 外部访问 redis 容器服务

```
# redis-cli 访问
docker run -it --link myredis:redis --rm redis redis-cli -h redis -p 6379
# -it 交互的虚拟终端
# --rm 退出是删除此容器
```

或者使用 shell 登录容器内操作

```
docker exec -it myredis bash
redis-cli
```

配置完成

## 主从配置

新建容器 redis-slave
查看 redis master 的内部 ip

```
docker inspect redis #Networks
可以得到 redis master 的 ip 地址
"NetworkSettings": {
            "Ports": {
                "6379/tcp": [
                    {
                        "HostIp": "0.0.0.0",
                        "HostPort": "6379"
                    }
                ]
            },
            ...
            "Gateway": "192.168.0.1",
            ...
            "IPAddress": "192.168.0.3",#ip
            ...
            "Networks": {
                "bridge": {
                    ...
                    "Gateway": "192.168.0.1",
                    "IPAddress": "192.168.0.3",#ip
                    ...
                }
            }
        }


修改 redis-slave 的配置文件
# 主地址
slaveof master-ip master-port
# 主认证
masterauth
```

重启 redis-slave

```
docker restart redis-slave
```

登录 redis master 使用 info 命令查看从的状态

如果配置不成功记得检查 redis master 的 bind 和 protected-mode 的设置，看下有没有监听内网地址，否则 redis-slave 没办法通过 redis master 的地址做数据同步