#### 在 docker 中使用 mysql

>   https://dev.mysql.com/doc/refman/5.7/en/docker-mysql-getting-started.html
>
>   http://www.infoq.com/cn/articles/can-mysql-run-in-docker
>
>   http://www.runoob.com/docker/docker-install-mysql.html

```shell
$ docker run -p 3306:3306 --name mymysql -e MYSQL_ROOT_PASSWORD=tiger -d mysql

$ docker container ls -a

$ docker exec -it mymysql bash

root@eae746cd953b:/# mysql -uroot -p
```

