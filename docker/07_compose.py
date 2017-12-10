# -*- coding=utf-8 -*-
# Created Time: 2017年08月05日 星期六 16时18分46秒
# File Name: 07_compose.py

Compose 项目是 Docker 官方的开源项目，负责实现对 Docker 容器集群的快速编排。从功能上看，跟 OpenStack 中的 Heat 十分类似。

Compose 恰好满足了这样的需求。它允许用户通过一个单独的 docker-compose.yml 模板文件（YAML 格式）来定义一组相关联的应用容器为一个项目（project）。

Compose 中有两个重要的概念：

服务（service）：一个应用的容器，实际上可以包括若干运行相同镜像的容器实例。
项目(project)：由一组关联的应用容器组成的一个完整业务单元，在 docker-compose.yml 文件中定义。
Compose 的默认管理对象是项目，通过子命令对项目中的一组容器进行便捷地生命周期管理。

Compose 项目由 Python 编写，实现上调用了 Docker 服务提供的 API 来对容器进行管理。因此，只要所操作的平台支持 Docker API，就可以在其上利用 Compose 来进行编排管理。

安装与卸载

    PIP 安装

        这种方式是将 Compose 当作一个 Python 应用来从 pip 源中安装。

        执行安装命令：

        $ sudo pip install -U docker-compose

        $ docker-compose -h

    容器中执行

        Compose 既然是一个 Python 应用，自然也可以直接用容器来执行它。

        $ curl -L https://github.com/docker/compose/releases/download/1.8.0/run.sh > /usr/local/bin/docker-compose
        $ chmod +x /usr/local/bin/docker-compose


使用

    场景

        下面，我们创建一个经典的 Web 项目：一个 Haproxy，挂载三个 Web 容器。

        创建一个 compose-haproxy-web 目录，作为项目工作目录，并在其中分别创建两个子目录：haproxy 和 web。

            HAProxy是什么

                HAProxy是一个免费的负载均衡软件，可以运行于大部分主流的Linux操作系统上。

                HAProxy提供了L4(TCP)和L7(HTTP)两种负载均衡能力，具备丰富的功能。
                HAProxy的社区非常活跃，版本更新快速（最新稳定版1.7.2于2017/01/13推出）。
                最关键的是，HAProxy具备媲美商用负载均衡器的性能和稳定性。











