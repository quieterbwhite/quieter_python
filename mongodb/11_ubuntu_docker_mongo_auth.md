### Docker MongoDB 配置权限登录

>    [speculatecat](https://www.jianshu.com/u/98ea51905386)

![img](https://upload-images.jianshu.io/upload_images/1638540-d7efd136261628ea.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/700)

在[《Docker MongoDB 部署》](https://www.jianshu.com/p/6fdb2bcb4b43)一文中，我们了解了如何使用 Docker 部署 MongoDB，但是按照上一篇文章部署好的 MongoDB，并没有设置连接权限，也就是说，只要知道服务器地址以及 MongoDB 的端口号，就能直接对数据库进行操作，这样会造成极大的安全隐患，因此本文将介绍如何为 Docker 部署的 MongoDB 配置权限。

## Ubuntu Docker 环境一键部署

安装 Docker 大致步骤主要有三个，分别是添加 Docker 安装源，配置 Docker 镜像源以及将用户添加到 docker 用户组。目前，阿里云的 Docker CE 镜像站有提供自动安装脚本，直接复制以下命令即可完成安装。

```
curl -fsSL https://get.docker.com | bash -s docker --mirror Aliyun

```

但是，我们依旧还是需要自己进行配置。为了日后再次安装或者配置新的服务器时更方便，我们将编写一个一键自动安装的脚本。

在编写脚本之前，需要先注册一个阿里云账户，然后找到里面的容器镜像服务，里面可以找到专属的容器加速地址。

![img](https://upload-images.jianshu.io/upload_images/1638540-69a190b8f81a1aa5.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/700)

上图黄色遮盖部分就是自己的用户编号。
接下来我们将创建一个一键安装脚本：

```
#! /bin/bash
# install docker form source aliyun
apt-get update
apt-get -y install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL http://mirrors.aliyun.com/docker-ce/linux/ubuntu/gpg | sudo apt-key add -
add-apt-repository "deb [arch=amd64] http://mirrors.aliyun.com/docker-ce/linux/ubuntu $(lsb_release -cs) stable"
apt-get -y update
apt-get -y install docker-ce
# change source to aliyun
mkdir -p /etc/docker
tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": ["https://<替换为阿里云提供的用户编码>.mirror.aliyuncs.com"]
}
EOF
# add user to docker group
user=$(who am i | awk '{print $1}')
usermod -aG docker $user
# restart docker
systemctl daemon-reload
systemctl restart docker

```

以上脚本有两点需要注意：

-   `registry-mirrors` 中的地址需要替换为自己的阿里云容器镜像加速服务里面提供的地址
-   由于该脚本需要使用 `sudo` 运行，而 Ubuntu 中使用 `sudo` 命令不能简单的使用 $USER$ 来获取用户名，因此这里使用了 `user=$(who am i | awk '{print $1}')` 来获取当前用户，并将其添加到 docker 用户组

编写完成后保存脚本，使用 sudo 命令运行即可。

## 创建 Mongo 容器

创建需要验证用户权限的 MongoDB 的容器和创建普通 MongoDB 容器区别不大，只是需要在命令末尾添加 `--auth` 参数，具体操作如下：

```
docker run -p 27017:27017 -v <LocalDirectoryPath>:/data/db --name --restart unless-stopped -d docker_mongodb  mongod --auth

```

创建完成后，我们将使用 admin 进入 mongodb，为数据库设置管理员用户，具体操作如下：

```
# 交互界面进入 mongo
docker exec -it <docker_mongodb_name> mongo admin
# 创建一个 admin 管理员账号
db.createUser({ user: 'admin', pwd: 'admin', roles: [ { role: "userAdminAnyDatabase", db: "admin" } ] });
>>
Successfully added user: {
    "user" : "admin",
    "roles" : [
        {
            "role" : "userAdminAnyDatabase",
            "db" : "admin"
        }
    ]
}

```

我们可以从反馈信息中看到，我们的 admin 账户已经创建成功，这时，我们可以尝试使用 Robo 3T 登录，这是会发现，如果我们不使用密码，数据库是服务登录查看数据的，具体参考下图：

![img](https://upload-images.jianshu.io/upload_images/1638540-7b75a9303be5a0e0.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/700)



![img](https://upload-images.jianshu.io/upload_images/1638540-3d8edd5c5856af39.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/700)

 

到这里为止，我们已经完成给 docker mongodb 设置权限了。另外，还有一点需要注意的，这里使用的 `userAdminAnyDatabase` 权限，该用户可以查看所有数据库，但不能创建和删除数据库，如果要使用可以创建数据库的用户，权限使用 `root`。

## 参考资料

[阿里云 Docker CE 镜像源站](https://link.jianshu.com/?t=https%3A%2F%2Fyq.aliyun.com%2Farticles%2F110806%3Fspm%3D5176.8351553.0.0.35061991MIKpD6)