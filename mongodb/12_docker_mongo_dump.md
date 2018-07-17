### [Docker MongoDB 数据库备份 并复制到宿主 恢复](https://segmentfault.com/a/1190000012330284)

[**FrontNg**](https://segmentfault.com/u/frontng) 关注作者

2017年12月07日  ·  1k 次阅读

 

#### 一、从宿主连接到MongoDB容器

`docker exec -it <你的MongodDB容器名> /bin/bash`

------

#### 二、使用mongodump命令进行数据库备份

##### 容器中执行

`mongodump -h 127.0.0.1 --port 27017 -d test -o /dump`

| 参数     | 作用                                |
| ------ | --------------------------------- |
| -h     | host                              |
| --port | 端口                                |
| -d     | 指定数据库                             |
| -o     | 指定备份到哪个目录，不指定应该是直接备份到根目录的/dump文件夹 |
| -u     | 用户名                               |
| -p     | 密码                                |

系统备份成功会在/home/dump目录下自动生成一个数据库名的文件夹/test，里面是全部Collection备份的bson文件。

------

#### 三、打包备份文件夹

##### 还是容器中执行

`tar -zcvf test.tar.gz /dump/test`

------

#### 四、从容器复制到宿主

##### Ctrl+D 或输入 `excit` 切回到宿主机

`docker cp <你的MongodDB容器名>:/dump/test.tar.gz /home`

##### 解压

`tar -zxvf /home/test.tar.gz`

##### 解压后，bson解压到 /home/dump/test/

------

#### 五、恢复

`mongorestore -h <IP地址>:<端口> -d <数据库名> /home/dump/test/`