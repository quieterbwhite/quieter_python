# -*- coding=utf-8 -*-
# Created Time: 2017年08月04日 星期五 23时42分48秒
# File Name: 01_init.py

1. instal

使用脚本自动安装

Docker 官方为了简化安装流程，提供了一套安装脚本，Ubuntu 和 Debian 系统可以使用这套脚本安装：

curl -sSL https://get.docker.com/ | sh

执行这个命令后，脚本就会自动的将一切准备工作做好，并且把 Docker 安装在系统中。

阿里云的安装脚本
curl -sSL http://acs-public-mirror.oss-cn-hangzhou.aliyuncs.com/docker-engine/internet | sh -

DaoCloud 的安装脚本
curl -sSL https://get.daocloud.io/docker | sh

docker -v

2. 镜像加速器

```
打开/etc/default/docker文件（需要sudo权限），在文件的底部加上一行。
DOCKER_OPTS="--registry-mirror=https://registry.docker-cn.com"
然后，重启 Docker 服务。
$ sudo service docker restart
```

阿里云加速器  http://cr.console.aliyun.com/#/accelerator

注册用户并且申请加速器，会获得如 https://571cbuth.mirror.aliyuncs.com 这样的地址。
我们需要将其配置给 Docker 引擎。

##################################ali##########################################
安装／升级你的Docker客户端
推荐安装1.10.0以上版本的Docker客户端。

您可以通过阿里云的镜像仓库下载：docker-engine、docker-ce

或执行以下命令：

curl -sSL http://acs-public-mirror.oss-cn-hangzhou.aliyuncs.com/docker-engine/internet | sh -
如何使用Docker加速器
针对Docker客户端版本大于1.10的用户

您可以通过修改daemon配置文件/etc/docker/daemon.json来使用加速器：

sudo mkdir -p /etc/docker
sudo tee /etc/docker/daemon.json
{
  "registry-mirrors": ["https://571cbuth.mirror.aliyuncs.com"]
}
sudo systemctl daemon-reload
sudo systemctl restart docker
##################################ali##########################################

Ubuntu 14.04、Debian 7 Wheezy

    对于使用 upstart 的系统而言，编辑 /etc/default/docker 文件，在其中的 DOCKER_OPTS 中添加获得的加速器配置 --registry-mirror=<加速器地址>，如：

    DOCKER_OPTS="--registry-mirror=https://jxus37ad.mirror.aliyuncs.com"
    重新启动服务。

    $ sudo service docker restart

Ubuntu 16.04、Debian 8 Jessie、CentOS 7

    对于使用 systemd 的系统，用 systemctl enable docker 启用服务后，
    编辑 /etc/systemd/system/multi-user.target.wants/docker.service 文件，
    找到 ExecStart= 这一行，在这行最后添加加速器地址 --registry-mirror=<加速器地址>，如：

    ExecStart=/usr/bin/dockerd --registry-mirror=https://jxus37ad.mirror.aliyuncs.com

检查加速器是否生效

    Linux系统下配置完加速器需要检查是否生效，在命令行执行 ps -ef | grep dockerd，
    如果从结果中看到了配置的 --registry-mirror 参数说明配置成功。

    $ sudo ps -ef | grep dockerd
    root      5346     1  0 19:03 ? 00:00:00 /usr/bin/dockerd --registry-mirror=https://jxus37ad.mirror.aliyuncs.com
    $


