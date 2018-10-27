# 黑马Python Redis 课程笔记

## 安装
```
下载：打开redis官方网站，推荐下载稳定版本(stable)

    https://redis.io/

解压

    tar zxvf redis-3.2.5.tar.gz

复制：推荐放到usr/local目录下

    sudo mv -r redis-3.2.3/* /usr/local/redis/

进入redis目录

    cd /usr/local/redis/

生成

    sudo make

测试

    sudo make test

这段运行时间会较长

安装：将redis的命令安装到/usr/bin/目录

    sudo make install

或者 apt-get 安装:

    http://www.runoob.com/redis/redis-install.html

    $sudo apt-get install redis-server
```

## 运行
```
启动服务器：

    redis-server

按ctrl+c停止

启动客户端：在新终端中运行如下代码

    redis-cli

运行命令

    ping

    set 'a' '123'

当添加键值后，发现在当前运行的目录下，创建了一个文件：dump.rdb，这个文件用于将数据持久化存储
```

## 基本配置
```
在源文件/usr/local/redis目录下，文件redis.conf为配置文件

绑定地址：如果需要远程访问，可将此行注释

    bind 127.0.0.1

端口，默认为6379

    port 6379

是否以守护进程运行

    如果以守护进程运行，则不会在命令行阻塞，类似于服务
    如果以非守护进程运行，则当前终端被阻塞，无法使用
    推荐改为yes，以守护进程运行

    daemonize no|yes

数据文件

    dbfilename dump.rdb

数据文件存储路径

    dir的默认值为./，表示当前目录

    推荐改为：dir /var/lib/redis

使用配置文件方式启动

    直接运行redis-server会直接运行，阻塞当前终端

    一般配置文件都放在/etc/目录下

    sudo cp /usr/local/redis/redis.conf /etc/redis/

推荐指定配置文件启动

    sudo redis-server /etc/redis/redis.conf

停止redis服务

    ps aux | grep redis

    sudo kill -9 redis的进程id

    或者 systemctl stop redis

密码相关:

    http://github.tiankonguse.com/doc/redis/connection/auth.html

    https://itbilu.com/database/redis/Ey_r7mWR.html

    可以通过配置文件修改密码

        /etc/redis/redis.conf

        line: 396   requirepass

    或者直接使用命令修改

        redis> CONFIG SET requirepass secret_password   # 密码: secret_password
```

##数据操作
```
redis是key-value的数据，所以每个数据都是一个键值对

键的类型是字符串

值的类型分为五种：

    字符串string

    哈希hash

    列表list

    集合set

    有序集合zset

数据操作的全部命令，可以查看中文网站 http://redis.cn/commands.html

清除所有库所有key数据: flushall

清除单个库所有key数据: flushdb - Redis Flushdb 命令用于清空当前数据库中的所有 key

查看数据量: dbsize
```

## string
```
设置键值

    set key value

设置键值及过期时间，以秒为单位

    SETEX key seconds value

设置多个键值

    MSET key value [key value ...]

根据键获取值，如果不存在此键则返回nil

    GET key

根据多个键获取多个值

    MGET key [key ...]

要求：值是数字

    将key对应的value加1

    INCR key

将key对应的value加整数

    INCRBY key increment

将key对应的value减1

    DECR key

将key对应的value减整数

    DECRBY key decrement

追加值

    APPEND key value

获取值长度

    STRLEN key

键的命令

查找键，参数支持正则 KEYS pattern

判断键是否存在，如果存在返回1，不存在返回0

    EXISTS key [key ...]

查看键对应的value的类型

    TYPE key

删除键及对应的值

    DEL key [key ...]

设置过期时间，以秒为单位

    创建时没有设置过期时间则一直存在，直到使用使用DEL移除

    EXPIRE key seconds

查看有效时间，以秒为单位

    TTL key
```

## hash
```
hash用于存储对象，对象的格式为键值对

设置单个属性

    HSET key field value

设置多个属性

    HMSET key field value [field value ...]

获取一个属性的值

    HGET key field

获取多个属性的值

    HMGET key field [field ...]

获取所有属性和值

    HGETALL key

获取所有的属性

    HKEYS key

返回包含属性的个数

    HLEN key

获取所有值

    HVALS key

判断属性是否存在

    HEXISTS key field

删除属性及值

    HDEL key field [field ...]

返回值的字符串长度

    HSTRLEN key field

HASH 类型不能像 STRING 一样直接设置过期时间，但是redis有另外一个单独的方法

    可以为任意数据设置过期时间
```

## 发布订阅
```
todo
```
