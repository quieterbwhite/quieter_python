# MongoDB 小课堂

## ObjectId
```
http://www.runoob.com/mongodb/mongodb-objectid.html

bjectId("52cbab70231dea1e819b2a39")

    52cbab70      时间戳
    231dea        机器号
    1e81          进程ID
    9b2a39        自增数

1.24个16进制数据，使用 12字节的存储空间。

2.最后3个字节为：自动增长。可确保每秒生成的值也不一样，一秒最多允许每个进程拥有256^3个不同ObjectId

from bson.objectid import ObjectId

# str -> ObjectId
ObjectId(post_id_as_str)

# ObjectId -> str
post_id_as_str = str(post_id)
```
