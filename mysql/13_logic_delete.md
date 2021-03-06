# 逻辑删除
> https://www.jianshu.com/p/f37281576585  

```
在互联网公司中数据的积累是非常重要的，所以就有了逻辑删除这样的设计。
所谓逻辑删除就是在表中加入类似is_deleted字段，将删除操作变成更新操作。
当is_deleted=1时就代表这条记录已经删除，这样做的好处非常明显，数据不会消失，
对于商业分析来说“被删除”的数据也非常有价值。

但事情往往不会这么简单，硬币的另一面是逻辑删除引入了一点点复杂度，
大部分读操作都需要过滤掉处于删除状态的记录，过滤操作要么在数据库层面完成，
要么在应用中完成，通常这样的复杂度是完全可以接受的，但是对于MySQL而言，
逻辑删除的设计还会导致常用的unique key失效，原因非常简单，已经删除的数据仍然存在，
所以在设计unique key的时候程序员不得不将is_deleted字段与应用要求unique的字段一起放入unique key中，
这样is_deleted=0的记录就不会与is_deleted=1的字段冲突了，这是符合逻辑的，is_deleted=0的记录之间会发生冲突，
但这正是unique key的本意，所以也是符合逻辑的，但是问题在于is_deleted=1的记录之间也会发生冲突，这可能就不符合逻辑了，为什么呢？
简单来说这样的设计在unique key存在的情况下不允许unique key字段相同的记录被删除两次以上，这对于应用来说是一个很大的限制。
```

## 解决问题
```
1. 不靠谱方案：放弃使用MySQL

2. 靠谱方案：增加delete_token字段

3. 推荐方案： 使用数据仓库

	所以还是让应用数据库与数据仓库发挥各自的功能吧，应用数据库与数据仓库都可以通过监听数据操作指令来自由的更新数据，
	至于删除操作，对于应用数据库来说就是物理删除，但对于数据仓库来说可以只是一条更新操作。
```
