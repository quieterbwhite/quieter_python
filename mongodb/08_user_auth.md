# MongoDB 权限,远程访问,用户名密码
> https://zhuanlan.zhihu.com/p/26215701  mongodb操作之用户篇  
> http://www.cnblogs.com/hanyinglong/p/5704320.html  MongoDB学习笔记—权限管理  

## 安装运行
```
Install mongodb on ubuntu

    https://docs.mongodb.com/manual/tutorial/install-mongodb-enterprise-on-ubuntu/

配置文件

    /etc/mongod.conf

图形化客户端工具

    robomongo
```

全新安装的MongoDB绑定的本地IP且没有开启用户验证。  
我们需要在没有开启验证时创建用户，然后再开启验证即可。  

MongoDB 权限系统比较灵活，可以通过各种权限设置方便地进行权限管理。  
## mongodb用户权限列表
```
Read：允许用户读取指定数据库

readWrite：允许用户读写指定数据库

dbAdmin：允许用户在指定数据库中执行管理函数，如索引创建、删除，查看统计或访问system.profile

userAdmin：允许用户向system.users集合写入，可以找指定数据库里创建、删除和管理用户

clusterAdmin：只在admin数据库中可用，赋予用户所有分片和复制集相关函数的管理权限。

readAnyDatabase：只在admin数据库中可用，赋予用户所有数据库的读权限

readWriteAnyDatabase：只在admin数据库中可用，赋予用户所有数据库的读写权限

userAdminAnyDatabase：只在admin数据库中可用，赋予用户所有数据库的userAdmin权限

dbAdminAnyDatabase：只在admin数据库中可用，赋予用户所有数据库的dbAdmin权限。

root：只在admin数据库中可用。超级账号，超级权限
```

在系统只需要进行简单的权限管理，防止别人随意访问数据库。只需要开启验证，创建一个需要用用户名密码登录的超级用户就可以了。  
如果涉及到不同系统不同人员那么就需要用到上述各种角色来划清界限了。  
下面演示只有超级用户验证的简单方案。

## 创建用户
```
$ mongo

// 切换到admin数据库，因为管理员需要在admin数据库下创建
> use admin

// 查看当前用户
> db.system.users.find()

// 创建用户
MongoDB Enterprise > db.createUser({
... user:"root",
... pwd:"tiger",
... roles:["root"]
... })

// 创建管理员后，需要给管理员授权，否则无权限操作用户
> db.auth("root", "tiger")

如果结果返回1，则表示授权成功，返回0则表示失败
```

## 开启 MongoDB 权限验证
```
修改配置文件

    > vim /etc/mongod.conf
    
    net:
  		port: 27017     # 阿里云的话记得开放端口
  		bindIp: 0.0.0.0

    添加:
        #security:
        security: 
          authorization: enabled
    :wq

重启MongoDB

    sudo systemctl restart mongod.service
```

## 访问
```
$ mongo --host x.x.x.x --port 27017 -u "root" -p "tiger" --authenticationDatabase "admin"

$ mongo admin -u root -p tiger

$ mongo mongodb://root:tiger@localhost:27017/admin
```

## Pymongo
```python
# -*- coding: utf-8 -*-

from pymongo import MongoClient
from urllib.parse import quote_plus
from django.conf import settings


class MongoService(object):

    def __init__(self, host="127.0.0.1", port="27017", user="", password="", database_name=""):

        uri = "mongodb://{}:{}@{}:{}/{}".format(quote_plus(user), quote_plus(password), host, port, "admin")
        client = MongoClient(uri)
        self.db = client[database_name]

    def get_collection(self, collection_name):

        self.conn = self.db[collection_name]
        return self.conn

mongo_service = MongoService(
    settings.MONGO_IP,
    settings.MONGO_PORT,
    settings.MONGO_USER,
    settings.MONGO_PASSWD,
    settings.MONGO_DB
)
```
