### Docker MongoDB 部署

>    [speculatecat](https://www.jianshu.com/u/98ea51905386)

MongoDB 是一款较为常用的NOSQL 数据库，结合 Docker 使用，能实现轻松配置部署、迁移，本文以下为简要介绍如何在 Docker 中部署并使用 MongoDB。下文主要分为几个部分，内容如下：

-   MongoDB 镜像安装
-   MongoDB 容器创建
-   MongoDB 容器数据目录挂载
-   MongoDB 数据迁移
-   MongoDB 常用 Docker 命令

## MongoDB Docker 镜像安装

MongoDB 提供官方镜像，下载安装镜像方法如下：

```
docker pull mongo
```

以上命令为安装 MongoDB 最新版本的镜像。

## MongoDB Docker 容器创建

MongoDB Docker 容器创建有以下几个问题：
1- MongoDB 容器基本创建方法和数据目录挂载
2- MongoDB 容器的数据迁移
3- MongoDB 设置登录权限问题

### MongoDB 容器基本创建方法和数据目录挂载

MongoDB 容器基本创建命令如下：

```
docker run -p 27017:27017 -v <LocalDirectoryPath>:/data/db --name docker_mongodb -d mongo
```

在上面的命令中，几个命令参数的详细解释如下：
`-p` 指定容器的端口映射，mongodb 默认端口为 27017
`-v` 为设置容器的挂载目录，这里是将<LocalDirectoryPath>即本机中的目录挂载到容器中的/data/db中，作为 mongodb 的存储目录
`--name` 为设置该容器的名称
`-d` 设置容器以守护进程方式运行

![img](https://upload-images.jianshu.io/upload_images/1638540-9345e04db4a2ee4d.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/700)

以上是 MongoDB 容器创建后的信息。
接下来，我们使用 Robo 3T 图形界面软件尝试打开数据库。
打开 RoBo 3T，选择新建连接，按照下图填入相关数据库信息，保存。

![img](https://upload-images.jianshu.io/upload_images/1638540-3dc8e714be5184ba.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/700)

然后点击连接，数据库连接成功，界面如下图显示

![img](https://upload-images.jianshu.io/upload_images/1638540-c95e451b1b062b86.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/700)

这里我们可以看到，这是一个空的数据库。随后我们创建一个test_database的数据库，然后在创建一个test_collection的集合，再在这个集合中添加一个文档，文档内容为：

```
{'info': 'create success!'}
```

我们可以通过 RoBo 3T来查看目前数据库中数据的情况

![img](https://upload-images.jianshu.io/upload_images/1638540-864cc3e5b72b8303.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/700)

## 容器数据迁移

接下来，我们先停止刚才创建的 docker_mongodb 容器，命令如下：

```shell
docker stop docker_mongodb
```

然后我们再创建一个新的 MongoDB 容器，挂载刚才刚刚的数据目录，命令如下：

```shell
docker run -p 27017:27017 -v <LocalDirectoryPath>:/data/db --name docker_mongodb_migration -d mongo
```

我们可以容器查询命令，查看当前 Docker 的容器状态，命令如下：

```shell
docker container ls -a
```

这里的 `-a` 参数是查看所有的容器，包括已经停止的容器。

![img](https://upload-images.jianshu.io/upload_images/1638540-77ffeead0fae3d93.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/700)

 

我们可以从输出结果看到，这时 `docker_mongodb` 的状态是 Exited，表示已经退出，而新创建的 `docker_mongodb_migration` 的状态显示为 Up，表明数据库正在运行。

然后我们再打开 RoBo 3T，连接数据库，可以看到我们看到我们再 `docker_mongodb` 中创建的数据，这里表明我们新创建的 `docker_mongodb_migration` 挂载的数据目录和 `docker_mongodb` 相同，利用这一方法，我们可以实现简单的数据迁移。

![img](https://upload-images.jianshu.io/upload_images/1638540-4057299e23d0addd.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/700)

## MongoDB 的 Docker 常用命令

使用 Docker MongoDB 会使用到以下几个常用的命令。

**查看当前运行的容器**

```shell
# 查看正在运行的容器
docker container ls
# 查看所有容器
docker container ls -a
```

**停止容器**

```shell
# 指定 CONTAINER ID 停止容器
docker stop <CONTAINER ID>
# 指定容器名称停止容器
docker stop <CONTAINER NAME>
```

**启动已经停止的容器**

```shell
# 指定容器 CONTAINER ID 启动容器
docker start <CONTAINER ID>
# 指定容器名称启动容器
docker start <CONTAINER NAME>
```

**重启已经运行的容器**

```shell
# 指定容器 CONTAINER ID 重启容器
docker restart <CONTAINER ID>
# 指定容器名称重启容器
docker restart <CONTAINER NAME>
```

**进入 mongo 交互模式**

```shell
docker exec -it <CONTAINER NAME> mongo admin
```