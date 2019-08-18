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

docker run --name redis-app -p 6379:6379 -v $PWD/data:/data -d --restart=always redis:latest redis-server --appendonly yes
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

#### 使用Docker搭建Redis集群
```shell
# 参考爱租房项目第七章文档.

#拉取镜像
docker pull redis:5.0.2

#创建容器
docker create --name redis-node01 -v /data/redis-data/node01:/data -p 6379:6379
redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-01.conf

docker create --name redis-node02 -v /data/redis-data/node02:/data -p 6380:6379
redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-02.conf

docker create --name redis-node03 -v /data/redis-data/node03:/data -p 6381:6379
redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-03.conf

#启动容器
docker start redis-node01 redis-node02 redis-node03

#开始组建集群

#进入redis-node01进行操作
docker exec -it redis-node01 /bin/bash

#组建集群
redis-cli --cluster create 172.17.0.1:6379 172.17.0.1:6380 172.17.0.1:6381 --
cluster-replicas 0

如果出现不能连接问题:

尝试使用容器的ip地址(172.17.0.1这个地址是docker容器分配给主机的地址):

#查看容器的ip地址
docker inspect redis-node01  ->  172.17.0.4
docker inspect redis-node02  ->  172.17.0.5
docker inspect redis-node03  ->  172.17.0.6

#删除容器
docker stop redis-node01 redis-node02 redis-node03
docker rm redis-node01 redis-node02 redis-node03
rm -rf /data/redis-data

#进入redis-node01进行操作
docker exec -it redis-node01 /bin/bash

#组建集群(注意端口的变化)
redis-cli --cluster create 172.17.0.4:6379 172.17.0.5:6379 172.17.0.6:6379 --
cluster-replicas 0

发现,搭建成功


#查看集群信息:
root@91df3e5228b1:/data# redis-cli
127.0.0.1:6379> CLUSTER NODES
207a4d90dce0857e26a2add4ed9fd07464ab02d5 172.17.0.5:6379@16379 master - 0
1543765218866 2 connected 5461-10922

eaaf2895fde3422c522defe6751e3de88d54a553 172.17.0.6:6379@16379 master - 0
1543765217856 3 connected 10923-16383

7eb19b3a82216880b61593e59bebefa5edc247a0 172.17.0.4:6379@16379 myself,master - 0
1543765218000 1 connected 0-5460

可以看到,集群中节点的ip地址是docker分配的地址,那么在客户端(spring-data-redis)是没有办法访问的?如
何解决?
5.2、docker的网络类型
docker的网络类型有:
None:不为容器配置任何网络功能,没有网络 --net=none
Container:与另一个运行中的容器共享Network Namespace,--net=container:containerID
Host:与主机共享Network Namespace,--net=host
Bridge:Docker设计的NAT网络模型(默认类型)
重点关注下Host类型:
host模式创建的容器没有自己独立的网络命名空间,是和物理机共享一个Network Namespace,并且共享物理机
的所有端口与IP。但是它将容器直接暴露在公共网络中,是有安全隐患的。

5.3、使用host网络进行搭建集群
#创建容器
docker create --name redis-node01 --net host -v /data/redis-data/node01:/data
redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-01.conf --port 6379

docker create --name redis-node02 --net host -v /data/redis-data/node02:/data
redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-02.conf --port 6380

docker create --name redis-node03 --net host -v /data/redis-data/node03:/data
redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-03.conf --port 6381

#启动容器
docker start redis-node01 redis-node02 redis-node03

#进入redis-node01容器进行操作
docker exec -it redis-node01 /bin/bash
#172.16.55.185是主机的ip地址

redis-cli --cluster create 172.16.55.185:6379 172.16.55.185:6380 172.16.55.185:6381
--cluster-replicas 0

查看集群信息:
root@itcast:/data# redis-cli
127.0.0.1:6379> CLUSTER NODES
46e5582cd2d96a506955cc08e7b08343037c91d9 172.16.55.185:6380@16380 master - 0
1543766975796 2 connected 5461-10922

b42d6ccc544094f1d8f35fa7a6d08b0962a6ac4a 172.16.55.185:6381@16381 master -0 1543766974789 3 connected 10923-16383

4c60f45d1722f771831c64c66c141354f0e28d18 172.16.55.185:6379@16379 myself,master -0 1543766974000 1 connected 0-5460
```