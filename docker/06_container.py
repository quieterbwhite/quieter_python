# -*- coding=utf-8 -*-
# Created Time: 2017年08月05日 星期六 12时54分31秒
# File Name: 06_container.py

启动容器

    启动容器有两种方式，一种是基于镜像新建一个容器并启动，另外一个是将在终止状态（stopped）的容器重新启动。

    因为 Docker 的容器实在太轻量级了，很多时候用户都是随时删除和新创建容器。

    新建并启动

        所需要的命令主要为 docker run。

        例如，下面的命令输出一个 “Hello World”，之后终止容器。

        $ sudo docker run ubuntu:14.04 /bin/echo 'Hello world'
        Hello world

        这跟在本地直接执行 /bin/echo 'hello world' 几乎感觉不出任何区别。

        下面的命令则启动一个 bash 终端，允许用户进行交互。

        $ sudo docker run -t -i ubuntu:14.04 /bin/bash
        root@af8bae53bdd3:/#

        其中，-t 选项让Docker分配一个伪终端（pseudo-tty）并绑定到容器的标准输入上， -i 则让容器的标准输入保持打开。

后台(background)运行

    更多的时候，需要让 Docker在后台运行而不是直接把执行命令的结果输出在当前宿主机下。此时，可以通过添加 -d 参数来实现。

    如果不使用 -d 参数运行容器。

    $ sudo docker run ubuntu:14.04 /bin/sh -c "while true; do echo hello world; sleep 1; done"
    hello world
    hello world
    hello world
    hello world

    容器会把输出的结果(STDOUT)打印到宿主机上面

    如果使用了 -d 参数运行容器。

    $ sudo docker run -d ubuntu:14.04 /bin/sh -c "while true; do echo hello world; sleep 1; done"
    77b2dc01fe0f3f1265df143181e7b9af5e05279a884f4776ee75350ea9d8017a

    此时容器会在后台运行并不会把输出的结果(STDOUT)打印到宿主机上面(输出结果可以用docker logs 查看)。

    注： 容器是否会长久运行，是和docker run指定的命令有关，和 -d 参数无关。

    使用 -d 参数启动后会返回一个唯一的 id，也可以通过 docker ps 命令来查看容器信息。

    $ sudo docker ps
    CONTAINER ID  IMAGE         COMMAND               CREATED        STATUS       PORTS NAMES
    77b2dc01fe0f  ubuntu:14.04  /bin/sh -c 'while tr  2 minutes ago  Up 1 minute        agitated_wright
    要获取容器的输出信息，可以通过 docker logs 命令。

    $ sudo docker logs [container ID or NAMES]
    hello world
    hello world
    hello world

终止容器

    可以使用 docker stop 来终止一个运行中的容器。

    此外，当Docker容器中指定的应用终结时，容器也自动终止。 例如对于上一章节中只启动了一个终端的容器，用户通过 exit 命令或 Ctrl+d 来退出终端时，所创建的容器立刻终止。

    终止状态的容器可以用 docker ps -a 命令看到。例如

    处于终止状态的容器，可以通过 docker start 命令来重新启动。

    此外，docker restart 命令会将一个运行态的容器终止，然后再重新启动它。

进入容器

    nsenter 命令

        nsenter 启动一个新的shell进程(默认是/bin/bash), 同时会把这个新进程切换到和目标(target)进程相同的命名空间，这样就相当于进入了容器内部。nsenter 要正常工作需要有 root 权限。

        为了连接到容器，你还需要找到容器的第一个进程的 PID，可以通过下面的命令获取。

        PID=$(docker inspect --format "{{ .State.Pid }}" <container>)

        下面给出一个完整的例子。

        $ sudo docker run -idt ubuntu
        243c32535da7d142fb0e6df616a3c3ada0b8ab417937c853a9e1c251f499f550
        $ sudo docker ps
        CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
        243c32535da7        ubuntu:latest       "/bin/bash"         18 seconds ago      Up 17 seconds                           nostalgic_hypatia
        $ PID=$(docker-pid 243c32535da7)
        10981
        $ sudo nsenter --target 10981 --mount --uts --ipc --net --pid
        root@243c32535da7:/#


        更简单的，建议大家下载 .bashrc_docker，并将内容放到 .bashrc 中。

        $ wget -P ~ https://github.com/yeasy/docker_practice/raw/master/_local/.bashrc_docker;
        $ echo "[ -f ~/.bashrc_docker ] && . ~/.bashrc_docker" >> ~/.bashrc; source ~/.bashrc

        这个文件中定义了很多方便使用 Docker 的命令，例如 docker-pid 可以获取某个容器的 PID；而 docker-enter 可以进入容器或直接在容器内执行命令。

        $ echo $(docker-pid <container>)
        $ docker-enter <container> ls

删除容器

    可以使用 docker rm 来删除一个处于终止状态的容器。 例如

    $sudo docker rm  trusting_newton
    trusting_newton
    如果要删除一个运行中的容器，可以添加 -f 参数。Docker 会发送 SIGKILL 信号给容器。

    清理所有处于终止状态的容器

    用 docker ps -a 命令可以查看所有已经创建的包括终止状态的容器，如果数量太多要一个个删除可能会很麻烦，用 docker rm $(docker ps -a -q) 可以全部清理掉。

    *注意：这个命令其实会试图删除所有的包括还在运行中的容器，不过就像上面提过的 docker rm 默认并不会删除运行中的容器。












