# 介绍 django 中 F() 表达式
> Created Time: 2015年11月07日 星期六 02时04分50秒  

```
一个 F()对象代表了一个model的字段值或注释列。
使用它就可以直接参考model的field和执行数据库操作而不用再把它们（model field）查询出来放到python内存中。
相反，Django使用 F()对象生成一个描述数据库级操作要求的SQL 表达式。

from django.db.models import F

Instances of F() act as a reference to a model field within a query.
These references can then be used in query filters to compare the values of two different fields on the same model instance.

当Django遇到 F()实例，它覆盖了标准的Python运算符创建一个封装的SQL表达式。
在这个例子中，reporter.stories_filed就代表了一个指示数据库对该字段进行增量的命令。

为了获得用这种方法保存的新值，此对象应重新加载：

    reporter = Reporters.objects.get(pk=reporter.pk)

We can also use update() to increment the field value on multiple objects - 
which could be very much faster than pulling them all into Python from the database, 
looping over them, incrementing the field value of each one, and saving each one back to the database:

    Reporter.objects.all().update(stories_filed=F('stories_filed') + 1)

F() therefore can offer performance advantages by:
    getting the database, rather than Python, to do work
    reducing the number of queries some operations require

Avoiding race conditions using F()¶

Another useful benefit of F() is that having the database - rather than Python - update a field’s value avoids a race condition.
```

## 几个常用的情景
```
** 字段+1(加减乘除运算)

    例如我们有个统计点击量的字段，每次更新的操作其实就是把字段的值加1.
    一般我们的做法是把这条记录取出来，把相应字段加+1，然后在save，类似下面的代码：

    # Tintin filed a news story!
    reporter = Reporters.objects.get(name='Tintin')
    reporter.stories_filed += 1
    reporter.save()

    当我们使用了F()之后呢？ 只需要一行代码

    Reporters.objects.filter(name='Tintin').update(stories_filed=F('stories_filed') + 1)

    不仅代码量少了，而且这是直接在数据中操作，效率也变高了，特别是并发的情况，减少了多线程同时操作带来的隐患。 但是不支持字符串相加的操作。

** 字段比较

    例如一个合同有两个日期，一个叫做终止日期，一个叫做结束日期，现在要筛选出终止日期小于结束日期的合同。

    from django.db.models import F
    from contracts.models import Contracts
    contracts = Contracts.objects.filter(contract_stop_time__lt=F('end_time'))

    如果没有F对象，就没法直接使用rom来查询。
```
