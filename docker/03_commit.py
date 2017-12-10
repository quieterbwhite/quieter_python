# -*- coding=utf-8 -*-
# Created Time: 2017年08月05日 星期六 09时51分38秒
# File Name: 03_commit.py

利用 commit 理解镜像构成

直接使用这些镜像是可以满足一定的需求，而当这些镜像无法直接满足需求时，
我们就需要定制这些镜像。接下来的几节就将讲解如何定制镜像。

现在让我们以定制一个 Web 服务器为例子，来讲解镜像是如何构建的。

docker pull nginx

docker run --name webserver -d -p 80:80 nginx

这条命令会用 nginx 镜像启动一个容器，命名为 webserver，并且映射了 80 端口，
这样我们可以用浏览器去访问这个 nginx 服务器。

现在，假设我们非常不喜欢这个欢迎页面，我们希望改成欢迎 Docker 的文字，我们可以使用 docker exec 命令进入容器，修改其内容。

$ docker exec -it webserver bash
root@3729b97e8226:/# echo '<h1>Hello, Docker!</h1>' > /usr/share/nginx/html/index.html
root@3729b97e8226:/# exit
exit

我们以交互式终端方式进入 webserver 容器，并执行了 bash 命令，也就是获得一个可操作的 Shell。

然后，我们用 <h1>Hello, Docker!</h1> 覆盖了 /usr/share/nginx/html/index.html 的内容。

现在我们再刷新浏览器的话，会发现内容被改变了。

我们修改了容器的文件，也就是改动了容器的存储层。我们可以通过 docker diff 命令看到具体的改动。

docker diff webserver

现在我们定制好了变化，我们希望能将其保存下来形成镜像。

要知道，当我们运行一个容器的时候（如果不使用卷的话），我们做的任何文件修改都会被记录于容器存储层里。
而 Docker 提供了一个 docker commit 命令，可以将容器的存储层保存下来成为镜像。
换句话说，就是在原有镜像的基础上，再叠加上容器的存储层，并构成新的镜像。
以后我们运行这个新镜像的时候，就会拥有原有容器最后的文件变化。

docker commit 的语法格式为：

docker commit [选项] <容器ID或容器名> [<仓库名>[:<标签>]]
我们可以用下面的命令将容器保存为镜像：

$ docker commit \
            --author "Tao Wang <twang2218@gmail.com>" \
            --message "修改了默认网页" \
            webserver \
            nginx:v2
            sha256:07e33465974800ce65751acc279adc6ed2dc5ed4e0838f8b86f0c87aa1795214

其中 --author 是指定修改的作者，而 --message 则是记录本次修改的内容。
这点和 git 版本控制相似，不过这里这些信息可以省略留空。

我们可以在 docker images 中看到这个新定制的镜像：

$ docker images nginx

docker run --name web2 -d -p 81:80 nginx:v2

慎用 docker commit

    使用 docker commit 命令虽然可以比较直观的帮助理解镜像分层存储的概念，但是实际环境中并不会这样使用。

    使用 docker commit 意味着所有对镜像的操作都是黑箱操作，生成的镜像也被称为黑箱镜像，换句话说，
    就是除了制作镜像的人知道执行过什么命令、怎么生成的镜像，别人根本无从得知。

    而且，回顾之前提及的镜像所使用的分层存储的概念，除当前层外，之前的每一层都是不会发生改变的，换句话说，
    任何修改的结果仅仅是在当前层进行标记、添加、修改，而不会改动上一层。
    如果使用 docker commit 制作镜像，以及后期修改的话，每一次修改都会让镜像更加臃肿一次，
    所删除的上一层的东西并不会丢失，会一直如影随形的跟着这个镜像，即使根本无法访问到™。这会让镜像更加臃肿。

    docker commit 命令除了学习之外，还有一些特殊的应用场合，比如被入侵后保存现场等。
    但是，不要使用 docker commit 定制镜像，定制行为应该使用 Dockerfile 来完成。
    下面的章节我们就来讲述一下如何使用 Dockerfile 定制镜像。



























