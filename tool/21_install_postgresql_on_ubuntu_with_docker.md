### docker安装PostgreSQL

>   https://blog.csdn.net/liuyueyi1995/article/details/61204205

2017年03月10日 19:14:10

#### 0 任务简介

-   在`Ubuntu 16.04`虚拟机中安装`docker`
-   使用`docker`安装`PostgreSQL`
-   完成端口映射使得外部机器可以访问虚拟机中的数据库

#### 1 安装docker

这一部分比较简单，不过考虑到完整性，还是列出来吧。 
我这次选择的是`docker-ce`，安装流程如下：

##### 1.1 建立 repository

```
sudo apt-get install apt-transport-https ca-certificates curl software-properties-common1
```

```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -1
```

```
sudo apt-key fingerprint 0EBFCD881
```

```
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"1
```

##### 1.2 安装docker

```
sudo apt-get update1
```

```
sudo apt-get install docker-ce1
```

#### 2 安装PostgreSQL

```
docker pull postgres:9.41
```

#### 3 创建容器

docker的容器默认情况下只能由本地主机访问，即A主机上的容器不能被B主机访问，所以要做端口映射。

```
docker run --name postgres1 -e POSTGRES_PASSWORD=password -p 54321:5432 -d postgres:9.4 1
```

解释： 
`run`，创建并运行一个容器； 
`--name`，指定创建的容器的名字； 
`-e POSTGRES_PASSWORD=password`，设置环境变量，指定数据库的登录口令为`password`； 
`-p 54321:5432`，端口映射将容器的5432端口映射到外部机器的54321端口； 
`-d postgres:9.4`，指定使用`postgres:9.4`作为镜像。

##### 3.1 验证结果

之后运行`docker ps -a`，结果和下表类似：

CONTAINER IDIMAGECOMMANDCREATEDSTATUSPORTSNAMESf6951e0c5c77postgres:9.4“docker-entrypoint…”38 minutes agoUp 38 minutes0.0.0.0:54321->5432/tcppostgres1

##### 3.2 关键点

我自己安装的过程中遇到了不少的坑，我认为最重要的一点是docker命令中**参数的顺序**。

例如端口映射的`-p 54321:5432`的位置如果过于靠后，则会导致映射失败。

#### 4 连接数据库

之前的准备工作都已完成，下一步就是从外部访问数据库了。 
这一步就很常规了：

```
psql -U postgres -h 192.168.100.172 -p 543211
```

**注意**： 
postgres镜像默认的用户名为`postgres`， 
登陆口令为创建容器是指定的值。

#### 5 参考文献

[1][docker官网](https://docs.docker.com/engine/installation/linux/ubuntu/) 
[2] [postgres镜像官方文档](https://hub.docker.com/_/postgres/) 
[3] [非常详细的 Docker 学习笔记](http://www.open-open.com/lib/view/open1423703640748.html)