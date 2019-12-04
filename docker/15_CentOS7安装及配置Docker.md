# CentOS7安装及配置Docker(附使用阿里云镜像加速器)

2019-04-27 20:28:32 [Kellen5l](https://me.csdn.net/qq_39506912) 阅读数 5993 收藏 更多

分类专栏： [Linux](https://blog.csdn.net/qq_39506912/category_8900801.html)

版权声明：本文为博主原创文章，遵循[ CC 4.0 BY-SA ](http://creativecommons.org/licenses/by-sa/4.0/)版权协议，转载请附上原文出处链接和本声明。本文链接：https://blog.csdn.net/qq_39506912/article/details/89606900

Ubuntu的安装及配置可移步[Ubuntu18安装及配置Docker(附使用阿里云镜像加速器)](https://blog.csdn.net/qq_39506912/article/details/88974664)

## 系统配置

1. 备份原来CentOS-Base.repo文件，以免发生错误之后可以还原。

```
sudo mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
1
```

1. 下载阿里云yum源配置文件。

```
sudo curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
1
```

1. 生成缓存并更新源。

```
# 生成缓存
sudo yum makecache

# 更新源
sudo yum -y update
12345
```

## Docker安装

若想使用官网安装方法则移步至[官网CentOS安装DockerCE方法](https://docs.docker.com/install/linux/docker-ce/centos/)

1. 安装所需要的包。

```
sudo yum install -y yum-utils \
  device-mapper-persistent-data \
  lvm2
123
```

1. 设置稳定存储库。

```
sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo
123
```

1. 安装DockerCE。

```
sudo yum install docker-ce docker-ce-cli containerd.io
1
```

1. 启动与检验Docker版本。

```
# 启动Docker
sudo systemctl start docker

# 检验版本
sudo docker version
12345
```

## 配置镜像加速器

1. 我们这里使用[阿里云镜像](https://promotion.aliyun.com/ntms/act/kubernetes.html)，之后如下图搜索任意镜像，目的是跳转至控制台，这里我们搜索Redis。
   ![在这里插入图片描述](https://img-blog.csdnimg.cn/2019040216032415.png)
2. 点击搜索后会需要你登录阿里云控制台，并设置镜像容器服务的登录密码，这里就不赘述了。登录成功后点击下图所示的镜像加速器选项。这里我隐去了我的加速器地址。
   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20190402160805152.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5NTA2OTEy,size_16,color_FFFFFF,t_70)
3. 修改daemon.json配置文件来使用我们的加速器，Ubuntu与CentOS操作类似。

```
sudo vim /etc/docker/daemon.json

# 添加以下配置
{
  "registry-mirrors": ["你的加速器地址"]
}
123456
```

1. 保存后我们重新加载配置文件，并重启Docker。之后我们即可通过加速器提升获取Docker官方镜像的速度。

```
sudo systemctl daemon-reload

sudo systemctl restart docker
```