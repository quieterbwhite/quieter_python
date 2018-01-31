# MongoDB 复制数据库，集合

## 复制数据库
```
使用 copyDatabase命令完成复制数据库，

格式：copyDatabase(fromdb,todb,fromhost[,username,password])

fromdb：源数据库名称

todb：目标数据库名称

fromhost：源数据库地址，本地和远程都可以

username：远程数据库用户名

password：远程数据密码

例子1、将本地db2库复制本地，并重命名db1

> db.copyDatabase("db2","db1","localhost")
例子2、将远程victory数据库复制到本地victory数据库中

db.copyDatabase("victory","victory","192.168.250.91:63008","用户名","密码");

或者:

用一个mongo的可视化工具，先把本地数据导出，json格式的文件，再用可视化工具连接服务器上的数据库，将数据导入进去即可。
```

## 复制集合
```
db.runCommand({cloneCollection:"集合",from:"原机器",copyIndexes:false}),copyIndexes:是否复制索引

> db.runCommand({cloneCollection:"test.t1",from:"132.42.33.175:28010"})
{ "ok" : 1 }
```
