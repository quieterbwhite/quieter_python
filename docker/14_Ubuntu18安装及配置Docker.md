#### Ubuntu18安装及配置Docker(附使用阿里云镜像加速器)

2019-04-02 16:15:44 [Kellen5l](https://me.csdn.net/qq_39506912) 阅读数 5794 收藏 文章标签： [Docker](https://so.csdn.net/so/search/s.do?q=Docker&t=blog)[Ubuntu](https://so.csdn.net/so/search/s.do?q=Ubuntu&t=blog)[Linux](https://so.csdn.net/so/search/s.do?q=Linux&t=blog) 更多

分类专栏： [Linux](https://blog.csdn.net/qq_39506912/category_8900801.html)

版权声明：本文为博主原创文章，遵循[ CC 4.0 BY-SA ](http://creativecommons.org/licenses/by-sa/4.0/)版权协议，转载请附上原文出处链接和本声明。本文链接：https://blog.csdn.net/qq_39506912/article/details/88974664

CentOS安装及配置可移步[CentOS7安装及配置Docker(附使用阿里云镜像加速器)](https://blog.csdn.net/qq_39506912/article/details/89606900)

> https://blog.csdn.net/qq_43901693/article/details/103131789

## 系统配置

1. 官方路径安装docker时总是会出现连接超时问题，为此我们使用以下命令修改源为阿里云镜像仓库。

```
sudo vim /etc/apt/sources.list

# 在末尾添加以下代码
deb http://mirrors.aliyun.com/ubuntu/ xenial main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ xenial-security main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ xenial-updates main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ xenial-proposed main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ xenial-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ xenial main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-proposed main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-backports main restricted universe multiverse
```

1. 添加完成后我们执行以下命令，重新同步包的索引文件。

```
sudo apt update
1
```

## Docker安装

若想使用官网安装方法则移步至[官网Ubuntu安装DockerCE方法](https://docs.docker.com/install/linux/docker-ce/ubuntu/)

1. 安装这些包来允许apt通过https使用存储库。

```
 sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common
123456
```

1. 添加Docker的官方GPG密钥。

```
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
1
```

1. 通过搜索指纹的后8个字符，验证是否拥有带指纹的密钥 。

```
sudo apt-key fingerprint 0EBFCD88

# 结果类似如下：
pub   rsa4096 2017-02-22 [SCEA]
      9DC8 5822 9FC7 DD38 854A  E2D8 8D81 803C 0EBF CD88
uid           [ unknown] Docker Release (CE deb) <docker@docker.com>
sub   rsa4096 2017-02-22 [S]
1234567
```

1. 使用以下命令设置稳定存储库。

```
sudo add-apt-repository "deb [arch=amd64] http://mirrors.aliyun.com/docker-ce/linux/ubuntu $(lsb_release -cs) stable"
1
```

1. 再次重新同步包的索引文件。

```
sudo apt update
1
```

1. 安装最新版本Docker。

```
sudo apt-get  install docker-ce
1
```

1. 检验是否安装成功。

```
sudo docker version

# 结果类似如下：
Client:
 Version:           18.06.0-ce
 API version:       1.38
 Go version:        go1.10.3
 Git commit:        0ffa825
...
123456789
```

## 配置镜像加速器

1. 我们这里使用[阿里云镜像](https://promotion.aliyun.com/ntms/act/kubernetes.html)，之后搜索任意镜像即可，目的是跳转至控制台，这里我们搜索Redis。
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
