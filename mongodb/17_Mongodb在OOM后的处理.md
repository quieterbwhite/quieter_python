# Mongodb在OOM后的处理

[ID王墨](https://www.jianshu.com/u/b6c1d46b2880)关注

> https://www.jianshu.com/p/629ab5612b92
> http://www.ruanyifeng.com/blog/2016/03/systemd-tutorial-part-two.html

2017.07.30 20:42:25字数 1,065阅读 543

同步自我的个人博客[墨语的后花园](https://link.jianshu.com/?t=https%3A%2F%2Fwww.mosdev.xyz%2F)，请多多指教。

------

# 原因

在Linux中使用Mongodb的时候，尤其是单机使用的时候，就会出现OOM（Out of Memory）的情况，当此进程是在root权限下执行的时候，系统在为了保证不出现重启这类的重大事件的情况下，就会选择将目前系统中的高消耗低优先级的进程被杀死，选择的方法是安装PID的序号来进行选择的，而不是按照用户来进行选择的。

出现这种的原因是因为Mongodb本身是不管了自己本身的内存的分配和回收的，而是内存管理的工作交给系统自己来进行处理。当系统本身的物理内存页消耗完的时候，如果应用本身还在请求内存，这个时候就会出现OOM，此时系统会进行一次内存管理，回收大部分的内存来减少系统自己的消耗。

# 解决办法

在这种情况下，如果不考虑使用主从服务器或者将Mongodb独立出来的方式的话，基本就只能考虑限制Mongodb自己本身的内存消耗或者在发现进程被杀之后将其重启。

## cgroup限制内存使用

在现在的linux操作系统中，可以考虑使用cgroup来现在一个进程的使用。CGroup 技术被广泛用于 Linux 操作系统环境下的物理分割，是 Linux Container 技术的底层基础技术，是虚拟化技术的基础。作为cgroup本身来说，它完全可以被用来限制基于任何用户或者是任何应用程序的资源限制。

### 安装

执行以下命令安装`cgroup`的本体及其依赖：

```
sudo apt install cgroup-bin cgroup-lite cgroup-tools cgroupfs-mount libcgroup1
```

### 配置Cgroup

这里就以限制Mongodb的内存使用来进行配置示例，首先在cgroup的配置中增加对内存限制的配置，增加一个`limitmongomem`的组，在其中对Mongodb的内存限制为3G：

```
# vim /etc/cgconfig.conf
group limitmongomem{
    memory {
        memory.limit_in_bytes = 3G;
    }
}
```

#### 配置

1. 启用这个配置

   ```
   # 在root用户执行
   cgconfigparser -l  /etc/cgconfig.conf
   ```

   然后可以在`/sys/fs/cgroup`文件夹下中可以看到多了一个`limitmongomem`的配置

2. 将用户、应用和cgroup绑定

   现在需要的是将Mongodb和`limitmongomem`绑定在一起：

   ```
   # vim /etc/cgrules.conf
   # user:process                         subsystems        group
   root:mongod                             memory       limitmongomem
   deploy:mongod                           memory       limitmongomem
   ```

3. 启用这配置

   ```
   # 在root用户下执行
   cgrulesengd
   ```

   此时会开启一个服务，它会自动监控符合规则的进程，然后将这些进程配置到对应的cgroup策略中从而达到限制资源的目的。

## 自动重启

如果在重启造成的损失影响不大的时候，其实在这种情况下还可以考虑使用自动重启的方式来解决这个问题。其实如果在合适的情况下，还是使用独立的服务器或者主从的方式来进行使用。

#### 使用monit

1. 安装

   ```
   sudo apt install monit
   ```

2. 创建一个monit配置目录放置配置文件：

   ```
   sudo mkdir -p /etc/monit/conf.d
   ```

3. 创建一个Mongodb的配置文件

   ```
   # vim /etc/monit/conf.d/mongod.conf
   check process mongod matching "/usr/bin/mongod"
      group database
      start program = "/sbin/start mongod"
      stop  program = "/sbin/stop mongod"
      if failed host 127.0.0.1 port 27017 protocol http
        and request "/" with timeout 10 seconds then restart
      if 5 restarts within 5 cycles then timeout
   ```

4. 重启服务使其生效：

   ```
   sudo service monit restart
   ```

#### 使用supervisor

1. 使用Ubuntu自带的安装命令安装，而不使用pip安装时因为服务器中的python环境异常的混乱：

   ```
   sudo apt install supervisor
   ```

2. 创建配置文件夹：

   ```
   sudo mkdir -p /etc/supervisor/conf.d
   ```

3. 编写配置文件：

   ```
   # vim /etc/supervisor/conf.d/mongod.conf
   [program:mongod]
   command = mongod
   user = root
   autostart = true
   autorestart = true
   stderr_logfile = /var/log/mongod.log
   stdout_logfile = /var/log/mongod_error.log
   ```

4. 重启supervisor服务：

   ```
   sudo service supervisor start
   ```

5. 启动配置：

   ```
   sudo supervisorctl start
   ```

#### systemd的自动重启服务

当安装好Mongodb服务后，注册service服务后，就可在将其设置为自动重启了：

修改一下配置就行：

```
[Service]
Restart=always
```
