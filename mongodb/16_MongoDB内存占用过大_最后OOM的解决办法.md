#### MongoDB内存占用过大，最后OOM的解决办法

##### MongoDB被Linux OOM Kill
```
https://blog.piclover.cn/2017/06/01/mongodb-oom-killer/

这问题就大了，进程突然消失就像被kill -9了一样，但是查history记录并没人执行过。
于是 dmesg|grep mongo了一下果然发现问题

与mongodb日志对比发现，被杀的pid与最后一次启动进程的pid一致，可以确认被linux oom(Out of Memory) killer杀了。

而触发oom killer一般是应用程序大量请求内存导致系统内存不足造成的，而为了保证整个系统的稳定linux内核会杀掉某个进程。

Linux 内核根据应用程序的要求分配内存，通常来说应用程序分配了内存但是并没有实际全部使用，为了提高性能，这部分没用的内存可以留作它用，这部分内存是属于每个进程的，内核直接回收利用的话比较麻烦，所以内核采用一种过度分配内存（over-commit memory）的办法来间接利用这部分 “空闲” 的内存，提高整体内存的使用效率。一般来说这样做没有问题，但当大多数应用程序都消耗完自己的内存的时候麻烦就来了，因为这些应用程序的内存需求加起来超出了物理内存（包括 swap）的容量，内核（OOM killer）必须杀掉一些进程才能腾出空间保障系统正常运行。
https://www.vpsee.com/2013/10/how-to-configure-the-linux-oom-killer/

给进程按内存排个序

ps -e -o 'pid,comm,args,rsz,vsz'|sort -nrk4
前三甲的大户都是pid小于5k的一等公民，也不敢动，自然pid五位数又能吃内存的mongodb被选中kill。要是我也选它。

触发oom killer后选择哪个进程被杀，是根据内核特定的算法给每个进程打分从而决定是否被选中，分数可以在

中看到，而设置oom_adj的值可以调整oom killer的行为，比如

echo -17 > /proc/$pid/oom_adj
```

##### 解决办法:
```
https://www.ipcpu.com/2017/01/mongodb-oom/

配置文件里加入了 cacheSizeGB: 3

vim /etc/mongod.conf

storage:
 engine: wiredTiger
 wiredTiger:
  engineConfig:
   cacheSizeGB: 3
```

##### 相关解释
```
MongoDB3.4开始，WiredTiger将会内部缓存将会占用以下（较大的一个）内存空间：

50%的内存减去1GB 
256MB

由于使用了系统缓存，MongoDB实际上会使用掉所有没有被WiredTiger内部缓存和其他应用程序占用的内存空间。文件系统缓存中的数据是被压缩过的

为了调整WiredTiger内部缓存大小，可以通过设定参数storage.wiredTiger.engineConfig.cacheSizeGB或者–wiredTigerCacheSizeGB。避免设置的内部缓存大小大于默认值（个人认为这样处理可能是为了防止内存溢出的问题）

注意：storage.wiredTiger.engineConfig.cacheSizeGB限制的是WiredTiger内部缓存占用内存大小。因为使用文件系统缓存的原因，操作系统会使用剩余的全部内存空间（所以跑着大业务量的mongod的机器内存使用总会100%）。

这个设定（WiredTiger内部缓存默认值）的前提是一个机器上只运行一个mongod实例，如果你的机器上运行了多个mongod实例的话，应该把这个配置相对调低。生产环境不推荐一个机器上启动多个mongod进程。

如果是在容器中运行mongod实例（单个容器往往没有权限使用全部内存），这时候需要把storage.wiredTiger.engineConfig.cacheSizeGB的值设的小于容器可使用的内存空间大小

查看WiredTiger内部缓存到底占用了多少内存的方式是，在mongo shell中之行以下命令

db.runCommand( { serverStatus: 1 } ).wiredTiger.cache["bytes currently in the cache"]:

如果不想重启mongoDB，可以在线修改，如下

db.adminCommand({setParameter: 1, wiredTigerEngineRuntimeConfig: "cache_size=8G"}):
```

##### 办法
```
https://developer.aliyun.com/ask/55228

注意配置cacheSizeGB，建议低于系统内存的50%。更深入的调整还有些Eviction参数，但调整起来比较麻烦。建议先尝试设置cacheSizeGB
```
