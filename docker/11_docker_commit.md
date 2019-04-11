# [docker commit使用](https://www.cnblogs.com/waterlufei/p/6682345.html)

> http://www.runoob.com/docker/docker-commit-command.html
>
> https://www.cnblogs.com/lsgxeva/p/8746644.html

我们运行的容器可能在镜像的基础上做了一些修改，有时候我们希望保存起来，封装成一个更新的镜像

docker自己提供的有commit功能

我们以centos为例，现在我们要在一个裸的centos上面安装vim编辑器，并且把这个功能保存下来，封装成一个能执行vim命令的centos镜像

拉去最新centos镜像：docker pull centos

进入镜像内部： docker run -it centos /bin/bash     备注：/bin/bash不要忘了

[root@202 ~]# docker run -it centos /bin/bash
[root@afcaf46e8305 /]#

afcaf46e8305是产生的容器ID，前面运行的时候不要-d后台运行了，不然会进不去容器内部的

[root@afcaf46e8305 /]# yum update

[root@afcaf46e8305 /]# yum install -y vim 

安装完了后：exit退出容器

然后把容器打包成镜像：

root@202 ~]# docker commit afcaf46e8305 centos-vim

完成后docker images查看镜像就会发现centos-vim这个镜像了

我们再用刚刚的方法进去centos-vim这个镜像,

[root@7f2d42f3e0a3 /]# vim --version

就可以看到vim的信息了