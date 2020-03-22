# java SE Lesson 13

```
内部类

内部类共分为4种
```

```
静态内部类
只能访问外部类的静态成员变量与静态方法，生成静态内部类对象的方式为
OuterClass.InnerClass inner = new OuterClass.InnerClass();
lesson13
```

```
成员内部类
可以访问外部类的所有成员，非静态的可以访问一切
```

```
局部内部类
用得最少的一种内部类类型
定义在方法当中

只能访问方法中申明的 final 类型的变量
```

```
匿名内部类
用得很多

匿名内部类会隐式地继承或实现一个接口

String str = test.get(new Date(){})
定义了一个匿名内部类
该类继承了Date
并且没有重写Date中的任何内容

这里new， 并不是new Date, 而是 new 的 继承了Date的子类，最后方法传递的也是这个子类
```

```
String str = test.get(new Date(){
    public String toLocalString() {
        return "hello world";
    }
})
```