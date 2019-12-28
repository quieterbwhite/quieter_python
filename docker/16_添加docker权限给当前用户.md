## [添加docker权限给当前用户，使docker命令免sudo](https://www.cnblogs.com/codeaaa/p/9041533.html)

如果还没有 docker group 就添加一个：



```
sudo groupadd docker 
```

 

将用户加入该 group 内。然后退出并重新登录就生效啦。



```
sudo gpasswd -a ${USER} docker 
```


重启 docker 服务



```
sudo service docker restart 
```

或

```
sudo systemctl restart docker
```

 

切换当前会话到新 group 或者重启 X 会话

```
newgrp  docker
```

或者

```
pkill X 
```


注意，最后一步是必须的，否则因为 groups 命令获取到的是缓存的组信息，刚添加的组信息未能生效，所以 docker images 执行时同样有错。


来源：https://blog.csdn.net/wzhi2001/article/details/46352417