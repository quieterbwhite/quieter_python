#### docker love python

```shell
-- 拉取镜像
docker pull python:3.6.8

-- 创建容器并进入容器命令行
docker run -it --entrypoint bash python:3.6.8

-- 启动容器
docker start 1e8aa

-- 进入容器命令行
docker exec -it 1e8aa /bin/bash

安装python依赖
$ pip install thrift
```

##### docker-compose
```shell
# 启动所有服务
docker-compose up -d

# 启动其中一个服务
docker-compose up -d message-service

# 停止所有服务
docker-compose down
```

##### 镜像仓库
```shell
docker 官方仓库
https://hub.docker.com

上传镜像到docker仓库

    1. 将本地镜像打tag
        docker tag message-service:v1 psky/message-service:v1

    2. 登录仓库
        docker login

    3. push
        docker push psky/message-service:v1

    4. 网页端查看
        hub.docker.com 网页端刷新就可以看到刚刚推送的镜像

私有仓库

    # 到docker仓库找合适版本的搭建私有仓库的镜像
    docker pull registry:2

    docker run -d -p 5000:5000 registry:2

    docker tag message-service:v1 localhost:5000/message-service:v1

    docker push localhost:5000/message-service:v1

    docker pull localhost:5000/message-service:v1

    这个docker官方默认的不好用，使用vmware在github开源的harbor

harbor

    到github下载线下安装包

    cd harbor

    修改配置文件, vim harbor.cfg

        hostname = hub.psky.com:8080

    修改挂在目录, vim docker-compose.yml

        所有的本地路径前面加 ./, 让其挂在到当前目录, 因为有权限

        harbor.cfg 这个配置文件里面也有挂载的路径需要修改

        更改绑定的端口地址为 8080

    安装, ./install.sh

    访问: http://hub.psky.com:8080/harbor/sign-in
        username: admin
        password: admin12345
        这个信息在　harbor.cfg　配置文件里面

        创建项目

    推送本地镜像到　hub.psky.com 仓库

        docker tag openjdk:7-jre hub.psky.com:8080/micro-service/openjdk:7-jre
        docker push hub.psky.com:8080/micro-service/openjdk:7-jre
            推送可能会遇到https问题，这个需要设置绕过
            docker启动的时候增加参数: --inscure-registry
```

##### docker swarm
```shell

```

##### jar命令
```shell
// 查看jar包里面的内容
jar -tf app.jar
```
