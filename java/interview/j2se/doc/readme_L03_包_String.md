# java SE Lesson 3

```
接口中声明的方法都是抽象方法，接口中的方法都是public的。
```

```
接口中也可以定义成员变量。接口中的成员变量都是 public, static, final 的。
实际开发中基本不会在接口中定义成员变量。
接口主要起到一个约定的作用。
lesson3/InterfaceTest.java
```

```
一个类不能既是abstract 又是 final 的，因为abstract的主要目的是定义一种约定，让子类去实现这种约定，
而final又表示该类不能被继承，这样两者矛盾。
```

```
Design Pattern(设计模式)。单例模式，表示一个类只会生成唯一的一个对象。
lesson3/SingletonTest.java
```

```
包(package)。用于将完成不同功能的类分门别类，放在不同的目录(包)下。包的命名规则，将公司名反转作为包名。
```

```
访问修饰符(access modifier)
public      被 public 所修饰的属性和方法可以被所有类访问。
protected   被 protected 所修饰的属性和方法可以在类内部、相同包以及该类的子类所访问。
private     被 private 所修饰的属性和方法只能在该类内部使用
default     不加任何访问修饰符, 在类内部以及相同包下面的类所使用。
```

```
instance of

判断某个对象是否是某个类的实例。语法形式：引用名 instanceof 类名（接口名），返回一个 boolean 值。

People people = new Man();
System.out.println(people instance of People);
结果是 true
因为Man是People的子类，根据继承，子类就是父类，因此Man也可以看作是People的实例
```

```
相等性比较

对于原生数据类型来说，比较的是左右两边的值是否相等。
对于引用类型来说，比较左右两边的引用是否指向同一个对象，或者说左右两边的引用地址是否相同。
```

```
java.lang.Object 类。
java.lang 包在使用的时候无需显式导入，编译时由编译器自动帮助我们导入。
```

```
API （Application Programming Interface），应用编程接口。
```

```
当打印引用时，实际上会打印出引用所指对象的 toString()方法的返回值，
因为每个类都直接或间接地继承自 Object，而 Object 类中定义了 toString()，因此每个类都有toString()这个方法。
```

```
关于进制的表示：16 进制，逢 16 进一，16 进制的数字包括：0～9，A,B,C,D,E,F
```

```
equals()方法，该方法定义在 Object 类当中，因此 Java 中的每个类都具有该方法，
对于 Object 类的 equals()方法来说，它是判断调用 equals()方法的引用与传进来的引
用是否一致，即这两个引用是否指向的是同一个对象。对于 Object 类的 equals()方
法来说，它等价于==。
```

```
对于 String 类的 equals()方法来说，它是判断当前字符串与传进来的字符串的内容是否一致。
```

```
对于 String 对象的相等性判断来说，请使用 equals()方法，而不要使用==。
```

```
String 是常量，其对象一旦创建完毕就无法改变。当使用+拼接字符串时，会生成新的 String 对象，而不是向原有的 String 对象追加内容。
StringBuffer 是一个变量，创建完成之后内容可以修改，可以追加字符串，所以StringBuffer对象只有一个。不会频繁创建大量String对象。
```

```
String Pool（字符串池）
```

```
String s = “aaa”;（采用字面值方式赋值）

查找 String Pool 中是否存在“aaa”这个对象，如果不存在，则在 String Pool 中创建
一个“aaa”对象，然后将 String Pool 中的这个“aaa”对象的地址返回来，赋给引
用变量 s，这样 s 会指向 String Pool 中的这个“aaa”字符串对象

如果存在，则不创建任何对象，直接将 String Pool 中的这个“aaa”对象地址返回来，赋给 s 引用。
```

```
String s = new String(“aaa”);

首先在 String Pool 中查找有没有“aaa”这个字符串对象，如果有，则不在 String Pool
中再去创建“aaa”这个对象了，直接在堆中（heap）中创建一个“aaa”字符串对
象，然后将堆中的这个“aaa”对象的地址返回来，赋给 s 引用，导致 s 指向了堆中
创建的这个“aaa”字符串对象。

如果没有，则首先在 String Pool 中创建一个“aaa“对象，然后再在堆中（heap）创
建一个”aaa“对象，然后将堆中的这个”aaa“对象的地址返回来，赋给 s 引用，
导致 s 指向了堆中所创建的这个”aaa“对象。
```

