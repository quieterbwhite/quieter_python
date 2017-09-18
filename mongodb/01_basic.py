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

保存:

    db.animal.save(document)

删除:

    db.animal.remove({gender:0},{justOne:true})

    db.animal.remove({})

查询:

    db.animal.find()

    db.animal.findOne()

    db.animal.find().pretty()

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


高级+++++++++++++++++++++++++++++++++++++++++++++++

聚合 aggregate:

    aggregate 类似sql中的 sum(), avg() 等

    管道:

        $group, 将集合中的文档分组，可用于统计结果
        $match, 过滤数据，只输出符合条件的文档
        $project, 修改输入文档的结构，如重命名，





"""
