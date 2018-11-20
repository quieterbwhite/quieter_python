#### docker - mysql 注意事项

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
