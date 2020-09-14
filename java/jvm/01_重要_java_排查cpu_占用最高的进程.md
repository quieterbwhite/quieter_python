#### 01_重要_java_排查cpu_占用最高的进程

> https://mp.weixin.qq.com/s/4LSFJ2r3CKXzY1ZLvbf9zA  Java 程序该怎么优化？实战篇  

##### 步骤
```
1. 首先，采用 top 命令，找出 CPU 占用最高的进程 PID；

2. 然后，通过 ps -ef | grep PID 查看对应的应用，确认一下是不是你的应用，运维喵别给扣错帽子，说啥咱也不能背锅。

3. 接着，采用 jstack -l PID >> PID.log  获取进程的堆栈信息。

4. 然后，采用 ps -mp PID -o THREAD,tid,time 拿到占用 CPU 最高的线程 TID。

5. 接着，采用 printf "%x\n" tid 获取 16 进制的线程 TID。

6. 最后，采用 grep TID -A20 PID.log 确定是线程哪儿出了问题。

找到代码位置，便可对症下药。

另外，你或许会感觉命令繁琐，其实摆脱命令的困扰，采用 VisualVM 图形化性能监控工具，则会有种土枪换炮的感觉，不过生产上一般还是用命令的居多（言外之意：势必要掌握命令）。
```
