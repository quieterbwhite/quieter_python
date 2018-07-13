# [mongodb 备份、还原、导入、导出简单操作](https://segmentfault.com/a/1190000006236494)



一、 **mongodump备份数据库**

1.一般常用的备份命令格式

```
mongodump -h IP --port 端口 -u 用户名 -p 密码 -d 数据库 -o 文件存在路径 
```

###### 如果想导出所有数据库，可以去掉-d

2.导出数据库
`[root@local ~]# mongodump -h 127.0.0.1 --port 30216 -d test -uxxxx -pxxxxx -o home/mongodb/`
`connected to: 10.10.3.245:30216`
`Thu Aug 11 02:15:04.529 DATABASE: test to /home/mongodb/test`

二、**mongorestore还原数据库**
1.常用命令格式

```
mongorestore -h IP --port 端口 -u 用户名 -p 密码 -d 数据库 --drop 文件存在路径
```

`[root@localhost mongodb]# mongorestore -d test /home/mongodb/test #test这个数据库的备份路径`

###### 这二个命令，可以实现数据库的备份与还原，文件格式是json和bson的

三、**mongoexport导出表，或者表中部分字段**

1.常用命令格式

```
mongoexport -h IP --port 端口 -u 用户名 -p 密码 -d 数据库 -c 表名 -f 字段
```

> -q 条件导出 --csv -o 文件名 上面的参数好理解，重点说一下：
> -f 导出指字段，以字号分割，-f name,email,age导出name,email,age这三个字段
> -q 可以根查询条件导出，-q '{ "_id" : "10001" }' 导出uid为100的数据
> --csv 表示导出的文件格式为csv的，这个比较有用，因为大部分的关系型数据库都是支持csv，在这里有共同点

2.导出整张表

```
[root@localhost mongodb]# mongoexport -d test -c users -o /home/mongodb/test/users.dat 
connected to: 127.0.0.1 
exported 24 records 
```

3.导出表中部分字段

```
[root@localhost mongodb]# mongoexport -d test -c users --csv -f uid,name,sex -o test/users.csv 
connected to: 127.0.0.1 
exported 24 records 
```

4.根据条件敢出数据

```
[root@localhost mongodb]# mongoexport -d test -c users -q '{uid:{$gt:1}}' -o test/users.json 
connected to: 127.0.0.1 
exported 12 records 
```

四、**mongoimport导入表，或者表中部分字段**

1.常用命令格式

1.1 还原整表导出的非csv文件

```
mongoimport -h IP --port 端口 -u 用户名 -p 密码 -d 数据库 -c 表名 --upsert --drop 文件名
```

###### 重点说一下--upsert，其他参数上面的命令已有提到，--upsert 插入或者更新现有数据

1.2 还原部分字段的导出文件

```
mongoimport -h IP --port 端口 -u 用户名 -p 密码 -d 数据库 -c 表名 --upsertFields 字段 --drop 文件名  

--upsertFields根--upsert一样
```

1.3 还原导出的csv文件

```
mongoimport -h IP --port 端口 -u 用户名 -p 密码 -d 数据库 -c 表名 --type 类型 --headerline --upsert--drop 文件名
```

###### 上面三种情况，还可以有其他排列组合的。

2.还原导出的表数据

```
[root@localhost mongodb]# mongoimport -d test -c users --upsert test/users.dat 
connected to: 127.0.0.1 
............
```

3.部分字段的表数据导入

```
[root@localhost mongodb]# mongoimport -d test -c users  --upsertFields uid,name,sex  test/users.dat  
connected to: 127.0.0.1  
............................................... 
```

4.还原csv文件

```
[root@localhost mongodb]# mongoimport -d test -c users --type csv --headerline --file test/users.csv 
connected to: 127.0.0.1 
...........................................
```