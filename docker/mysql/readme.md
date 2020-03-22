#### docker - mysql 注意事项

##### ref
```
https://www.jianshu.com/p/c5e9c21c87e7
```

##### 获取docker主机ip
```
> https://www.cnblogs.com/yhtong/p/8070346.html

获取docker主机 IP

docker-machine ip
192.168.99.100

获取 docker container ip：---注意，并不能直接访问container。

 ---------------------- bwhite@os ~/data/mysql last:1 ----------------------
$ docker inspect micro-mysql --format '{{ .NetworkSettings.IPAddress }}' 
172.17.0.2
```

##### another command
```
docker run -p 3306:3306 --name mysql --restart=always --privileged=true -v $PWD/conf:/etc/mysql/conf.d -v $PWD/logs:/logs -v $PWD/data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root -v /etc/localtime:/etc/localtime:ro -d mysql:5.6 --lower_case_table_names=1


**备注**
--restart=always 跟随docker启动
--privileged=true 容器root用户享有主机root用户权限
-v 映射主机路径到容器
-e MYSQL_ROOT_PASSWORD=root 设置root用户密码
-d 后台启动
--lower_case_table_names=1 设置表名参数名等忽略大小写
```
