#### Jenkins


---
Docker+Jenkins+GitLab+Maven+SpringBoot&SpringCloud实现自动化构建镜像与部署详解
https://www.jianshu.com/p/bdb0642b7495

https://www.jianshu.com/p/358bfb64e3a6
基于Jenkins，docker实现自动化部署（持续交互）

[手把手教你用 Gitlab 和 Jenkins 构建持续集成环境](https://cloud.tencent.com/developer/article/1470779)

[实战docker+jenkins+git+registry构建持续集成环境](https://blog.51cto.com/ganbing/2085769)

[基于Jenkins，docker实现自动化部署（持续交互）](https://www.jianshu.com/p/358bfb64e3a6)

[Jenkins安装及自动部署Maven项目](https://juejin.im/post/5be125c151882516d725a851)

['三剑客'之Swarm集群架构、集群管理 、服务管理](https://blog.51cto.com/ganbing/2090290)

##### 安装
```
java -jar jenkins.war --httpPort=7004  

https://juejin.im/post/5cf4a297e51d45595319e2f7

sudo docker run -it -d \
  --rm \
  -u root \
  -p 8099:8080 \
  -v /opt/data/jenkins/data:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v "$HOME":/home \
  --name jenkins jenkinsci/blueocean
```




##### 流程

```shell
开发人员在gitLab上打了一个tag
gitLab把tag事件推送到Jenkins
Jenkins 获取tag源码，编译，打包，构建镜像
Jenkins push 镜像到阿里云仓库
Jenkins 执行远程脚本
5-1. 远程服务器 pull 指定镜像
5-2. 停止老版本容器，启动新版本容器
通知测试人员部署结果

链接：https://www.jianshu.com/p/358bfb64e3a6
```

##### 常用插件

```shell
Maven Integration plugin
docker-build-step
Docker plugin
Gitlab Hook Plugin
GitLab Plugin
SSH Plugin
```

---

##### jenkins更换国内源

```shell
系统管理>>管理插件>>高级
将 [升级站点] 更换为
https://mirrors.tuna.tsinghua.edu.cn/jenkins/updates/current/update-center.json

上面配置的是 清华大学开源软件镜像站

jenkins镜像地址列表
http://mirrors.jenkins-ci.org/status.html

上面的是假加速，害死我了。还需要加上下面的方法

https://www.cnblogs.com/hellxz/p/jenkins_install_plugins_faster.html

操作步骤
以上的配置Json其实在Jenkins的工作目录中

$ cd {你的Jenkins工作目录}/updates  #进入更新配置位置
UndefinedCopy
第一种方式：使用vim
$ vim default.json   #这个Json文件与上边的配置文件是相同的
UndefinedCopy
这里wiki和github的文档不用改，我们就可以成功修改这个配置

使用vim的命令，如下，替换所有插件下载的url

:1,$s/http:\/\/updates.jenkins-ci.org\/download/https:\/\/mirrors.tuna.tsinghua.edu.cn\/jenkins/g
UndefinedCopy
替换连接测试url

:1,$s/http:\/\/www.google.com/https:\/\/www.baidu.com/g
UndefinedCopy
进入vim先输入：然后再粘贴上边的：后边的命令，注意不要写两个冒号！

修改完成保存退出:wq

第二种方式：使用sed
$ sed -i 's/http:\/\/updates.jenkins-ci.org\/download/https:\/\/mirrors.tuna.tsinghua.edu.cn\/jenkins/g' default.json && sed -i 's/http:\/\/www.google.com/https:\/\/www.baidu.com/g' default.json
UndefinedCopy
这是直接修改的配置文件，如果前边Jenkins用sudo启动的话，那么这里的两个sed前均需要加上sudo

重启Jenkins，安装插件试试，简直超速！！

结束
自从发现这个办法后，妈妈再也不用担心 Jenkins插件下载速度慢、安装失败了！

```

---

##### 下载jenkins.war包并运行
```

到平安云镜像站找到下载地址

java -jar jenkins.war --httpPort=8099
```

##### Docker安装Jenkins详解
```
https://www.jianshu.com/p/72d05e43a8f3

docker run -d --restart=always -p 9001:8080 \
-v /usr/local/jenkins/workspace/:/root/.jenkins/workspace \
-v /var/run/docker.sock:/var/run/docker.sock \
-v /usr/bin/git:/usr/bin/git \
-v /usr/local/jdk1.8:/usr/local/jdk1.8 \
-v /usr/local/maven3:/usr/local/maven3 --name jenkins jenkins:latest

```



