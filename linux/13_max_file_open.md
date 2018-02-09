# ubuntu 设置最大文件打开数

## 配置方式
```
大家知道linux下可以通过ulimit -n查看或者设置最大文件打开数，
由于linux下一切皆是文件，包括网络连接数，因此默认值1024在运行web app的服务器上是个瓶颈。
但是通过ulimit -n设置的值只对当前登录session有效，所以很多人选择将该命令加到~/.bashrc或者/etc/profile，
这里提供一个一劳永逸的办法：修改/etc/security/limits.conf，加入：

*    hard    nofile    102400
*    soft    nofile    102400

soft 应用级别
hard 操作系统级别
* 表示所有用户

生效:
    1. 重载会话设置
    2. 重启

可以用 ulimit -a 查看目前会话中的所有核心配置
```

## 验证效果
```
那么,我们如何来验证配置是否起作用了呢?在 Linux 系统中,所有的进程都会有 一个临时的核心配置文件描述,存放路径在/proc/进程号/limit

$ ps -elf | grep nginx

$ cat /proc/进程号/limits

注意其中 max open files 的值
```

## 注意
```
请注意在生产环境下,各位读者一定要确保 Nginx 工作进程的配置信息是经
过了优化设量的 , 否则 Nginx 对并发请求的处理能力会大打折扣。
```
