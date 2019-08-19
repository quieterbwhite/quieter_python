### Docker安装官方Redis镜像并启用密码认证 实践笔记

2018年06月18日 20:11:25

>   https://blog.csdn.net/cookily_liangzai/article/details/80726163

#### 参考：docker官方redis文档

#### 1.有特殊版本需求的可以查看redis镜像tag版本

```shell
3.2.11, 3.2, 3 (3.2/Dockerfile)
3.2.11-32bit, 3.2-32bit, 3-32bit (3.2/32bit/Dockerfile)
3.2.11-alpine, 3.2-alpine, 3-alpine (3.2/alpine/Dockerfile)
4.0.9, 4.0, 4, latest (4.0/Dockerfile)
4.0.9-32bit, 4.0-32bit, 4-32bit, 32bit (4.0/32bit/Dockerfile)
4.0.9-alpine, 4.0-alpine, 4-alpine, alpine (4.0/alpine/Dockerfile)123456
```

#### 2.选择最新版latest

```shell
docker pull redis:latest1
```

```shell
[root@localhost~]# docker pull redis:latest
latest: Pulling from library/redis
4d0d76e05f3c: Pull complete 
cfbf30a55ec9: Pull complete 
82648e31640d: Pull complete 
fb7ace35d550: Pull complete 
497bf119bebf: Pull complete 
89340f6074da: Pull complete 
Digest: sha256:166788713c58c2db31c41de82bbe133560304c16c70e53a53ca3cfcf35467d8a
Status: Downloaded newer image for redis:latest12345678910
```

#### 3.启动容器并带密码

```shell
docker run --name redis-test -p 6379:6379 -d --restart=always redis:latest redis-server --appendonly yes --requirepass "your passwd"1

docker run --name redis-bloom -p 6379:6379 -v $PWD/data:/data:rw -d --restart=always redis:latest redis-server --appendonly yes
```

>   -p 6379:6379 :将容器内端口映射到宿主机端口(右边映射到左边) 
>   redis-server –appendonly yes : 在容器执行redis-server启动命令，并打开redis持久化配置 
>   requirepass “your passwd” :设置认证密码 
>   –restart=always : 随docker启动而启动

#### 4.查看容器

```shell
docker ps1
```

```shell
[root@localhost~]# docker ps
CONTAINER ID        IMAGE                     COMMAND                  CREATED             STATUS              PORTS                                          NAMES
a126ec987cfe        redis:latest              "docker-entrypoint.s…"   4 minutes ago       Up 4 minutes        0.0.0.0:6379->6379/tcp                         redis-test
3645da72ece6        portainer/portainer       "/portainer"             7 days ago          Up 7 days           0.0.0.0:9000->9000/tcp                         sharp_lovelace
118ba79de20a        hwdsl2/ipsec-vpn-server   "/opt/src/run.sh"        12 days ago         Up 12 days          0.0.0.0:500->500/udp, 0.0.0.0:4500->4500/udp   l2tp-vpn-server
848fdba6de60        kylemanna/openvpn         "ovpn_run"               12 days ago         Up 12 days          1194/udp, 0.0.0.0:1194->1194/tcp               openvpn
a273504f9646        mysql:5.6.38              "docker-entrypoint.s…"   8 weeks ago         Up 5 days           0.0.0.0:3306->3306/tcp                         mysql5.6.381234567
```

>   redis容器的id是 a126ec987cfe

#### 5.查看进程

```shell
ps -ef|grep redis1
```

```shell
[root@localhost~]# ps -ef|grep redis
polkitd  26547 26535  0 14:58 ?        00:00:00 redis-server *:6379
root     26610 26432  0 15:05 pts/0    00:00:00 grep --color=auto redis123
```

#### 6.进入容器执行redis客户端

```shell
docker exec -it a126ec987cfe redis-cli -a 'your passwd'1
```

```shell
[root@localhost~]# docker exec -it a126ec987cfe redis-cli -h 127.0.0.1 -p 6379 -a 'your passwd'
127.0.0.1:6379> ping
PONG
127.0.0.1:6379> info
# Server
redis_version:4.0.9
redis_git_sha1:00000000
redis_git_dirty:0
redis_build_id:d3ebfc7feabc1290
redis_mode:standalone
os:Linux 3.10.0-693.21.1.el7.x86_64 x86_64
...123456789101112
```

>   -h 127.0.0.1 :默认不加为-h 127.0.0.1 
>   -p 6379 :默认不加为 -p 6379

#### 或者连接的时候不带密码,如下：

```shell
[root@localhost ~]# docker exec -it a126ec987cfe redis-cli
127.0.0.1:6379> ping
(error) NOAUTH Authentication required.
127.0.0.1:6379> auth 'your passwd'
OK
127.0.0.1:6379> ping
PONG
127.0.0.1:6379> info
# Server
redis_version:4.0.9
redis_git_sha1:00000000
redis_git_dirty:0
redis_build_id:d3ebfc7feabc1290
redis_mode:standalone
os:Linux 3.10.0-693.21.1.el7.x86_64 x86_64
arch_bits:6412345678910111213141516
```
