# -*- coding=utf-8 -*-
# Created Time: 2017年09月18日 星期一 14时58分30秒
# File Name: 01_basic.py

"""

数据库:

    查看当前数据库名称:  db

    查看所有数据库: show dbs

    切换数据库: use db_name

    删除当前指向的数据库: db.dropDatabase()

集合:

    创建集合:

        db.createCollection("animal")

    创建有上限的集合:

        capped: true, 表示设置上限

        size: 上限大小，会将之前的数据覆盖，单位为字节

        db.createCollection("animal", {capped : true, size : 10})

    查看当前所有集合:

        show collections;

    删除:

        db.animal.drop()

常用数据类型:

    ObjectID     文档ID

        12个字节的16进制数

        前4个字节为当前时间戳
        接下来3个字节为机器id
        接下来两个字节为mongodb的服务进程id
        最后3个字节是简单的增量值

    String       必须是有效的 utf-8

    Boolean

    Integer

    Double

    Arrays

    Object       嵌入式文档

    Null

    Timestamp

    Date

插入:

    db.animal.insert({name:'tiger', gender:1})

    foo = {_id:'20160101', name:'tiger'}
    foo.age = 12
    db.animal.insert(foo)

更新:

    db.animal.update({name:'tiger'}, {name:'dog'})

    db.animal.update({name:'tiger'}, {$set:{name:'dog'}}, {multi:true})

    改变数据类型:

        db.data.update({'name': 'zero'}, {'$set': {'value': NumberInt(0)}}, {"multi":true})

保存:

    db.animal.save(document)

删除:

    db.animal.remove({gender:0},{justOne:true})

    db.animal.remove({})

查询:

    db.animal.find()

    db.animal.findOne()

    db.animal.find().pretty()

    # 模糊查询，以xx开头的
    db.wsd201801.find({"data_flaw":/^<!DOC/})

    db.user.find({"name":/ab/})
    这样，可以查出所有包含有"ab"字符串的数据了。
    等同于select * from user where name like "ab"

    语句是：{"title":/F5\\(v/}
    我加双斜杠的原因是所查字段里面有括号，要转义一下。不然查不到。

    ---

    That would have to be:

        db.users.find({"name": /.*m.*/})

        or, similar:

        db.users.find({"name": /m/})

    ---

    db.users.insert({name: 'paulo'})
    db.users.insert({name: 'patric'})
    db.users.insert({name: 'pedro'})

    db.users.find({name: /a/})  //like '%a%'
    out: paulo, patric

    db.users.find({name: /^pa/}) //like 'pa%'
    out: paulo, patric

    db.users.find({name: /ro$/}) //like '%ro'
    out: pedro

    ---

    db.users.find({'name': {'$regex': 'sometext'}})

运算符:

    <    $lt
    <=   $lte

    >    $gt
    >=   $gte

    !=   $ne

    db.animal.find({age:{$gte:18}})

    查询年龄大于等于18，且性别为1的动物
    db.animal.find({age:{$gte:18}, {gender:1}})

    查询年龄大于等于18, 或性别为0的学生
    db.animal.find({$or:[{age:{$gt:18}}, {gender:0}]})

    查询年龄大于等于18, 或性别为0的学生, 并且名字为psky的
    db.animal.find({$or:[{age:{$gt:18}}, {gender:0}]}, {name:'psky'})

    范围:

        $in, $nin

        db.animal.find({age:{$in:[18, 28]}})

    正则表达式:

        //  |  $regex

        查询姓黄的学生

        db.animal.find({name:/^黄/})

        db.animal.find({name:{$regex:'^黄'}})

    自定义查询:

        使用$where后面写一个函数，返回满足条件的数据
        查询年龄大于20的学生

        db.animal.find({$where:function(){return this.age>20}})

limit:

    db.animal.find({}).limit(2)

skip:

    db.animal.find({}).skip(10)

    limit, skip 可以一起使用不分先后顺序

投影:

    定制返回的字段

    db.animal.find({},{_id:0, name:1, gender:1})

排序:

    1，  升序
    -1， 降序

    根据性别降序，再根据年龄升序
    db.animal.find().sort({gender:-1, age:1})

统计个数:

    方法 count() 用于统计结果集中文档条数

    db.animal.find({gender:1}).count()

    db.animal.count({age:{$gte:20}, gender:1})

去重:

    db.animal.distinct('gender', {age:{$gt:20}})


聚合 aggregate:

    aggregate 类似sql中的 sum(), avg() 等

    管道:
        $group, 将集合中的文档分组，可用于统计结果
        $match, 过滤数据，只输出符合条件的文档
        $project, 修改输入文档的结构，如重命名，增加，删除字段，创建计算结果
        $sort, 将输入文档排序后输出
        $limit, 限制聚合管道返回的文档数
        $skip, 跳过指定数量的文档，并返回余下的文档
        $unwind, 将数组类型的字段进行拆分

    表达式
        处理输入文档并输出

        $sum：计算总和，$sum:1同count表示计数
        $avg：计算平均值
        $min：获取最小值
        $max：获取最大值
        $push：在结果文档中插入值到一个数组中
        $first：根据资源文档的排序获取第一个文档数据
        $last：根据资源文档的排序获取最后一个文档数据

$group

    将集合中的文档分组，可用于统计结果
    _id表示分组的依据，使用某个字段的格式为'$字段'
    例1：统计男生、女生的总人数
    db.stu.aggregate([
        {$group:
            {
                _id:'$gender',
                counter:{$sum:'$age'}
            }
        }
    ])

    Group by null

        将集合中所有文档分为一组
        例2：求学生总人数、平均年龄
        db.stu.aggregate([
            {$group:
                {
                    _id:null,
                    counter:{$sum:1},
                    avgAge:{$avg:'$age'}
                }
            }
        ])

    透视数据

        例3：统计学生性别及学生姓名
        db.stu.aggregate([
            {$group:
                {
                    _id:'$gender',
                    name:{$push:'$name'}
                }
            }
        ])

        使用$$ROOT可以将文档内容加入到结果集的数组中，代码如下
        db.stu.aggregate([
            {$group:
                {
                    _id:'$gender',
                    name:{$push:'$$ROOT'}
                }
            }
        ])

$match

    用于过滤数据，只输出符合条件的文档
    使用MongoDB的标准查询操作

    例1：查询年龄大于20的学生
    db.stu.aggregate([
        {$match:{age:{$gt:20}}}
    ])

    例2：查询年龄大于20的男生、女生人数
    db.stu.aggregate([
        {$match:{age:{$gt:20}}},
        {$group:{_id:'$gender',counter:{$sum:1}}}
    ])

$project

    投影, 修改输入文档的结构，如重命名、增加、删除字段、创建计算结果

    例1：查询学生的姓名、年龄
    db.stu.aggregate([
        {$project:{_id:0,name:1,age:1}}
    ])

    例2：查询男生、女生人数，输出人数
    db.stu.aggregate([
        {$group:{_id:'$gender',counter:{$sum:1}}},
        {$project:{_id:0,counter:1}}
    ])

$sort

    将输入文档排序后输出

    例1：查询学生信息，按年龄升序
    b.stu.aggregate([{$sort:{age:1}}])

    例2：查询男生、女生人数，按人数降序
    db.stu.aggregate([
        {$group:{_id:'$gender',counter:{$sum:1}}},
        {$sort:{counter:-1}}
    ])

$limit

    限制聚合管道返回的文档数
    例1：查询2条学生信息
    db.stu.aggregate([{$limit:2}])

$skip

    跳过指定数量的文档，并返回余下的文档

    例2：查询从第3条开始的学生信息
    db.stu.aggregate([{$skip:2}])

    例3：统计男生、女生人数，按人数升序，取第二条数据
    db.stu.aggregate([
        {$group:{_id:'$gender',counter:{$sum:1}}},
        {$sort:{counter:1}},
        {$skip:1},
        {$limit:1}
    ])

    注意顺序：先写skip，再写limit

$unwind

    将文档中的某一个数组类型字段拆分成多条，每条包含数组中的一个值

    语法1

        对某字段值进行拆分
        db.集合名称.aggregate([{$unwind:'$字段名称'}])
        构造数据
        db.t2.insert({_id:1,item:'t-shirt',size:['S','M','L']})
        查询
        db.t2.aggregate([{$unwind:'$size'}])

    语法2

        对某字段值进行拆分
        处理空数组、非数组、无字段、null情况

        db.inventory.aggregate([{
            $unwind:{
                path:'$字段名称',
                preserveNullAndEmptyArrays:<boolean>#防止数据丢失
            }
        }])
        构造数据
        db.t3.insert([
        { "_id" : 1, "item" : "a", "size": [ "S", "M", "L"] },
        { "_id" : 2, "item" : "b", "size" : [ ] },
        { "_id" : 3, "item" : "c", "size": "M" },
        { "_id" : 4, "item" : "d" },
        { "_id" : 5, "item" : "e", "size" : null }
        ])

        使用语法1查询
        db.t3.aggregate([{$unwind:'$size'}])
        查看查询结果，发现对于空数组、无字段、null的文档，都被丢弃了

        问：如何能不丢弃呢？
        答：使用语法2查询
        db.t3.aggregate([{$unwind:{path:'$sizes',preserveNullAndEmptyArrays:true}}])

索引:

    造数据, 连上数据库直接执行语句即可
    for(i=0;i<100000;i++){db.t1.insert({name:'test'+i,age:i})}

    查找姓名为test10000
    db.t1.find(name:'test10000')

    使用explain命令进行查询性能分析
    db.t1.find(name:'test10000').explain('executionStats')
    其中executionStats下的executionTimeMillis表示整体查询时间，单位是毫秒

    创建索引
    1，表示升序，-1， 表示降序
    db.t1.ensureIndex({name:1})

    再次查询就能看到使用索引查询的效果

创建唯一索引

    建立唯一索引实现唯一约束功能

    db.t1.ensureIndex({name:1}, {unique:true})

联合索引

    对多个属性建立一个索引，按照 find() 的出现顺序

安全

    为了更安全的访问mongodb，需要访问者提供用户名和密码，于是需要在mongodb中创建用户
    采用了角色-用户-数据库的安全管理方式

    常用系统角色如下：
    root：只在admin数据库中可用，超级账号，超级权限
    Read：允许用户读取指定数据库
    readWrite：允许用户读写指定数据库

    创建超级管理用户
    use admin
    db.createUser({
        user:'admin',
        pwd:'123',
        roles:[{role:'root',db:'admin'}]
    })

启用安全认证

    修改配置文件
    sudo vi /etc/mongod.conf
    启用身份验证
    注意：keys and values之间一定要加空格, 否则解析会报错
    security:
    authorization: enabled

    重启服务
    sudo service mongod stop
    sudo service mongod start

    终端连接
    mongo -u 'admin' -p '123' --authenticationDatabase 'admin'

普通用户管理

    使用超级管理员登录，然后进入用户管理操作
    查看当前数据库的用户
    use test1
    show users

    创建普通用户
    db.createUser({
        user:'t1',
        pwd:'123',
        roles:[{role:'readWrite',db:'test1'}]
    })

    终端连接
    mongo -u t1 -p 123 --authenticationDatabase test1

    切换数据库，执行命令查看效果

    修改用户：可以修改pwd、roles属性
    db.updateUser('t1',{pwd:'456'})

复制，副本集

    什么是复制

        复制提供了数据的冗余备份，并在多个服务器上存储数据副本，提高了数据的可用性，并可以保证数据的安全性
        复制还允许从硬件故障和服务中断中恢复数据

    为什么要复制

        数据备份
        数据灾难恢复
        读写分离
        高（24* 7）数据可用性
        无宕机维护
        副本集对应用程序是透明

    复制的工作原理

        复制至少需要两个节点A、B...
        A是主节点，负责处理客户端请求
        其余的都是从节点，负责复制主节点上的数据
        节点常见的搭配方式为：一主一从、一主多从
        主节点记录在其上的所有操作，从节点定期轮询主节点获取这些操作，然后对自己的数据副本执行这些操作，从而保证从节点的数据与主节点一致
        主节点与从节点进行数据交互保障数据的一致性

    复制的特点

        N 个节点的集群
        任何节点可作为主节点
        所有写入操作都在主节点上
        自动故障转移
        自动恢复

    设置复制节点

        step1:创建数据库目录t1、t2
        mkdir t1
        mkdir t2

        step2:使用如下格式启动mongod，注意replSet的名称是一致的
        mongod --bind_ip 192.168.196.128 --port 27017 --dbpath ~/Desktop/t1 --replSet rs0
        mongod --bind_ip 192.168.196.128 --port 27018 --dbpath ~/Desktop/t2 --replSet rs0

        step3:连接主服务器，此处设置192.168.196.128:27017为主服务器
        mongo --host 192.168.196.128 --port 27017

        step4:初始化
        rs.initiate()

        step5:查看当前状态
        rs.status()

        step6:添加复本集
        rs.add('192.168.196.128:27018')

        step7:复本集添加成功后，当前状态
        rs.status()

        step8:连接第二个mongo服务
        mongo --host 192.168.196.128 --port 27018

        step9:向主服务器中插入数据
        use test1
        for(i=0;i<10;i++){db.t1.insert({_id:i})}
        db.t1.find()

        step10:在从服务器中插查询
        说明：如果在从服务器上进行读操作，需要设置rs.slaveOk()
        rs.slaveOk()
        db.t1.find()

    删除从节点

        rs.remove('192.168.196.128:27018')
        关闭主服务器后，再重新启动，会发现原来的从服务器变为了从服务器，新启动的服务器（原来的从服务器）变为了从服务器

备份

    语法
    mongodump -h dbhost -d dbname -o dbdirectory
    -h：服务器地址，也可以指定端口号
    -d：需要备份的数据库名称
    -o：备份的数据存放位置，此目录中存放着备份出来的数据

    例1
    sudo mkdir test1bak
    sudo mongodump -h 192.168.196.128:27017 -d test1 -o ~/Desktop/test1bak

恢复

    语法
    mongorestore -h dbhost -d dbname --dir dbdirectory
    -h：服务器地址
    -d：需要恢复的数据库实例
    --dir：备份数据所在位置

    例2
    mongorestore -h 192.168.196.128:27017 -d test2 --dir ~/Desktop/test1bak/test1
"""
