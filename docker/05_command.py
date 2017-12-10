# -*- coding=utf-8 -*-
# Created Time: 2017年08月05日 星期六 10时57分21秒
# File Name: 05_command.py

COPY 复制文件

    格式：

    COPY <源路径>... <目标路径>
    COPY ["<源路径1>",... "<目标路径>"]

    比如：

    COPY package.json /usr/src/app/
    <源路径> 可以是多个，甚至可以是通配符，其通配符规则要满足 Go 的 filepath.Match 规则，如：

    COPY hom* /mydir/
    COPY hom?.txt /mydir/

CMD 容器启动命令

    CMD 指令的格式和 RUN 相似，也是两种格式：

    shell 格式：CMD <命令>

    之前介绍容器的时候曾经说过，Docker 不是虚拟机，容器就是进程。
    既然是进程，那么在启动容器的时候，需要指定所运行的程序及参数。
    CMD 指令就是用于指定默认的容器主进程的启动命令的。

    Docker 不是虚拟机，容器中的应用都应该以前台执行，而不是像虚拟机、物理机里面那样，
    用 upstart/systemd 去启动后台服务，容器内没有后台服务的概念。

    一些初学者将 CMD 写为：

    CMD service nginx start

    然后发现容器执行后就立即退出了。甚至在容器内去使用 systemctl 命令结果却发现根本执行不了。
    这就是因为没有搞明白前台、后台的概念，没有区分容器和虚拟机的差异，依旧在以传统虚拟机的角度去理解容器。

    对于容器而言，其启动程序就是容器应用进程，容器就是为了主进程而存在的，
    主进程退出，容器就失去了存在的意义，从而退出，其它辅助进程不是它需要关心的东西。

    而使用 service nginx start 命令，则是希望 upstart 来以后台守护进程形式启动 nginx 服务。
    而刚才说了 CMD service nginx start 会被理解为 CMD [ "sh", "-c", "service nginx start"]，
    因此主进程实际上是 sh。那么当 service nginx start 命令结束后，sh 也就结束了，sh 作为主进程退出了，自然就会令容器退出。

    正确的做法是直接执行 nginx 可执行文件，并且要求以前台形式运行。比如：

    CMD ["nginx", "-g", "daemon off;"]

ENTRYPOINT 入口点

    ENTRYPOINT 的目的和 CMD 一样，都是在指定容器启动程序及参数。ENTRYPOINT 在运行时也可以替代，不过比 CMD 要略显繁琐，需要通过 docker run 的参数 --entrypoint 来指定。

    ENTRYPOINT 就是可以附加参数的 CMD

ENV 设置环境变量

    格式有两种：

    ENV <key> <value>
    ENV <key1>=<value1> <key2>=<value2>...

    ENV VERSION=1.0 DEBUG=on \
                NAME="Happy Feet"

    可以从这个指令列表里感觉到，环境变量可以使用的地方很多，很强大。
    通过环境变量，我们可以让一份 Dockerfile 制作更多的镜像，只需使用不同的环境变量即可。

VOLUME 定义匿名卷

    格式为：

    VOLUME ["<路径1>", "<路径2>"...]
    VOLUME <路径>

    之前我们说过，容器运行时应该尽量保持容器存储层不发生写操作，对于数据库类需要保存动态数据的应用，其数据库文件应该保存于卷(volume)中

    docker run -d -v mydata:/data xxxx
    在这行命令中，就使用了 mydata 这个命名卷挂载到了 /data 这个位置，替代了 Dockerfile 中定义的匿名卷的挂载配置。

EXPOSE 声明端口

    格式为 EXPOSE <端口1> [<端口2>...]。

    要将 EXPOSE 和在运行时使用 -p <宿主端口>:<容器端口> 区分开来。
    -p，是映射宿主端口和容器端口，换句话说，就是将容器的对应端口服务公开给外界访问，
    而 EXPOSE 仅仅是声明容器打算使用什么端口而已，并不会自动在宿主进行端口映射。

WORKDIR 指定工作目录

    格式为 WORKDIR <工作目录路径>。

    使用 WORKDIR 指令可以来指定工作目录（或者称为当前目录），以后各层的当前目录就被改为指定的目录，如该目录不存在，WORKDIR 会帮你建立目录。

删除本地镜像

    如果要删除本地的镜像，可以使用 docker rmi 命令，其格式为：

    docker rmi [选项] <镜像1> [<镜像2> ...]
    注意 docker rm 命令是删除容器，不要混淆。

    用 ID、镜像名、摘要删除镜像











