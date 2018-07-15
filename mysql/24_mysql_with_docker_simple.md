#### 在 docker 中使用 mysql



```shell
$ docker run -p 3306:3306 --name mymysql -e MYSQL_ROOT_PASSWORD=tiger -d mysql

$ docker container ls -a

$ docker exec -it mymysql bash

root@eae746cd953b:/# mysql -uroot -p
```

