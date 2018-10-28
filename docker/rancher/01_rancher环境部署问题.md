1. 部署rancher agent

    待部署机器, 配置/etc/docker/daemon.json( 10.78.115.167可以为你的IP )

    $ sudo vim /etc/docker/daemon.json
         {

```
{
"registry-mirrors": [
"https://571cbuth.mirror.aliyuncs.com",  我的镜像加速器
"https://2lqq34jg.mirror.aliyuncs.com",
"https://pee6w651.mirror.aliyuncs.com",
"https://registry.docker-cn.com",
"http://hub-mirror.c.163.com"
],
```

​                "insecure-registries":["10.78.115.167:5000"],  # 搭建私有仓库用

            	"dns": ["8.8.8.8", "8.8.4.4", "172.16.0.113"]
         }

        $ sudo service docker restart

参照自：https://docs.docker.com/install/linux/linux-postinstall/#specify-dns-servers-for-docker



2. 创建rancher server以后，创建rancher agent后UI界面不显示，以及查看agent容器异常。

{ERROR: DNS Checking loopback IP address 127.0.0.0/8, localhost or ::1 configured as the DNS server on the host file /etc/resolv.conf, can’t accept it}
   解决办法：
        /etc/resolv.conf 文件添加 nameserver  local IP   例如： nameserver  10.78.115.167然后重启容器
