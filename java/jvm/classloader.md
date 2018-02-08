# classloader

```
JVM 基本结构

类加载器, 执行引擎, 运行时数据区, 本地接口
```

```
.java ----> .class -> ClassLoader -> 运行时数据区 -> 执行引擎,本地库接口 -> 本地库方法
```

```
this.getClass.getClassLoader(); 
方法一得到的Classloader是静态的，表明类的载入者是谁

Thread.currentThread().getContextClassLoader();
方法二得到的Classloader是动态的，谁执行（某个线程），就是那个执行者的Classloader

对于单例模式的类，静态类等，载入一次后，这个实例会被很多程序（线程）调用，对于这些类，载入的Classloader和执行线程的Classloader通常都不同。
```
