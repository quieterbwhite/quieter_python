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
```