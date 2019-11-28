##### 1. install
```shell
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04

使用脚本自动安装

Docker 官方为了简化安装流程，提供了一套安装脚本，Ubuntu 和 Debian 系统可以使用这套脚本安装：

curl -sSL https://get.docker.com/ | sh

执行这个命令后，脚本就会自动的将一切准备工作做好，并且把 Docker 安装在系统中。

阿里云的安装脚本
curl -sSL http://acs-public-mirror.oss-cn-hangzhou.aliyuncs.com/docker-engine/internet | sh -

DaoCloud 的安装脚本
curl -sSL https://get.daocloud.io/docker | sh

docker -v
```

##### 2. 镜像加速器

```shell
打开/etc/default/docker文件（需要sudo权限），在文件的底部加上一行。
DOCKER_OPTS="--registry-mirror=https://registry.docker-cn.com"
然后，重启 Docker 服务。
$ sudo service docker restart
```

```shell
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
```
