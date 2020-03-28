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
```



##### 其他命令
```
1. 将当前路径加入到环境变量
export PATH=$PATH:$PWD
```
