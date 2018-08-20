#### 关于docker的各种点点

##### 删除docker0网卡
> https://segmentfault.com/q/1010000004213164
```
虚拟网卡docker0其实是一个网桥，如果想删除它，只需要按照删除网桥的方法即可。

#ifconfig docker0 down
#brctl delbr docker0

docker0这个网桥是在启动Docker Daemon时创建的，因此，这种删除方法并不能根本上删除docker0，下次daemon启动（假设没有指定-b参数）时，又会自动创建docker0网桥。
```
