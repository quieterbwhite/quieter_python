# java SE Lesson 7

```
HashSet 底层是使用 HashMap 实现的。
当使用add()方法将对象添加到Set当中时，实际上是将该对象作为底层
所维护的Map对象的key,而value则都是同一个Object对象，该对象是个常量，占位用
```

```
HashMap底层是使用数组实现的，我们想HashMap中放置的对象实际上是存储在该数组中的。
数组中是一个个Entry对象，当放置元素到数组中时，如果hash碰撞，那么
最新的Entry,放置到数组中，旧的Entry通过其next指向它。
```

```
当向HashMap中put一个键值对时，它会根据key的hashCode值计算出一个位置，
该位置就是此对象准备往数组中存放的位置。

如果该位置没有对象存在，就将此对象直接放进数组中。
如果该位置已经有对象存在了，则顺着此存在的对象的链开始寻找（Entry类有一个Entry类型的next成员变量，指向该对象的下一个对象），如果此链上有对象的话，
再去使用equals方法比较，如果对此链上的某个对象的equals方法比较为false，
则将该对象放到数组中，然后将数组中该位置以前存在的那个对象链接到此对象的后面。
```

```
泛型

所谓泛型，就是变量类型的参数化

j2se/lesson7/GenericFoo.java
j2se/lesson7/Generic.java
j2se/lesson7/Generic2.java
j2se/lesson7/SimpleCollection.java

这里没有笔记，一切都在 lesson7 的代码中

当没有指定泛型继承的类型或接口时，默认使用 T extends Object,
所以默认情况下任何类型都可以作为参数传入
```