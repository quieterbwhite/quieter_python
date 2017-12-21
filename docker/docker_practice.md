# Docker 基础

## 安装docker
```
* 方法一

    $ sudo wget -qO- https://get.docker.com/ | sh

        -q, 减少输出
        O-, 将下载的脚本文件送给sh执行
        
* 方法二, 用这个就好了，虽然不是最新的，但是是比较新的稳定版本

    $ sudo apt-get install docker.io

* 让当前用户可以直接执行docker命令

    $ sudo usermod -aG docker `whoami`

*测试是否安装成功:

    $ sudo docker info
    $ sudo docker version
```

## 命令解释
```

$ docker pull

# 显示所有顶层镜像
$ docker image ls

# 显示所有镜像，包括中间层镜像
$ docker image ls -a

# 显示容器
$ docker container ls

$ docker system df, 查看镜像，容器，数据卷所占空间

# 删除镜像
$ docker rm

# 删除容器
$ docker rmi

# 将修改过的容器保存为镜像, 一般不用commit命令
$ docker commit --author "psKy <libo0o@163.com>" --message "修改了默认网页" webserver nginx:v2
    --author: 修改的作者
    --message: 记录本次修改的内容

# 使用build命令构建镜像, 当前目录新建 Dockerfile
$ docker build -t nginx:v3 .

    命令最后的 .  其实并不是指Dockerfile的路径，而是指上下文路径
    构建镜像要用到的文件应该都放到 指定的上下文目录中，不然Docker引擎不能获得文件

# 查看镜像内的历史记录
$ docker  history nginx:v2

# show dangling image, 显示虚悬镜像
$ docker  image   ls  -f  dangling=true

# 删除虚悬镜像
$ docker  image   prune

# 查看容器的修改
$ docker  diff    webserver
```

# Dockerfile
```
* COPY 复制文件

    COPY package.json /usr/src/app/

* ADD 更高级的复制文件

     在 COPY 和 ADD 指令中选择的时候，可以遵循这样的原则，
     所有的文件复制都使用 COPY 指令，仅在需要自动解压的场合使用 ADD

* CMD 容器自动命令

    容器就死进程。
    既然是进程，那么在启动容器的时候，需要指定所运行的程序及参数。
    CMD指令就是用于指定默认的容器主进程的启动命令。

    Docker 不是虚拟机，容器中的应用都应该在前台执行，而不是像虚拟机，物理机里面那样，
    用upstart/systemd去启动后台服务，容器内没有后台服务的概念。
    如前台执行 nginx 主进程:
        CMD ["nginx", "-g", "daemon off;"]

* ENTRYPOINT 入口点

    ENTRYPOINT 和 CMD 目的一样，都是在指定启动程序及参数。

    当指定了 ENTRYPOINT 后，CMD的含义就发生了变化，不再是直接运行其命令，
    而是将 CMD 的内容作为参数传给 ENTRYPOINT 指令，换句话说实际执行时，将变为:

    <ENTRYPOINT> "<CMD>"

    为什么有了 CMD 还有 ENTRYPOINT?

    场景一： 动态参数, 让镜像变成命令一样使用

    CMD:
        FROM ubuntu:16.04
        RUN apt-get update \
            && apt-get install -y curl \
            && rm -rf /var/lib/apt/lists/*
        CMD ["curl", "-s", "http://ip.cn"]

        # 构建镜像
        docker build -t myip
        # 执行
        docker run myip

        这样做不好的地方在于，不能给内部命令动态增加参数
        而 ENTRYPOINT 就可以解决这个问题

    ENTRYPOINT:
        FROM ubuntu:16.04
        RUN apt-get update |
            && apt-get install -y curl \
            && rm -rf /var/lib/apt/lists/*
        ENTRYPOINT ["curl", "-s", "http://ip.cn"]

        # 构建镜像
        docker build -t myip
        # 执行
        docker run myip -i 
        CMD 的内容将会作为参数传递给 ENTRYPOINT
        -i 是新的参数CMD 

    场景二：应用运行前的准备工作

        准备工作是和容器 CMD 无关的，无论是 CMD 是什么，都需要事先进行一个预处理的工作。
        这种情况下，可以写一个脚本，然后放入 ENTRYPOINT 中去执行，而这个脚本会
        将接到的参数(也就是<CMD>)作为命令，在脚本最后执行。如官方redis:

        FROM alpine:3.4
        ...
        RUN addgroup -S redis && adduser -S -G redis redis
        ...
        ENTRYPOINT ["docker-entrypoint.sh"]

        EXPOSE 6379
        CMD ["redis-server"]$

        可以看到创建了用户，并指定了 ENTRYPOINT 为 docker-entrypoint.sh 脚本。

    场景三：设置环境变量

        ENV VERSION=1.0 DEBUG=on \
        NAME="Happy Feet"

        无论是后面的其他指令，如 RUN, 还是运行时应用
        都可以直接使用这里定义的环境变量。

* ARG 构建参数

    构建参数和 ENV 的效果一样，都是设置环境变量。
    所不同的是，ARG 所设置的构建环境的环境变量, 在将来容器运行时是不会存在这些环境变量的。

    Dockerfile 中的ARG指令是定义参数名称，以及定义其默认值。
    该默认值可以在构建命令docker build 中用 --build-arg <参数名>=<值> 来覆盖。

* VOLUME 定义匿名卷

    VOLUME /data

    Dockerfile 中，我们可以事先指定某些目录挂载为匿名卷，这样在运行时如果用户
    不指定挂载，其应用也可以正常运行，不会向容器存储层写入大量数据。

    运行时可以覆盖这个挂载设置，如:
    docker run -d -v mydata:/data xxxx
    在这行命令中，就使用了mydata这个命令卷挂载到了/data这个位置，
    替代了Dockerfile 中定义的匿名卷的挂载配置。

* EXPOSE 申明端口

    EXPOSE 指令是申明运行时容器提供服务端口，
    这只是一个申明，在运行时并不会因为这个声明就会开启这个端口的服务。

    要将EXPOSE和在运行时使用 -p <宿主端口>:<容器端口>区分开来。
    -p, 是映射宿主端口和容器端口,换句话说,
    就是将容器的对应端口服务公开给外界访问,而 EXPOSE 仅仅是声明
    容器打算使用什么端口而已,并不会自动在宿主进行端口映射。

* WORKDIR 指定工作目录

    WORKDIR <工作目录路径>

    RUN cd /app
    RUN echo "hello" > world.txt
    这两行 RUN 命令的执行环境根本不同，是两个完全不同的容器。

    每一个 RUN 都是启动一个容器，执行命令，然后提交存储层文件变更。
    第一层 RUN cd /app 的执行仅仅是当前进程的工作目录变更,一个内存上的变化而已,其结果不会造成任
    何文件变更。而到第二层的时候,启动的是一个全新的容器,跟第一层的容器更完全没关
    系,自然不可能继承前一层构建过程中的内存变化。
    因此如果需要改变以后各层的工作目录的位置,那么应该使用 WORKDIR 指令。

* USER 指定当前用户

    USER <用户名>   

    这个用户必须是事先建立好的，否则无法切换

    RUN groupadd -r redis && useradd -r -g redis redis
    USER redis
    RUN ["redis-server"]

    gosu 用户，这个需要的时候查资料 docker_practice.pdf

* HEALTHCHECK 健康检查


* Dockerfile 多阶段构建
```

```
* 示例一

    FROM ubuntu
    MAINTAINER libo
    RUN sed -i 's/archive.ubuntu.com/mirrors.ustc.edu.cn/g' /etc/apt/sources.list
    RUN apt-get update
    RUN apt-get install -y nginx
    COPY index.html /var/www/html
    ENTRYPOINT ["/usr/sbin/nginx", "-g", "daemon off;"] # run nginx frontend
    EXPOSE 80

    docker build -t libo/hello-nginx .

    docker run -d -p 80:80 libo/hello-nginx
```

## 操作Docker容器
```
* 新建并启动

    # 输出后终止容器
    $ docker run ubuntu:14.04 /bin/echo 'hello world'

    # 启动一个bash终端，允许用户进行交互
    $ docker run -t -i ubuntu:14.04 /bin/bash

        -t 分配一个伪终端(pseudo-tty)并绑定到容器的标准输入上
        -i 让容器的标准输入保持打开

* 后台运行

    使用 -d 参数运行容器

    docker run -d ubuntu:17.10 /bin/sh -c "while true; do echo hello world; sleep 1; done"

    此时容器会在后台运行。输出结果可以使用 docker logs 查看

    要获取容器的输出信息，可以通过 docker container logs 命令

    docker container logs [container ID or NAMES]

* 终止容器

    docker container stop

    终止状态的容器可以用 docker container ls -a 查看

* 进入容器

    docker exec

    docker run -dit ubuntu

    docker container ls

    docker exec -it 69d1 bash
    如果从这个stdin中exit，不会导致容器的停止。
    这就是为什么推荐使用docker exec 而不是 attach 的原因

* 导出和导入容器

    docker export 命令可以到处本地某个容器

    $ docker ps -a

    # 这样将导出容器快照到本地文件
    $ docker export container_id > ubuntu.tar

* 导入容器快照

    可以使用 docker import 导入容器快照文件为镜像

    $ cat ubuntu.tar | docker import - test/ubuntu:v1.0

    docker load 导入镜像存储文件 && docker import 导入容器快照

    区别:
        快照将丢失历史记录和元数据信息

* 删除容器

    $ docker container rm trusting_newton

    如果要删除一个运行中的容器，可以添加 -f 参数，Docker 会发送 SIGKILL 信号给容器

* 清理所有处于终止状态的容器

    $ docker container prune
```

## 访问仓库
```
* 登录&退出

    docker login

    docker logout

* 拉取镜像

    # 以 centos 为关键字进行搜索
    docker search centos

* 推送镜像

    用户在登录后也可以推送自己的镜像到 Docker Hub。

    $ docker tag ubuntu:17.10 psky/ubuntu:17.10

    $ docker image ls

    $ docker push psky/ubuntu:17.10

    $ docker search psky

* 自动创建

    pass

* 私有仓库

    pass

* Docker 数据管理

    容器中管理数据主要有两种方式:

        数据卷 Volumes
        挂载主机目录 Bind mounts

* 数据卷

    1. 数据卷可以在容器之间共享和重用

    2. 对数据卷的修改会立马生效

    3. 对数据卷的更新，不会影响镜像

    4. 数据卷默认会一直存在，即使容器被删除

    注意: 数据卷的使用，类似于Linux下对目录或文件进行mount，镜像中的被指定
    为挂载点的目录中的文件会隐藏掉，能显示看的是挂载的数据卷。

    选择 -v 还是 --mount 参数

    Docker 新用户应该选择 --mount 参数，经验丰富的 Docker 使用者对 -v 或者 --volume
    已经很熟悉了，但是推荐使用 --mount 参数。

    ----命令----

    创建一个数据卷:

        $ docker volume create my-vol

    查看所有的数据卷:

        $ docker volume ls

    查看指定数据卷的信息:

        $ docker volume inspect my-vol

    启动一个挂载数据卷的容器:

        在用 docker run 命令的时候，使用 --mount 标记来将 数据卷 挂载到容器里。
        在一次　docker run 中可以挂载多个 数据卷

    创建一个名为 web 的容器，并加载一个　数据卷 到容器的 /webapp 目录

    $ docker run -d -P \
        --name web \
        # -v my-vol:/webapp \
        --mount source=my-vol,target=/webapp \
        training/webapp \
        python app.py

    查看数据卷的具体信息:

        # 在主机里使用以下命令可以查看 web 容器的信息
        $ docker inspect web

        数据卷信息在 "Mounts" Key 下面

    删除数据卷:

        $ docker volume rm my-rol

    数据卷是被设计用来持久化数据的

    清理无主的数据卷:

        $ docker volume prune

    挂载主机目录

        挂载一个主机目录作为数据卷
        使用 --mount 标记可以指定挂载一个本地主机的目录到容器中去

        $ docker run -d -P \
            --name web \
            # -v /src/webapp:/opt/webapp \
            --mount type=bind,source=/src/webapp,target=/opt/webapp,readonly \
            training/webapp \
            python app.py

        上面的命令加载主机目录到容器目录。

        本地路径必须是绝对路径且必须存在

        Docker 挂载主机目录的默认权限是 读写，也可以通过增加 readonly 指定为只读

    挂载一个本地主机文件作为数据卷

        --mount 标记也可以从主机挂载单个文件到容器中

* Docker 中的网络功能

    外部访问容器

        通过 -P 或 -p 参数来指定端口映射

        -P, 随机映射 49000 - 49900 的端口到内部容器开放的网络端口。

        如，本地主机的49155映射到了容器的5000端口，那么
        此时访问本机的49155端口即可访问容器内web应用提供的界面。

        $ docker run -d -P training/webapp python app.py

        -p, 则可以指定要映射的端口，并且，在一个指定端口上只可以绑定一个容器。

            可以用来绑定多个端口

            $ docker run -d \
                -p 5000:5000
                -p 3000:80 \
                training/webapp \
                python app.py

        * 映射所有接口地址:

            # 此时默认会绑定所有接口上的所有地址
            $ docker run -d -p 5000:5000 training/webapp python app.py

        * 映射到指定地址的指定端口:

            $ docker run -d -p 127.0.0.1:5000:5000 training/webapp python app.py

        * 映射到指定地址的任意端口:

            $ docker run -d -p 127.0.0.1::5000 training/webapp python app.py

        * 还可以使用 udp 标记来指定udp端口

        $ docker run -d -p 127.0.0.1:5000:5000/udp training/webapp python app.py

        * 查看映射端口配置

        $ docker port nostalgic_morse 5000

* 容器互联

    * 新建网络

    $ docker network create -d bridge my-net

        -d, 指定Docker网络模型，有 bridge, overlay

    * 连接容器
    
        运行两个容器并都加入到 my-net 网络

        $ docker run -it --rm --name busybox1 --network my-net busybox sh

        $ docker run -it --rm --name busybox2 --network my-net busybox sh

        测试 busybox1 和 busybox2 的网络联通性

        在 busybox1 容器中输入以下命令:
        
            $ ping busybox2

        这样 busybox1 和 busybox2 建立了联系

    * Docker Compose

        如果有多个容器之间需要互相连接，推荐使用 Docker Compose

        * 配置 DNS

            Docker 利用虚拟文件来挂载容器的3个相关配置文件

            在容器中使用 mount 命令可以看到挂载信息

            这种机制，可以让宿主主机DNS信息发生更新后，所有Docker容器的DNS
            配置通过 /etc/resolv.conf 文件立即得到更新

            配置全部容器的DNS，也可以在 /etc/docker/daemon.json文件中增加以下内容来设置
            {
                "dns" : [
                    "114.114.114.114",
                    "8.8.8.8"
                ]
            }

            这样每次启动的容器 DNS 自动配置为 114.114.114.114 和 8.8.8.8
            使用以下命令证明其已经生效

            $ docker run -it --rm ubuntu:17.10 cat etc/resolv.conf

                nameserver 114.114.114.114
                nameserver 8.8.8.8

            如果想手动指定容器的配置，那么使用参数:

                --hostname=HOSTNAME
                --dns=IP_ADDRESS
                --dns-search=DOMAIN
```

## Compose
```
* 安装与卸载

    sudo pip install docker-compose

    sudo pip uninstall docker-compose
```


