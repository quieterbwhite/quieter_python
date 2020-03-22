# java SE Lesson 6

```
集合 Collection

Set
```

```
Object类，equals 方法的特点

自反性: x.equals(y) 应该返回 true
对称性: x.equals(y) 为true, 那么 y.equals(x)也为true
传递性: x.equals(y) == true, y.equals(z) == true, so, x.equals(z) == true.
一致性: x.equals(y) == true, 那么第n次调用也为true，前提条件没有修改x,y
对于非空引用x, x.equals(null) 返回 false
```

```
Object类的hashCode()方法的特点:

1. 在Java应用得一次执行过程中，一个对象的hashCode方法的多次调用他们应该返回同样的值，前提是该对象的信息没有发生变化
2. 对于两个对象，如果使用equals方法比较返回true，那么这两个对象的hashCode值一定是相同的
3. 两个对象，如果equals方法比较返回false，那么这两个对象的hashCode可以相同可以不同，但是如果不同则可以提供应用得性能
4. 对于Object类来说，他的不同对象的hashCode值是不同的，Object类的hashCode值表示的是对象的地址
```

```
当使用HasSet时，hashCode()方法就会得到调用，判断已经存储在集合中的对象的hash code值是否与增加的对象的hash code 值一致，
不一致：直接添加
一致：
    进行equals方法的比较:
        true: 表示对象已经加进去，就不会再增加新的对象
        false: 添加
```

```
一般重写 equals / hashcode 方法中的任一个都需要重写另一个
比如，一般ide的自动重写都是两个在一起的。
```

```
Map(映射): Map的keySet()方法会返回key的集合，因为map的键是不能重复的
因此keySet()方法的返回类型是Set;
而map的值是可以重复的，因此values()方法的返回类型是Collection,
可以容纳重复元素
```

```
策略模式

体现了两个基本的面向对象设计的原则
封装变化的概念
编程中使用接口，而不是对接口的实现

面向接口的编程

策略模式定义:
1. 定义一组算法，将每个算法都封装起来，并且使他们之间可以互换
2. 策略模式使这些算法在客户端调用他们的时候能够互不影响的变化

策略模式的组成：
1. 抽象策略角色，策略类，通常由一个接口或者抽象类实现
2. 具体策略角色，包装了相关算法或行为
3. 环境角色，持有一个策略类的引用，最终给客户端调用的

策略模式的编写步骤：
1. 对策略对象定义一个公共接口
2. 编写策略类，该类实现了上面的接口
3. 在使用策略对象的类中保存一个对策略对象的引用
4. 在使用策略对象的类中，实现对策略对象的set、get方法（注入）
或者使用构造方法完成赋值

code: j2se/lesson6/Strategy.py
```

```
工厂模式可以避免策略模式中策略过多带来的弊端
```