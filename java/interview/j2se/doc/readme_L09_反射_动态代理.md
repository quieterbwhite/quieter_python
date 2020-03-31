# java SE Lesson 9

```
class 对象是在没有生成任何对象之前，jvm生成好的。
通过class对象就能获得该类的所有信息。
class 对象是java里面非常重要的对象。
```

```
获取某个类或某个对象所对应的Class对象的常用的三种方式：
1. 使用Class类的静态方法 forName, Class.forName("java.lang.String");
2. 使用类的 .class 方法 String.class;
3. 使用对象的 getClass() 方法, String s = "aa"; Class<?> class = s.getClass();
```

```
若想通过类的不带参数的构造方法来生成对象，有两种方式：
    先获得Class对象，然后通过Class对象的newInstance()方法直接生成即可
    Class<?> classType = String.class;
    Object obj = classType.newInstance();

    先获得Class对象，然后通过该对象获得对应的Constructor对象，
    再通过该Constructor对象的newInstance()方法生成
    Class<?> classType = object.getClass();
    Constructor cons = classType.getConstructor(new Class[]{String.class, int.class});
    Object obj = cons.newInstance(new Object[]{"hahh", 2});

若想通过类的带参数的构造方法生成对象，只能使用下面一种方式：
    Class<?> classType = object.getClass();
    Constructor cons = classType.getConstructor(new Class[]{String.class, int.class});
    Object obj = cons.newInstance(new Object[]{"hahh", 2});
```

```
Integer.TYPE 返回 int
Integer.class 返回的是 Integer 类所对应的对象 class java.lang.Integer
```

```
利用反射修改对象的私有属性，调用对象的私有方法，构造对象等
```

```
众所周知Java有个Object class，是所有java classes的继承根源，
其内申明了数个应该在所有Java class中被改写的methods：
hashCode(), equals(), clone(), toString(), getClass()等。
其中getClass()返回一个Class object。
```

```
代理模式的作用是，为其他对象提供一种代理以控制对这个对象的访问。

在某些情况下客户不想或不能直接引用一个对象，而代理对象可以在客户端和
目标对象之间起到中介的作用
```

```
代理模式一般涉及到的角色有：
抽象角色，申明真实对象和代理对象的共同接口

代理角色，代理对象角色内部含有对真实对象的引用，从而可以操作真实对象，
同时代理对象提供与真实对象相同的接口以便在任何时候都能代替真实对象。
同时，代理对象可以在执行真实对象操作时，附加其他的操作，相当与对真实对象进行封装

真实角色，代理角色所代表的真实对象，是我们最终要引用的对象
```

```
如果按照上述静态代理模式，那么真实角色必须是事先已存在的，并将其作为代理对象的内部属性。但实际使用时，一个真不是角色必须对应一个代理角色，如果大量使用会导致类很多。

此外，如果事先不知道真实角色呢？这个问题可以通过Java的动态代理来解决。

比如，spring等框架有很多xml配置文件，就是通过反射，代理动态加载生成对象
```

```
在使用动态代理类时，我们必须实现InvocationHandler接口
Subject.java
RealSubject.java
DynamicSubject.java
Client.java
```

```
动态代理类相对于静态代理类

以前是一个搬砖对应一个代理，一个和泥对应一个代理

现在搬砖和和泥的都对应同一个代理

不就是python的装饰器，定义一次，到处装饰

Spring 框架大量运用动态代理，动态代理懂了，spring也就懂了大半
Spring 还用到了更高级的动态字节码生成等技术
```

```
所谓 Dynamic Proxy 是这样一种 class：
它是在运行时生成的class，在生成它时你必须提供一组interface给它，
然后该class就宣称它实现了这些interface。
你当然可以把该class的实例当做这些interface中的任何一个来用。
当然，这个 Dynamic Proxy 其实就是一个proxy, 它不会替你做实质性的工作，
在生成它的实例时你必须提供一个handler，由它接管实际的工作。
```

```
动态代理创建步骤:

1. 创建一个实现接口InvocationHandler的类，它必须实现invoke方法
2. 创建被代理的类以及接口
3. 通过proxy的静态方法 newProxyInstance(ClassLoader loader, Class[] interfaces, InvocationHandler h)创建一个代理
4. 通过代理调用方法
```