#### docker：轻量级图形页面管理之Portainer

甘兵 2018-03-05 14:26:56

>   https://blog.51cto.com/ganbing/2083051

---

## 1.介绍

>   docker 图形化管理提供了很多工具，有Portainer、Docker UI、Shipyard等等，本文主要介绍Portainer。

 Portainer是一个开源、轻量级Docker管理用户界面，基于Docker API，提供状态显示面板、应用模板快速部署、容器镜像网络数据卷的基本操作（包括上传下载镜像，创建容器等操作）、事件日志显示、容器控制台操作、Swarm集群和服务等集中管理和操作、登录用户管理和控制等功能。功能十分全面，基本能满足中小型单位对容器管理的全部需求。

## 2.创建容器

### 2.1下载官方镜像

```
[root@ ganbing /]# docker pull portainer/portainer
Using default tag: latest
latest: Pulling from portainer/portainer
d1e017099d17: Pull complete 
ba5495c717cb: Pull complete 
Digest: sha256:8146a5aae1135a0ccee424488c6867b438be21d1e915903a858d12e8382b817b
Status: Downloaded newer image for portainer/portainer:latest
```

### 2.2单机运行

>   如果仅有一个docker宿主机，则可使用单机版运行，Portainer单机版运行十分简单，只需要一条语句即可启动容器，来管理该机器上的docker镜像、容器等数据。

**创建数据卷：**

```
[root@ganbing ~]# docker volume create portainer_data
portainer_data
```

**运行容器：**

```
[root@ganbing ~]# docker run -d -p 9000:9000 -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer
439cc8a6d44a84f5967534c50d3accc43fbeb578258a52c2683afeb230dd6e04
```

参数说明：
-d：容器在后台运行；
-p 9000:9000 ：宿主机9000端口映射容器中的9000端口
-v /var/run/docker.sock:/var/run/docker.sock ：把宿主机的Docker守护进程(Docker daemon)默认监听的Unix域套接字挂载到容器中；
-v portainer_data:/data ：把宿主机portainer_data数据卷挂载到容器/data目录；

**查看容器进程：**

```
[root@ganbing ~]# docker ps -l
CONTAINER ID        IMAGE                 COMMAND             CREATED             STATUS              PORTS                    NAMES
439cc8a6d44a        portainer/portainer   "/portainer"        13 seconds ago      Up 13 seconds       0.0.0.0:9000->9000/tcp   amazing_clarke
```

**访问服务：**

-   访问方式：[http://IP:9000](http://ip:9000/) ，首次登录需要注册用户，给用户admin设置密码，如下图：

![docker：轻量级图形页面管理之Portainer](https://s1.51cto.com/images/blog/201803/05/5b88849fe1e52c6fb6fa78b74aded19c.png?x-oss-process=image/watermark,size_16,text_QDUxQ1RP5Y2a5a6i,color_FFFFFF,t_100,g_se,x_10,y_10,shadow_90,type_ZmFuZ3poZW5naGVpdGk=)

-   单机版本选择“Local"，点击Connect即可连接到本地docker，如下图：
    ![docker：轻量级图形页面管理之Portainer](https://s1.51cto.com/images/blog/201803/05/d0ac00ebaa10a3cad79cbbe2687b6ab0.png?x-oss-process=image/watermark,size_16,text_QDUxQ1RP5Y2a5a6i,color_FFFFFF,t_100,g_se,x_10,y_10,shadow_90,type_ZmFuZ3poZW5naGVpdGk=)
    注意：从上图可以看出，有提示需要挂载本地 /var/run/docker.socker与容器内的/var/run/docker.socker连接。因此，在启动时必须指定该挂载文件。
-   进入后可以对容器、镜像、网络、数据卷等进行管理，如下图：
    ![docker：轻量级图形页面管理之Portainer](https://s1.51cto.com/images/blog/201803/05/b138b2e9e8f5d0748df6fde86da103c0.png?x-oss-process=image/watermark,size_16,text_QDUxQ1RP5Y2a5a6i,color_FFFFFF,t_100,g_se,x_10,y_10,shadow_90,type_ZmFuZ3poZW5naGVpdGk=)

### 2.3集群运行

>   更多的情况下，我们会有一个docker集群，可能有几台机器，也可能有几十台机器，因此，进行集群管理就十分重要了，Portainer也支持集群管理，Portainer可以和Swarm一起来进行集群管理操作。首先要搭建了一个Swarm，本文不着重介绍swarm集群的安装。

**portainer集群启动：**

-   启动集群参考官方文档：<https://portainer.io/install.html>

    ```
    $ docker service create \
    --name portainer \
    --publish 9000:9000 \
    --replicas=1 \
    --constraint 'node.role == manager' \
    --mount type=bind,src=//var/run/docker.sock,dst=/var/run/docker.sock \
    --mount type=bind,src=//opt/portainer,dst=/data \
    portainer/portainer \
    -H unix:///var/run/docker.sock
    ```

-   启动Portainer之后，首页还是给admin用户设置密码（这里和单机启动一样）。
    ![docker：轻量级图形页面管理之Portainer](https://s1.51cto.com/images/blog/201803/05/35c353abedce986cca4a3c3f91ec4a45.png?x-oss-process=image/watermark,size_16,text_QDUxQ1RP5Y2a5a6i,color_FFFFFF,t_100,g_se,x_10,y_10,shadow_90,type_ZmFuZ3poZW5naGVpdGk=)

-   进入后，如下图所示会发现多了关于swarm的选项，其它配置和单机运行的portainer一样，都很简单：
    ![docker：轻量级图形页面管理之Portainer](https://s1.51cto.com/images/blog/201803/05/c0e9e1e20302f7a8b318173dcce6eabb.png?x-oss-process=image/watermark,size_16,text_QDUxQ1RP5Y2a5a6i,color_FFFFFF,t_100,g_se,x_10,y_10,shadow_90,type_ZmFuZ3poZW5naGVpdGk=)

-   Portainer的基本操作就这么多，具体的操作步骤还需要大家自己去学习理解。

## 3.参考链接

官方网站：<https://portainer.io/> 
官方文档：<https://portainer.readthedocs.io/> 
演示网址：[http://demo.portainer.io](http://demo.portainer.io/) 账号admin 密码 tryportainer