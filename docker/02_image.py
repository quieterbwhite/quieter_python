# -*- coding=utf-8 -*-
# Created Time: 2017年08月05日 星期六 00时21分14秒
# File Name: 02_image.py

1. 镜像

    获取镜像

        docker pull [选项] [Docker Registry地址]<仓库名>:<标签>

        具体的选项可以通过 docker pull --help 命令看到，这里我们说一下镜像名称的格式。

        $ docker pull ubuntu:14.04
        14.04: Pulling from library/ubuntu
        bf5d46315322: Pull complete
        9f13e0ac480c: Pull complete
        e8988b5b3097: Pull complete
        40af181810e7: Pull complete
        e6f7c7e5c03e: Pull complete
        Digest: sha256:147913621d9cdea08853f6ba9116c2e27a3ceffecf3b492983ae97c3d643fbbe
        Status: Downloaded newer image for ubuntu:14.04

    运行

        $ docker run -it --rm ubuntu:14.04 bash
        root@e7009c6ce357:/# cat /etc/os-release
        NAME="Ubuntu"
        VERSION="14.04.5 LTS, Trusty Tahr"
        ID=ubuntu
        ID_LIKE=debian
        PRETTY_NAME="Ubuntu 14.04.5 LTS"
        VERSION_ID="14.04"
        HOME_URL="http://www.ubuntu.com/"
        SUPPORT_URL="http://help.ubuntu.com/"
        BUG_REPORT_URL="http://bugs.launchpad.net/ubuntu/"
        root@e7009c6ce357:/# exit
        exit
        $

    docker run 就是运行容器的命令，具体格式我们会在后面的章节讲解，我们这里简要的说明一下上面用到的参数。

    -it：这是两个参数，一个是 -i：交互式操作，一个是 -t 终端。我们这里打算进入 bash 执行一些命令并查看返回结果，因此我们需要交互式终端。
    --rm：这个参数是说容器退出后随之将其删除。默认情况下，为了排障需求，退出的容器并不会立即删除，除非手动 docker rm。我们这里只是随便执行个命令，看看结果，不需要排障和保留结果，因此使用 --rm 可以避免浪费空间。
    ubuntu:14.04：这是指用 ubuntu:14.04 镜像为基础来启动容器。
    bash：放在镜像名后的是命令，这里我们希望有个交互式 Shell，因此用的是 bash。

    进入容器后，我们可以在 Shell 下操作，执行任何所需的命令。这里，我们执行了 cat /etc/os-release，这是 Linux 常用的查看当前系统版本的命令，从返回的结果可以看到容器内是 Ubuntu 14.04.5 LTS 系统。

    最后我们通过 exit 退出了这个容器。

    docker inspect ubuntu:14.04   可以看到关于这个容器的更多详细信息, 结果是json格式输出

    容器使用 bridge桥接方式通信，它是docker容器默认使用的网络驱动

    访问


列出镜像

    要想列出已经下载下来的镜像，可以使用 docker images 命令。

    $ docker images
    REPOSITORY           TAG                 IMAGE ID            CREATED             SIZE
    redis                latest              5f515359c7f8        5 days ago          183 MB

    列表包含了仓库名、标签、镜像 ID、创建时间以及所占用的空间。

虚悬镜像

    由于新旧镜像同名，旧镜像名称被取消，从而出现仓库名、标签均为 <none> 的镜像。
    这类无标签镜像也被称为 虚悬镜像(dangling image)

    $ docker images -f dangling=true
    REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
    <none>              <none>              00285df0df87        5 days ago          342 MB


    一般来说，虚悬镜像已经失去了存在的价值，是可以随意删除的，可以用下面的命令删除。

    $ docker rmi $(docker images -q -f dangling=true)

中间层镜像

    默认的 docker images 列表中只会显示顶层镜像，如果希望显示包括中间层镜像在内的所有镜像的话，需要加 -a 参数。

    $ docker images -a

    这样会看到很多无标签的镜像，与之前的虚悬镜像不同，这些无标签的镜像很多都是中间层镜像，是其它镜像所依赖的镜像。
    这些无标签镜像不应该删除，否则会导致上层镜像因为依赖丢失而出错。

列出部分镜像

    不加任何参数的情况下，docker images 会列出所有顶级镜像

    根据仓库名列出镜像
    $ docker images ubuntu

    列出特定的某个镜像，也就是说指定仓库名和标签
    $ docker images ubuntu:16.04

    除此以外，docker images 还支持强大的过滤器参数 --filter，或者简写 -f。
    $ docker images -f since=mongo:3.2

    想查看某个位置之前的镜像也可以，只需要把 since 换成 before 即可。
    此外，如果镜像构建时，定义了 LABEL，还可以通过 LABEL 来过滤。
    $ docker images -f label=com.example.version=0.1
















