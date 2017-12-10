# -*- coding=utf-8 -*-
# Created Time: 2017年08月05日 星期六 10时11分51秒
# File Name: 04_dockerfile.py


使用 Dockerfile 定制镜像

    还以之前定制 nginx 镜像为例，这次我们使用 Dockerfile 来定制。

    在一个空白目录中，建立一个文本文件，并命名为 Dockerfile：

    $ mkdir mynginx
    $ cd mynginx
    $ touch Dockerfile
    其内容为：

    FROM nginx
    RUN echo '<h1>Hello, Docker!</h1>' > /usr/share/nginx/html/index.html
    这个 Dockerfile 很简单，一共就两行。涉及到了两条指令，FROM 和 RUN。

FROM 指定基础镜像

    所谓定制镜像，那一定是以一个镜像为基础，在其上进行定制。
    就像我们之前运行了一个 nginx 镜像的容器，再进行修改一样，基础镜像是必须指定的。
    而 FROM 就是指定基础镜像，因此一个 Dockerfile 中 FROM 是必备的指令，并且必须是第一条指令。

RUN 执行命令

    RUN 指令是用来执行命令行命令的。

    shell 格式：RUN <命令>，就像直接在命令行中输入的命令一样。
    RUN echo '<h1>Hello, Docker!</h1>' > /usr/share/nginx/html/index.html

    exec 格式：RUN ["可执行文件", "参数1", "参数2"]，这更像是函数调用中的格式。

    之前说过，Dockerfile 中每一个指令都会建立一层，RUN 也不例外。每一个 RUN 的行为，
    就和刚才我们手工建立镜像的过程一样：新建立一层，在其上执行这些命令，执行结束后，commit 这一层的修改，构成新的镜像。

    而上面的这种写法，创建了 7 层镜像。这是完全没有意义的，而且很多运行时不需要的东西，
    都被装进了镜像里，比如编译环境、更新的软件包等等。

    Union FS 是有最大层数限制的，比如 AUFS，曾经是最大不得超过 42 层，现在是不得超过 127 层。

    上面的 Dockerfile 正确的写法应该是这样：

    FROM debian:jessie

    RUN buildDeps='gcc libc6-dev make' \
                && apt-get update \
                    && apt-get install -y $buildDeps \
                        && wget -O redis.tar.gz "http://download.redis.io/releases/redis-3.2.5.tar.gz" \
                            && mkdir -p /usr/src/redis \
                                && tar -xzf redis.tar.gz -C /usr/src/redis --strip-components=1 \
                                    && make -C /usr/src/redis \
                                        && make -C /usr/src/redis install \
                                            && rm -rf /var/lib/apt/lists/* \
                                                && rm redis.tar.gz \
                                                    && rm -r /usr/src/redis \
                                                        && apt-get purge -y --auto-remove $buildDeps

    首先，之前所有的命令只有一个目的，就是编译、安装 redis 可执行文件。
    因此没有必要建立很多层，这只是一层的事情。因此，这里没有使用很多个 RUN 对一一对应不同的命令，
    而是仅仅使用一个 RUN 指令，并使用 && 将各个所需命令串联起来。将之前的 7 层，简化为了 1 层。
    在撰写 Dockerfile 的时候，要经常提醒自己，这并不是在写 Shell 脚本，而是在定义每一层该如何构建。

    并且，这里为了格式化还进行了换行。Dockerfile 支持 Shell 类的行尾添加 \ 的命令换行方式，以及行首 # 进行注释的格式。
    良好的格式，比如换行、缩进、注释等，会让维护、排障更为容易，这是一个比较好的习惯。

    很多人初学 Docker 制作出了很臃肿的镜像的原因之一，就是忘记了每一层构建的最后一定要清理掉无关文件。

构建镜像

    好了，让我们再回到之前定制的 nginx 镜像的 Dockerfile 来。现在我们明白了这个 Dockerfile 的内容，那么让我们来构建这个镜像吧。

    在 Dockerfile 文件所在目录执行：

    $ docker build -t nginx:v3 .
    Sending build context to Docker daemon 2.048 kB
    Step 1 : FROM nginx
     ---> e43d811ce2f4
     Step 2 : RUN echo '<h1>Hello, Docker!</h1>' > /usr/share/nginx/html/index.html
      ---> Running in 9cdc27646c7b
       ---> 44aa4490ce2c
       Removing intermediate container 9cdc27646c7b
       Successfully built 44aa4490ce2c

    这里我们使用了 docker build 命令进行镜像构建。其格式为：

    docker build [选项] <上下文路径/URL/->
    在这里我们指定了最终镜像的名称 -t nginx:v3，构建成功后，我们可以像之前运行 nginx:v2 那样来运行这个镜像，其结果会和 nginx:v2 一样。


镜像构建上下文（Context）

    如果注意，会看到 docker build 命令最后有一个 .。
    . 表示当前目录，而 Dockerfile 就在当前目录，因此不少初学者以为这个路径是在指定 Dockerfile 所在路径，
    这么理解其实是不准确的。如果对应上面的命令格式，你可能会发现，这是在指定上下文路径。那么什么是上下文呢？

    首先我们要理解 docker build 的工作原理。Docker 在运行时分为 Docker 引擎（也就是服务端守护进程）和客户端工具。
    Docker 的引擎提供了一组 REST API，被称为 Docker Remote API，而如 docker 命令这样的客户端工具，
    则是通过这组 API 与 Docker 引擎交互，从而完成各种功能。因此，虽然表面上我们好像是在本机执行各种 docker 功能，
    但实际上，一切都是使用的远程调用形式在服务端（Docker 引擎）完成。
    也因为这种 C/S 设计，让我们操作远程服务器的 Docker 引擎变得轻而易举。

    当我们进行镜像构建的时候，并非所有定制都会通过 RUN 指令完成，经常会需要将一些本地文件复制进镜像，
    比如通过 COPY 指令、ADD 指令等。而 docker build 命令构建镜像，其实并非在本地构建，
    而是在服务端，也就是 Docker 引擎中构建的。那么在这种客户端/服务端的架构中，如何才能让服务端获得本地文件呢？

    这就引入了上下文的概念。当构建的时候，用户会指定构建镜像上下文的路径，docker build 命令得知这个路径后，
    会将路径下的所有内容打包，然后上传给 Docker 引擎。这样 Docker 引擎收到这个上下文包后，展开就会获得构建镜像所需的一切文件。

    如果在 Dockerfile 中这么写：

    COPY ./package.json /app/

    这并不是要复制执行 docker build 命令所在的目录下的 package.json，
    也不是复制 Dockerfile 所在目录下的 package.json，而是复制 上下文（context） 目录下的 package.json。

    因此，COPY 这类指令中的源文件的路径都是相对路径。
    这也是初学者经常会问的为什么 COPY ../package.json /app 或者 COPY /opt/xxxx /app 无法工作的原因，
    因为这些路径已经超出了上下文的范围，Docker 引擎无法获得这些位置的文件。如果真的需要那些文件，应该将它们复制到上下文目录中去。

    如果目录下有些东西确实不希望构建时传给 Docker 引擎，那么可以用 .gitignore 一样的语法写一个 .dockerignore，该文件是用于剔除不需要作为上下文传递给 Docker 引擎的。





































