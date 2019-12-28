# -*- coding=utf-8 -*-
# Created Time: 2016年01月28日 星期四 23时01分06秒
# File Name: 07_query_tricks.py

'''
django 中 使用ORM查询时，有用的函数
'''

'''
filter

exclude

values

values_list

dates

defer

only

len

list

none

extra

using

select_for_update

get

create

get_or_create

update_or_create

in_bulk

latest

earliest

first

last

range




'''


'''
** values

    values是返回QuerySet吗？严格说是ValuesQuerySet，是QuerySet的子集。看代码：
    Blog.objects.values()
    得出的是：
    [{'id': 1, 'name': 'Beatles Blog', 'tagline': 'All the latest Beatles news.'},...]
    没有指定参数，默认会返回全部的字段字典列表。指定参数：
    Blog.objects.values('id', 'name')
    得出：
    [{'id': 1, 'name': 'Beatles Blog'}]

** values_list

    上面 values 返回的是字典。

    而 values_list 返回的是元组。

    当 values_list 只需要一个字段时，可以这样写 values_list('name', flat=True), 返回的便是一个列表，如 ['bwhite', 'tiger']

    >>> Entry.objects.values_list('id').order_by('id')
    [(1,), (2,), (3,), ...]

    >>> Entry.objects.values_list('id', flat=True).order_by('id')
    [1, 2, 3, ...]
    如果传递的字段不止一个，使用 flat 就会导致错误。

** dates

    dates(field, kind, order=’ASC’)

    field 是你的 model 中的 DateField 字段名称。

    kind 是 “year”, “month” 或 “day” 之一。 每个 datetime.date对象都会根据所给的 type 进行截减。

    “year” 返回所有时间值中非重复的年分列表。
    “month” 返回所有时间值中非重复的年／月列表。
    “day” 返回所有时间值中非重复的年／月／日列表。
    order, 默认是 ‘ASC’，只有两个取值 ‘ASC’ 或 ‘DESC’。它决定结果如何排序。

    >>> Entry.objects.filter(headline__contains='Lennon').dates('pub_date', 'day')

    顾名思义，dates是和时间有关的函数，用法：
    Entry.objects.dates('pub_date', 'year')
    结果：
    [datetime.datetime(2005, 1, 1)，...]
    得出的是时间datetime列表，和values函数相似，得出的是QuerySet的子集：DateQuerySet；这个函数不好理解，如上面的Entry.objects.dates('pub_date', 'year')，是什么意思呢？
    其实就是取出所有博客的时间列表，参数‘year’，出来的时间列表 是以年份为依据，不会有重复年份,月份和日期默认是1；比如众多blog中，有几万条，发表时间当然不止同一年的，该语句出来 ：
    [datetime.datetime(2005, 1, 1)，datetime.datetime(2006, 1, 1)，datetime.datetime(2007, 1, 1)，datetime.datetime(2008, 1, 1)，...]
    嗯，时间列表，在template用，你应该知道了！

    参数 field kind order，形如：
    Entry.objects.dates('pub_date', 'day', order='DESC')
    field就是实体的一个时间字段，kid就是 year month day，order就是排序 desc asc，好理解吧？

    如果你还有疑问：我们想取出博客的所有月份，怎么写？ 呃，试试这样：
    Blog.objects.dates('pub_date', 'month', order='DESC')...
    结果：
    [datetime.datetime(2005, 1, 1)，datetime.datetime(2005, 2, 1)，... ，datetime.datetime(2006, 4, 1)，...，datetime.datetime(2008, 6, 1)，...]
    但如果想取所有日期列表呢？唉，有必要吗？dates用途，你平时见到的归档 都是按照年份或者月份归档的，如果按照日期归档，该网站的文摘更新速度不是一般的快哦！还是有办法的：
    Blog.objects.dates('pub_date', 'day', order='DESC')...

** defer

    defer是个好函数，有时候一个实体有过多的字段，取实体或者实体列表的时候，占用了多大的内存，而你却不需要取出全部的字段，
    比如博客的正文内容，你不需要立即检索数据库，这时defer就是你需要的东西。defer函数与前面讲的values有区别的，前者返回的是ValuesQuerySet，
    而defer返回的是QuerySet对象，这意味着，使用了defer后，你还可以结合QuerySet其他的函数，让整个语句结合更多的条件；Django的ORM除了做得OO，还很注重性能的。

    如果取博客的文章列表，让容量很大的正文和副标题在数据库层不进行检索，看看代码：
    Blog.objects.defer("content", "subtitle")

** only

    only很多程度上和defer是同一类的东西，可以理解为defer的相反函数吧。比如Person实体里有三个字段：name age birthday，下面这两条语句是等价的：

    Person.objects.defer("age", "biography")
    Person.objects.only("name")

** 统计每天的 注册量(比如):

query = C1.objects.filter(createTime__range=(start_date, end_date)).extra(select={'year': "EXTRACT(year FROM createtime)",
                                              'month': "EXTRACT(month from createtime)",
                                              'day': "EXTRACT(day from createtime)"}
                                      ).values('year', 'month', 'day').annotate(Count('id'))
SQL:
select count(id),
extract(year from createtime) as year,
extract(month from createtime) as month,
extract(day from createtime) as day
from table
group by year, month, day
;

结果:
[
    {'year': 2012L, 'id__count': 14, 'day': 17L, 'month': 5L},
    {'year': 2012L, 'id__count': 4, 'day': 18L, 'month': 5L},
    {'year': 2012L, 'id__count': 4, 'day': 22L, 'month': 5L}
]


** len

    len(). 调用 QuerySet 的 len() 方法，查询就会被运行。这正如你所料，会返回查询结果列表的长度。

    注意：如果你想得到集合中记录的数量，就不要使用 QuerySet 的 len() 方法。因为直接在数据库层面使用 SQL 的 SELECT COUNT(*) 会更加高效，Django 提供了 count() 方法就是这个原因。详情参阅下面的 count() 方法。


** list

    list(). 对 QuerySet 应用 list() 方法，就会运行查询。例如：

    entry_list = list(Entry.objects.all())
    要注意地是：使用这个方法会占用大量内存，因为 Django 将列表内容都载入到内存中。做为对比，遍历 QuerySet 是从数据库读取数据，仅在使用某个对象时才将其载入到内容中。


** none

    none()

    返回一个 EmptyQuerySet — 它是一个运行时只返回空列表的 QuerySet。它经常用在这种场合：你要返回一个空列表，但是调用者却需要接收一个 QuerySet 对象。（这时，就可以用它代替空列表）

    例如：

    >>> Entry.objects.none()
    []
    >>> from django.db.models.query import EmptyQuerySet
    >>> isinstance(Entry.objects.none(), EmptyQuerySet)
    True


** extra

extra(select=None, where=None, params=None, tables=None, order_by=None, select_params=None)

有些情况下，Django 的查询语法难以简练地表达复杂的 WHERE 子句。对于这种情况，Django 提供了 extra() QuerySet 修改机制，它能在QuerySet 生成的 SQL 从句中注入新子句。


** using

using(alias)

使用多个数据库时使用，参数是数据库的alias

# queries the database with the 'default' alias.
>>> Entry.objects.all()

# queries the database with the 'backup' alias
>>> Entry.objects.using('backup')


** select_for_update(nowait=False)

返回queryset，并将需要更新的行锁定，类似于SELECT … FOR UPDATE的操作。

entries = Entry.objects.select_for_update().filter(author=request.user)
所有匹配的entries都会被锁定直到此次事务结束。


** get(**kwargs)

返回与所给的筛选条件相匹配的对象，筛选条件在 字段筛选条件(Field lookups) 一节中有详细介绍。

在使用 get() 时，如果符合筛选条件的对象超过一个，就会抛出 MultipleObjectsReturned 异常。MultipleObjectsReturned 是 model 类的一个属性。

在使用 get() 时，如果没有找到符合筛选条件的对象，就会抛出 DoesNotExist 异常。这个异常也是 model 对象的一个属性。例如：

Entry.objects.get(id='foo') # raises Entry.DoesNotExist
DoesNotExist 异常继承自 django.core.exceptions.ObjectDoesNotExist，所以你可以直接截获 DoesNotExist 异常。例如：

from django.core.exceptions import ObjectDoesNotExist
try:
    e = Entry.objects.get(id=3)
    b = Blog.objects.get(id=1)
except ObjectDoesNotExist:
    print("Either the entry or blog doesn't exist.")


** create(**kwargs)

创建对象并同时保存对象的快捷方法：

p = Person.objects.create(first_name="Bruce", last_name="Springsteen")
和
p = Person(first_name="Bruce", last_name="Springsteen")
p.save(force_insert=True)
是相同的。


** get_or_create(defaults=None,**kwargs)

这是一个方便实际应用的方法，它根据所给的筛选条件查询对象，如果对象不存在就创建一个新对象。

它返回的是一个 (object, created) 元组，其中的 object 是所读取或是创建的对象，而 created 则是一个布尔值，它表示前面提到的 object 是否是新创建的。

这意味着它可以有效地减少代码，并且对编写数据导入脚本非常有用。例如：

try:
    obj = Person.objects.get(first_name='John', last_name='Lennon')
except Person.DoesNotExist:
    obj = Person(first_name='John', last_name='Lennon', birthday=date(1940, 10, 9))
    obj.save()
上面的代码会随着 model 中字段数量的激增而变得愈发庸肿。接下来用 get_or_create() 重写：

obj, created = Person.objects.get_or_create(first_name='John', last_name='Lennon',
                  defaults={'birthday': date(1940, 10, 9)})
在这里要注意 defaults 是一个字典，它仅适用于创建对象时为字段赋值，而并不适用于查找已存在的对象。 
get_or_create() 所接收的关键字参数都会在调用 get() 时被使用，有一个参数例外，就是 defaults。
在使用get_or_create() 时如果找到了对象，就会返回这个对象和 False。如果没有找到，就会实例化一个新对象，并将其保存；同时返回这个新对象和 True。


** update_or_create(defaults=None, **kwargs)

与上面类似

try:
    obj = Person.objects.get(first_name='John', last_name='Lennon')
    for key, value in updated_values.iteritems():
        setattr(obj, key, value)
    obj.save()
except Person.DoesNotExist:
    updated_values.update({'first_name': 'John', 'last_name': 'Lennon'})
    obj = Person(**updated_values)
    obj.save()
可以简写为：

obj, created = Person.objects.update_or_create(
    first_name='John', last_name='Lennon', defaults=updated_values)


** in_bulk(id_list)

接收一个主键值列表，然后根据每个主键值所其对应的对象，返回一个主键值与对象的映射字典。

>>> Blog.objects.in_bulk([1])
{1: <Blog: Beatles Blog>}
>>> Blog.objects.in_bulk([1, 2])
{1: <Blog: Beatles Blog>, 2: <Blog: Cheddar Talk>}
>>> Blog.objects.in_bulk([])
{}
如果你给 in_bulk() 传递的是一个空列表明，得到就是一个空字典。


** iterator()

运行查询(QuerySet)，然后根据结果返回一个 迭代器(iterator。 做为比较，使用 QuerySet 时，从数据库中读取所有记录后，一次性将所有记录实例化为对应的对象；而 iterator() 则是读取记录后，是分多次对数据实例化，用到哪个对象才实例化哪个对象。相对于一次性返回很多对象的 QuerySet，使用迭代器不仅效率更高，而且更节省内存。

要注意的是，如果将 iterator() 作用于 QuerySet，那就意味着会再一次运行查询，就是说会运行两次查询。


** latest(field_name=None)

根据时间字段 field_name 得到最新的对象。

下面这个例子根据 pub_date 字段得到数据表中最新的 Entry 对象：

Entry.objects.latest('pub_date')
如果你在 model 中 Meta 定义了 get_latest_by 项, 那么你可以略去 field_name 参数。Django 会将 get_latest_by 做为默认设置。

和 get(), latest() 一样，如果根据所给条件没有找到匹配的对象，就会抛出 DoesNotExist 异常。

注意 latest()和earliest() 是纯粹为了易用易读而存在的方法。


** first()

p = Article.objects.order_by('title', 'pub_date').first()
相当于：

try:
    p = Article.objects.order_by('title', 'pub_date')[0]
except IndexError:
    p = None
last()

类似于first()


** range

    包含的范围。

    例如：

    import datetime
    start_date = datetime.date(2005, 1, 1)
    end_date = datetime.date(2005, 3, 31)
    Entry.objects.filter(pub_date__range=(start_date, end_date))
    等价于 SQL：

    SELECT ... WHERE pub_date BETWEEN '2005-01-01' and '2005-03-31';
    你可以把 range 当成 SQL 中的 BETWEEN 来用，比如日期，数字，甚至是字符。

    year

    对日期／时间字段精确匹配年分，年分用四位数字表示。

    例如：

    Entry.objects.filter(pub_date__year=2005)
    等价于 SQL：

    SELECT ... WHERE EXTRACT('year' FROM pub_date) = '2005';
    (不同的数据库引擎中，翻译得到的 SQL 也不尽相同。)

    month

    对日期／时间字段精确匹配月分，用整数表示月分，比如 1 表示一月，12 表示十二月。

    day

    对日期／时间字段精确匹配日期。

    要注意的是，这个匹配只会得到所有 pub_date 字段内容是表示 某月的第三天 的记录，如一月三号，六月三号。而十月二十三号就不在此列。

    week_day

    对日期／时间字段匹配星期几

    例如：

    Entry.objects.filter(pub_date__week_day=2)
    等价于 SQL：

    SELECT ... WHERE EXTRACT('dow' FROM pub_date) = '2';
    (不同的数据库引擎中，翻译得到的 SQL 也不尽相同。)

    要注意的是，这段代码将得到 pub_date 字段是星期一的所有记录 (西方习惯于将星期一看做一周的第二天)，与它的年月信息无关。星期以星期天做为第一天，以星期六做为最后一天。

    hour

    minute

    second


'''
