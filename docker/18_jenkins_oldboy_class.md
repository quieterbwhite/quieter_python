#### 老男孩 jenkins 教程笔记

##### 环境准备
```
1. 安装软件 
docker, docker-compose

2. 创建目录
/data/gitlab
/data/jenkins
目录给777权限

3. pull镜像
docker load -i gitlab-ce.tar.gz
docker load -i 


docker pull gitlab/gitlab-ce:latest

docker pull jenkins:lts

docker run -it --name jenkinsci -v /data/jenkins:/var/jenkins_home -p 8080:8080 -p 50000:50000 -p 45000:45000 jenkins/jenkins:lts

docker run -u root -v /home/bwhite/data/jenkins:/var/jenkins_home -p 8005:8080 jenkinszh/jenkins-zh:lts

!!! 上面docker方式都不合适，还是下载 jenkins.war包来用。
使用命令　java -jar jenkins.war --httpPort=7004　来启动服务
```

##### 测试环境
```
机器: sony
ip: 192.168.31.180

jenkins:

    java -jar jenkins.war --httpPort=7004
    psky
    oli

gitlab:

    docker start gitlab
    username: root
    password: oli
```

##### 第一个项目 free style
```
name: my-freestyle-job

build: Execute shell

command:
    env

    echo "hello world"
    
第一次执行不成功，因为没有可用于执行的节点。

进入系统管理，管理节点，去添加一个执行节点。可以把master作为执行节点，就是需要把其executors数量更改为大于1的数。

添加源码管理：

1. 添加git仓库地址
2. 添加用户名密码
```

##### 新建节点
```
可以添加多个用于执行任务的节点。
```

##### 如何使用参数
```
功能在项目里的路径: General -> This project is parameterized

Boolean参数
Choice参数
String参数
Multi-line String参数
File参数
其他

参数值如何使用
1. 构建参数会自动添加为构建过程环境变量
2. 可以通过$parameter或者${parameter}形式使用

就是定义了参数，然后在脚本中去使用

安装的插件 git parameter 也会出现在这里面
可以指定分支，tag等参数，那么在开始构建的时候会弹出来所有的分支或tag，可以选择来进行构建。
这样实现了在一个项目里面支持多个分支/tag的构建。

Build环境变量Report

安装插件 Environment Injector Plugin

Choice参数，就是生成一个参数列表
新增参数:
    Name: OPTION
    Choices: node1, node2, node3
    
然后在脚本中使用该参数 test.sh:
echo ${OPTION}

比如这样就可以实现选择版本进行拉取镜像，创建docker容器。
```

##### 触发构建的方式
```
常用的triggers

1. Build periodically
设定类似cron周期性时间触发构建

2. Poll SCM
设定类似Cron周期性时间触发检查代码变化，只有当代码变动时才触发构建

3. Hooks
1. Giblab hooks
2. Github hooks

4. Events
1. Gerrit events
```

##### 如何触发下游project构建
```
Jenkins Core功能
1. "Build other projects" under "Post build actions"

2. 3中触发条件

Parameterized Trigger plugin-1

更多信息见Parameterized Trigger plugin
支持在build step中触发其他构建
```

##### 如何查看上下游构建视图
```
1. 安装 Build Pipeline Plugin

2. 创建一个Build Pipeline View

视图，文件夹，都是用于管理任务的。比如有100个job等。

当公司组织结构众多的时候有用。对我就没用了。所以，我就暂不关心了。
```

##### 如何使用环境变量
```
Jenkins系统变量

全局变量 Configure System

Slave配置

Job配置

Job Configure

环境变量的生效顺序

全局变量 < Slave < Job < Job injected 

一般不Override系统变量
```

##### 如何并发构建
```
如何enable并发构建
1. Project配置勾选 "Excute concurrent builds if necessary"
2. 每个并发构建使用单独的workspace,默认<workspace path>@<num>
```

##### 其他命令
```
1. 将当前路径加入到环境变量
export PATH=$PATH:$PWD
```

##### 插件
```
git parameter
```
