#### Jenkins

---

[手把手教你用 Gitlab 和 Jenkins 构建持续集成环境](https://cloud.tencent.com/developer/article/1470779)

[实战docker+jenkins+git+registry构建持续集成环境](https://blog.51cto.com/ganbing/2085769)

[基于Jenkins，docker实现自动化部署（持续交互）](https://www.jianshu.com/p/358bfb64e3a6)

[Jenkins安装及自动部署Maven项目](https://juejin.im/post/5be125c151882516d725a851)

['三剑客'之Swarm集群架构、集群管理 、服务管理](https://blog.51cto.com/ganbing/2090290)



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
```

---

##### 下载jenkins.war包并运行
```

到平安云镜像站找到下载地址

java -jar jenkins.war --httpPort=8099
```
