# java SE Lesson 5

```
集合 Collection
```

```
list基本操作
j2se/lesson5/ArrayListTest1.java

放到list中的变量类型在取出来的时候一定记得转换到合适的类型
j2se/lesson5/ArrayListTest2.java
```

```
集合里面只能放置对象

ArrayList list = new ArrayList();
// list.add(3) // 这一句是错误的，不能够直接添加原生数据类型, 包装类型也就有出现理由了
```

```
从集合中取出数据进行想要的操作
j2se/lesson5/ArrayListTest3.java
```

```
不能将 Object[] 转换成 Integer[]
// error
// Integer[] in = (Integer[])list.toArray();
因为add到列表中时是对象，包含各种数据类型，取出来的时候是Object, 就不能直接转换为Integer。
需要使用强制类型转换，转换为放置进去的类型。
```

```
集合中存放的依然是对象的引用而不是对象本身。

ArrayList 底层就是一个Object类型数组。当使用不带参数的构造方法生成ArrayList对象时，实际上
会在底层生成一个长度为10的Object类型数组。

如果增加的元素超过10个，那么ArrayList底层会新生成一个数组，长度为原数组的1.5倍+1,
然后将原数组的内容复制到新数组当中，并且后续增加的内容都会放到新数组中。
当新数组装下增加的元素时，重复该过程。
```

```
对于ArrayList元素的删除操作，需要将被删除元素的后续元素向前移动，代价比较高。
```

```
一般将数据结构分为两大类，线性数据结构和非线性数据结构。
线性数据结构：线性表，栈，队列，串，文件
非线性数据结构：树和图
```

```
线性表，按其存储结构可分为顺序表和链表。
用顺序存储结构存储的线性表称为顺序表
用链式存储结构存储的线性表称为链表

将线性表中的元素依次存放在某个存储区域中，所形成的表称为顺序表。一维数组就是用顺序方式存储的线性表。
```

```
链表

j2se/lesson5/Node.java

public class Node {

    String data; //存放节点数据本身
    Node node;   //存放指向下一个节点的引用

}

单向链表
单向循环链表
双向链表
双向循环链表

前驱
后继

LinkedList list = new LinkedList();
list.add("add");
实际添加到list中的是 由字符串构造的Entry对象，包含数据本身，前驱，后继
Entry {
    Entry previous;
    Object element;
    Entry next;
}
Entry entry = new Entry();
entry.element = "aaa";
list.add(entry);
```

```
ArrayList底层采用数组实现，LinkedList底层采用双向链表实现。

当执行插入或者删除操作时，采用LinkedList比较好。
当执行搜索操作时，采用ArrayList比较好。
```

```
当向ArrayList添加一个对象时，实际就是将该对象放置到了ArrayList底层所维护的
数组当中；
当向LinkedList中添加一个对象时，实际上LinkedList内部会生成一个
Entry对象。
```



