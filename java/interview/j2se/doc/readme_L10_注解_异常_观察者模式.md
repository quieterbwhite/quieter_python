# java SE Lesson 10

```
注解:
    @Override

    @Deprecated
```

```
自定义注解
当注解中的属性名为value时，对其赋值时可以不指定属性的名称，而直接写上属性即可

除了value以外的其他值都需要使用 name = value 这种赋值方式。

public @interface AnnotationTest {
    // 就是这个value是个默认值
    String value();
}
```

```
使用@interface自定义Annotation时，实际上是自动继承了 java.lang.annotation.Annotation接口，
有编译程序自动完成了其他细节，
在定义Annotation时，不能继承其他的Annotation形态或接口。
```

```
告知编译程序如何处理 @Retention
0. .SOURCE
1. .CLASS 只是编译到字节码文件中
2. .RUNTIME 可以在运行期被反射获取到
```

```
@Documented

    将注解包含在Javadoc中

@Target
    java.lang.annotation.Target
    用于设定注解使用范围
    java.lang.annotation.ElementType
    Target通过ElementType来指定注解可使用范围的枚举集合

    取值	注解使用范围
    METHOD	可用于方法上
    TYPE	可用于类或者接口上

@Inherited 子类是否继承父类
默认子类不会继承父类的注解，可以用这个注解让其继承
```

```
异常

所谓自定义异常，通常就是定义了一个继承自Exception类的子类，
那么这个类就是一个自定义异常类。
通常情况下去我们会直接继承自Exception类，一般不会继承某个运行时的异常类。

异常没有细致的看。时间紧迫。能用就行了。别人应该不会问这部分内容吧。
```

```
观察者模式

观察者模式定义了一种一对多的依赖关系，让多个观察者对象同时监听某一个主题的对象。
这个主题对象在状态发生变化时，会通知所有观察者对象，让他们能够自己更新自己。

抽象主题角色
抽象观察者角色
具体主题角色
具体观察者角色

j2se/lesson10/observer/

jdk 内置了对观察者模式的支持
class 84, 用内置的观察者模式实现。lesson12
继承 Observable, Observer
```