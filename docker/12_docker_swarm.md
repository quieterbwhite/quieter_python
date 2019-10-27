#### Docker Swarm

##### 搭建集群
```shell

Swarm Manager 初始化集群 - 172.16.0.224

    $ docker swarm init --listen-addr <MANAGER-IP>:<PORT>

    $ docker swarm init --advertise-addr 172.16.0.224

    Swarm initialized: current node (wx7wrlkrfvp5tjwkc465765t6) is now a manager.

    To add a worker to this swarm, run the following command:

        docker swarm join --token SWMTKN-1-0n8mcpoybo8vygh2t7zj2w6r4hcr92zhyzm7fc3fp1eh4bgjvj-4ophfjl0dpmp5zg4bla5cmmip 172.16.0.224:2377

    To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructions.

    # 查看当前网络
    $ docker network ls
    NETWORK ID          NAME                DRIVER              SCOPE
    a440fbf5b965        bridge              bridge              local
    a501d9d07850        docker_gwbridge     bridge              local
    2ec4b9db0de8        host                host                local
    lkp9a2pkxk1c        ingress             overlay             swarm
    33413bf1bd56        none                null                local

    # 只有一个manager的话不可靠
    # 可以把至少三个节点都设置成manager节点,他们同时也是worker节点

    # 查看当前节点状态
    $ docker node ls
    ID                            HOSTNAME            STATUS              AVAILABILITY        MANAGER STATUS      ENGINE VERSION
    wx7wrlkrfvp5tjwkc465765t6 *   bwhite              Ready               Active              Leader              18.06.1-ce
    fid2gfrfg67mhhubxtzahqc77     yunhe               Ready               Active                                  19.03.4

    # 提升<yunhe>节点为manager节点
    $ docker node promote yunhe
    Node yunhe promoted to a manager in the swarm.

    # 再次查看节点状态, <yunhe>的status变更为(Reachable)
    $ docker node ls
    ID                            HOSTNAME            STATUS              AVAILABILITY        MANAGER STATUS      ENGINE VERSION
    wx7wrlkrfvp5tjwkc465765t6 *   bwhite              Ready               Active              Leader              18.06.1-ce
    fid2gfrfg67mhhubxtzahqc77     yunhe               Ready               Active              Reachable           19.03.4

    # 当至少有三台服务器 Leader + Reachable + Reachable, 即为高可用状态

Swarm Node 加入工作节点 - 172.16.0.113

    $ docker swarm join --token <TOKEN> <MANAGER-IP>:<PORT>

    $ docker swarm join --token SWMTKN-1-0n8mcpoybo8vygh2t7zj2w6r4hcr92zhyzm7fc3fp1eh4bgjvj-4ophfjl0dpmp5zg4bla5cmmip 172.16.0.224:2377

        This node joined a swarm as a worker.
```

##### 创建测试服务
```shell
创建一个测试用服务

    $ docker service create --name test1 alpine ping www.baidu.com
    hhugk13lis4qn6e1bsidq69td
    overall progress: 1 out of 1 tasks 
    1/1: running   [==================================================>] 
    verify: Service converged

查看当前的服务, 在<bwhite>, <yunhe>上执行命令都是相同的

    $ docker service ls
    ID                  NAME                MODE                REPLICAS            IMAGE               PORTS
    hhugk13lis4q        test1               replicated          1/1                 alpine:latest

查看服务的详细信息

    $ docker service inspect test1

查看服务日志

    $ docker service logs test1
```

##### 创建Nginx服务
```shell
创建Nginx服务

    $ docker service create --name swamnginx --detach=false nginx
    qscbto172w2smz04cbwn4qgfc
    overall progress: 1 out of 1 tasks 
    1/1: running   [==================================================>] 
    verify: Service converged

查看服务

    $ docker service ls
    ID                  NAME                MODE                REPLICAS            IMAGE               PORTS
    qscbto172w2s        swamnginx           replicated          1/1                 nginx:latest        
    hhugk13lis4q        test1               replicated          1/1                 alpine:latest

修改服务,增加暴露一个端口

    $ docker service update --publish-add 8080:80 --detach=false swamnginx
    swamnginx
    overall progress: 1 out of 1 tasks 
    1/1: running   [==================================================>] 
    verify: Service converged

查看暴露端口是否成功

    $ netstat -apn | grep 8080
    (Not all processes could be identified, non-owned process info
    will not be shown, you would have to be root to see it all.)
    tcp6       0      0 :::8080                 :::*                    LISTEN      -

网页访问 http://172.16.0.224:8080/ & http://172.16.0.113:8080/ 可以正常访问到 Nginx

    这就看到我们的 Ingress 网络生效了, 在我们的每一个Node节点都暴露了8080端口, 通过虚拟IP的方式访问到最终提供服务的Nginx容器

    但是现在是一个节点在提供服务,不高可用,应该在每个节点上都启动服务,保证服务高可用

把Nginx变成3个节点

    $ docker service scale swamnginx=2
    swamnginx scaled to 2
    overall progress: 2 out of 2 tasks 
    1/2: running   [==================================================>] 
    2/2: running   [==================================================>] 
    verify: Service converged

查看服务列表 - 可以看到Nginx服务已经有两个实例了, 这时候在访问服务的时候就会通过Vip的方式自动负载均衡

    $ docker service ls
    ID                  NAME                MODE                REPLICAS            IMAGE               PORTS
    qscbto172w2s        swamnginx           replicated          2/2                 nginx:latest        *:8080->80/tcp
    hhugk13lis4q        test1               replicated          1/1                 alpine:latest

验证负载均衡

    修改每个实例的Nginx页面,这样才能观察到负载均衡是否起作用

    # 查看服务
    $ docker service ps swamnginx

    # 选择进入一个容器
    $ docker exec -it container_id bash

    # 修改默认页面
    $ vim /usr/share/nginx/html/index.html
    $ echo 'number one test page' > /usr/share/nginx/html/index.html

    # 再次多次访问页面就会发现会访问到我们修改过的那个实例

    # 容器内部只能通过ingress的服务发现访问到其他实例
    # 可以通过　wget 172.16.0.113:8080 获取到其他实例的页面
```

#### 自己创建网络
```shell
# 查看网络
$ docker network ls

$ docker network create -d overlay swarm-overlay

# 再次查看会发现多了一个 swarm-overlay 网络
$ docker network ls

# 停止/删除服务
$ docker service ls
$ docker service rm swamnginx test1
$ docker service ls

# 新建服务
$ docker service create --network swarm-overlay --name nginx -p 8080:80 --detach=false nginx

$ docker service create --network swarm-overlay --name alpine --detach=false alpine ping www.baidu.com

# 查看服务，刚才创建的两个服务都是使用的我们自定义的网络
$ docker service ls

# 进入alpine服务
$ docker exec -it container_id sh
    # 在容器内部ping另一个实例的名称，可见通过名称可以访问到其他服务
    ping nginx
    wget nginx
```

#### 测试另外一个种负载均衡类型，网络类型
```shell
# 创建新的服务
$ docker service create --name nginx-b --endpoint-mode dnsrr --detach=false nginx

# 进入alpine实例，发现能ping nginx, 但是ping 不通 nginx-b

# 上面命令没有指定网络，现在更新下
$ docker service update --network-add swarm-overlay --detach=false nginx-b

# 现在在alpine能ping通nginx-b

# 以上就是自定义网络的演示

# 删除演示用服务
$ docker service rm alpine nginx nginx-b

# 查看network是否还在, swarm-overlay
$ docker network ls
```

#### 测试service组
```shell
# 查看 stack 相关命令
$ docker stack

# 查看 stack deploy 相关帮助
$ docker stack deploy --help

# 新建服务配置文件, 跟docker compose文件是非常像的
$ vim service.yml

version: "3.4"
services:
    alpine:
        image: alpine
        command:
            - "ping"
            - "www.baidu.com"
        networks:
            - "swarm-overlay"
        deploy:
            replicas: 2
            restart_policy:
                condition: on-failure
            resources:
                limits:
                    cpus: "0.1"
                    memory: 50M
        depends_on:
            - nginx
    nginx:
        image: nginx
        networks:
            - "swarm-overlay"
        ports:
            - "8080:80"
networks:
    swarm-overlay:
        external: true # 外部定义好的

# 参数解释
networks - 一个服务可以属于很多个网络
deploy - 是docker-compose没有的，可以定义很多部署时的属性

# 发布服务
$ docker stack deploy -c service.yml test

# 查看刚才发布的服务
$ docker stack

$ docker stack services test

$ docker service ls

# 访问服务，测试是否正常, 访问每个机器上的nginx服务

$ docker service ps test_apline

$ doker stack rm test
$ docker stack deploy -c service.yml test 
```

#### 搭建微服务
```shell
搭建好了swarm集群环境,server01,server02,server03三台虚拟机。每一台既是manager节点,也是worker节点。

服务间的通讯，也就是服务发现

从微服务的角度考虑

有的服务是专门给其他服务使用的，像message-service, user-service, course-service

还有的服务是需要给客户端访问的，像api-gateway, A-edge-service, B-edge-service

对应到swarm上，这种服务之间的通讯，

有的需要暴露出服务端口给客户端访问，使用vip模式

有的不需要端口，而是直接通过名字，通过dns去实现容器间的通讯，也就是使用dnsrr模式

确定这个之后，想想我们首先需要做的是什么，是先改造服务间的访问方式

改造完成之后，需要构建镜像推送到镜像仓库。

service.yml

version: "3.4"
services:
    message-service:
        image: hub.psky.com:8080/micro-service/message-service:latest
        deploy:
            endpoint_mode: dnsrr
            replicas: 2
            resources:
                limits:
                    cpus: "0.2"
                    memory: "128M"
            restart_policy:
                condition: on-failure

    user-service:
        image: hub.psky.com:8080/micro-service/user-service:latest
        deploy:
            endpoint_mode: dnsrr
            resources:
                limits:
                    cpus: "0.2"
                    memory: "512M"

    user-edge-service:
        image: hub.psky.com:8080/micro-service/user-edge-service:latest
        deploy:
            endpoint_mode: vip
            resources:
                limits:
                    cpus: "0.2"
                    memory: "512M"
            placement:
                constraints: [ node.role == manager]
        healthcheck:
            test: ["CMD", "curl", "-f", "http://wwww.psky.com/user/login"]
            interval: 60s
            timeout: 10s
            retries: 3
        ports:
            - "8082:8082"
        depends_on:
            - user-service
            - message-service

    course-service:
        image: hub.psky.com:8080/micro-service/course-service:latest
        deploy:
            endpoint_mode: dnsrr
            resources:
                limits:
                    cpus: "0.2"
                    memory: "512M"
        depends_on:
            - user-service

    course-edge-service:
        image: hub.psky.com:8080/micro-service/course-edge-service:latest
        deploy:
            endpoint_mode: vip
            resources:
                limits:
                    cpus: "0.2"
                    memory: "512M"
        ports:
            - "8081:8081"
        depends_on:
            - user-edge-service

    api-gateway:
        image: hub.psky.com:8080/micro-service/api-gate-zuul:latest
        deploy:
            endpoint_mode: vip
            resources:
                limits:
                    cpus: "0.2"
                    memory: "512M"
        ports:
            - "8080:8080"
        depends_on:
            - user-edge-service
            - course-edge-service

networks:
    default:
        external:
            name: swarm-overlay

把这个配置文件service.yml, 拷贝到服务器上

# 发布服务
$ docker stack deploy -c services.yml ms

$ docker service ls

# web ip地址加端口访问，确定服务都启动

# Nginx搭建负载均衡

# 拉取镜像
$ docker pull nginx

# 进入镜像，看配置文件应该挂载到哪个目录
$ docker run -it --entrypoint bash nginx

    $ cd /etc/nginx/conf.d/

vim name.conf

upstream psky {
    server 192.168.1.17:8080;
    server 192.168.1.18:8080;
    server 192.168.1.19:8080;
}

server {

    listen 80;
    server_name www.psky.com;

    location / {
        proxy_pass http://psky;
    }
}

# 写一个启动Ningx的命令
$ docker run -idt -p 80:80 -v `pwd`/name.conf:/etc/nginx/conf.d/default.conf nginx

$ netstat -apn | grep 80

# 现在通过域名访问服务

# 扩容某一个服务
$ docker service scale ms_api-gateway=3 --detach=false

# 查看扩容后的服务, 可以看到ms_api-gateway服务已经起了三个服务
$ docker service ls

# 查看扩容后的三个服务都在哪些机器上
$ docker service ps ms_api-gateway

# 到每台机器上查看服务是否已经起来
$ docker ps

# 可以使用update更新已经启动的服务, 这里提升cpu使用率
$ docker service update ms_course-edge-service --limit-cpu 0.5 --detach=false

# 查看服务是否更新成功
$ docker service inspect ms_course-edge-service

    这里面有个更新状态的字段，可以看到开始更新的时间，结束更新时间等

    更新是会重启服务的

# 除了使用命令方式更新，还是以编辑配置文件
# 编辑配置文件过后，重新部署服务
$ docker stack deploy -c services.yml ms
# 存在的服务会更新
# 不存在的服务会创建

# 查看日志
docker logs -f commit_id

# 如何让一个服务运行在manager节点上

# 查看当前的node,看看当前的Leader是哪一个, 是server02
$ docker node ls

# 到Leader节点上运行命令, demote, 取消manager节点功能
$ docker node demote server01
$ docker node demote server03

# 所以当前server02是manager节点, server01,server03是worker节点

# 由于某种原因原先运行在server03 worker节点上的服务想要运行在server02上，应该怎么办呢
# 修改这个服务的配置文件，增加placement配置
placement:
    constraints: [ node.role == manager]


```