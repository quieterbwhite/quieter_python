
# 北京动力节点 Spring4 视频教程

## 第一次学习 2016/12/3
```
练习项目 01
    包含项目构建

    基于 xml 的注解

    等
```

## 第二次学习这个视频 2018-4-14
```
    时间过去 一年多， 不会的还是不会，技术烂是有原因的。
    
    这个东西不用就忘记。所以，学习的时候记笔记，平时有时间就看看，复习，练习。就是这么简单。
    
    笔记要尽量详细，别以为自己记得住，当时确实能记住，一个星期后，他妈的，自己姓什么都能忘了。

    资料: 北京动力节点-Spring4讲义.pdf

    项目名: 01-primary
    
        Spring 第一个程序 - jar包的导入
        Spring 第一个程序 - 配置文件的创建
        Spring 第一个程序 - Bean的定义和注册
        Spring 第一个程序 - 不使用Spring容器的问题
        Spring 第一个程序 - 从Spring容器中获取Bean

            实际上可以从逻辑上认为这个文件就是一个容器
            注册Bean: 下面的注册, 相当于在代码中写的
            ISomeService someService = new SomeServiceImpl();
            默认是单例的, 也可以其他 prototype, request, session
            id就相当于容器为我们创建的对象的名字，标识。
            <bean id="someService" class="com.bjpowernode.service.SomeServiceImpl" />

        Spring 第一个程序 - 从文件系统加载Spring配置文件
        Spring 第一个程序 - 直接使用BeanFactory容器

        Spring 第一个程序 - ApplicationContext容器与BeanFactory容器的区别

            ApplicationContext 容器: 在初始化容器时, 就将容器中所有对象进行了创建  一开始创建全部对象,占用内存,效率高
            BeanFactory 容器, 使用时才创建  需要对象时才创建,节约内存,效率低 基本不用

        Bean的装配 - 默认装配方式

            代码通过 getBean()方式从容器获取指定的 Bean 实例,容器首先会调用 Bean 类的无参构造器,创建空值的实例对象。
            所以，在为一个类创建带参数的构造器时，一定要添加一个无参构造器，因为Spring会调用这个无参构造器。

        Bean的装配 - 动态工厂Bean

            把工厂放到容器里面，用容器获取工厂，工厂再获取对象
            动态工厂Bean将测试类与工厂的耦合问题解决了

            <!-- Bean的装配 - 动态工厂Bean 例子 -->
            <bean id="someFactory" class="com.bjpowernode.service.SomeFactory" />
            <!-- 在容器中指定用来创建最终对象的工厂，并指定工厂中创建该对象的方法. 就将工厂与最终代码分开 -->
            <!-- 表明someServiceByFactory对象是由someFactory这个工厂Bean的getSomeService()方法创建的 -->
            <bean id="someServiceByFactory" factory-bean="someFactory" factory-method="getSomeService" />

        Bean的装配 - 静态工厂Bean

            <!-- 静态工厂 -->
            <bean id="someServiceByFactoryStatic" class="com.bjpowernode.service.SomeFactory" factory-method="getSomeServiceStatic" />

            // 是通过类名直接调用的，所以不是传统的在容器中配置的方式来生成对象
            public static ISomeService getSomeServiceStatic() {
                return new SomeServiceImpl();
            }

        Bean的装配 - Bean的作用域

            默认是单例的, 通过scope变量来指定，可以是 prototype, request, session
            prototype: 原型模式, 使用时才由容器创建,每次使用时创建
            singleton: 单例模式(默认)，容器初始化时由容器创建

            <!-- 一样的class, 不一样的id, 容器会创建两个对象 -->
            <bean id="someService_another_object" class="com.bjpowernode.service.SomeServiceImpl" scope="singleton" />

        Bean的装配 - Bean后处理器

            <!-- 注册 bean 后处理器 容器初始化, bean 实例化 时 执行 -->
            <!-- 是继承的BeanPostProcessor,会被自动调用 -->
            <bean class="com.bjpowernode.service.MyBeanPostProcessor" />

        Bean的装配 - 定制Bean的生命周期(了解)

            bean 的生命周期有很多步骤,非常复杂,每个步骤我们都是可以插入代码来进行控制的,了解即可一共有 11 个步骤, 每个步骤都可以插入代码

            这两个参数对应接口的两个方法, 管理 bean 的生命周期
            值是类中定义的方法, 会在各个指定的阶段执行
            <!-- init-method="" destroy-method="" -->

            若要看到销毁方法的执行，需要两个条件:
            1. Bean 需要是 Singleton 的
            2. 手动关闭容器
                ((ClassPathXmlApplicationContext)ac).close()
```

## 基于 XML 的 DI
```
1. 设值注入

    <!-- 设值注入 -->
    <bean id="mySchool" class="com.bjpowernode.service.School">
        <property name="name" value="科成" />
    </bean>
    <bean id="student" class="com.bjpowernode.service.Student">
        <!-- 会调用Student类的 set() 方法 -->
        <property name="name" value="libobo" />
        <property name="age" value="22" />
        <property name="school" ref="mySchool" />
    </bean>

2. 构造注入

    <!-- 构造注入 -->
    <!-- 设值注入用得最多，构造注入基本不用 -->
    <bean id="teacher" class="com.bjpowernode.service.Teacher">
        <constructor-arg name="name" value="teacher li"/>
    </bean>

3. 命名空间注入(了解)

    p 命名空间设值注入
    c 命名空间构造注入

4. 为应用指定多个 Spring 配置文件

    平等关系的配置文件

    包含关系的配置文件
```

## 基于注解的DI
```java
/*
搭建环境 2018-04-18

1. 依赖包: spring-aop-4.3.4.RELEASE.jar

2. 添加 context 约束
*/

<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:context="http://www.springframework.org/schema/context" xsi:schemaLocation="
        http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
        http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context.xsd"> <!-- bean definitions here -->

<!-- 除了扫描指定的包，还会扫描子包 -->
<!-- com.bjpowernode.* 这种写法，只扫描子包，不扫描当前包:com.bjpowernode -->
<!-- com.bjpowernode 这种写法，先扫描当前包，没有再扫描子包 -->
<context:component-scan base-package="com.bjpowernode.annotationdi" />

//////////////////////////////////////////////////////////////////////////////

package com.bjpowernode.annotationdi;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Scope;
import org.springframework.stereotype.Component;

/**
 * Created by bwhite on 18-4-18.
 *
 * @Component 注解，表明这个类是个组件, 容器创建的这个组件对象名称为 myStudent, 相当于 <bean></bean> 的id属性
 * 与本注解具有相同功能的注解还有三个
 * @Repository:    注解在 Dao 接口的实现类上，表示当前 Dao 类为组件
 * @Service:       注解在 Service 接口的实现类上，表示当前 Service 类为组件
 * @Controller:    注解在 Controller 类上，表示当前 Controller 类为组件
 */
@Component("myAnimal")
@Scope("singleton")     // 设置 Bean 的作用范围[singleton, prototype]，默认是 singleton
public class Animal {

    @Value("李四")       // 为 name 属性赋值
    private String name;

    private int age;

    @Override
    public String toString() {
        return "Student{" +
                "name='" + name + '\'' +
                ", age=" + age +
                '}';
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        System.out.println("执行 setName()");
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    @Value("38")      // 可以将该注解放到 setter 上
    public void setAge(int age) {
        System.out.println("执行 setAge()");
        this.age = age;
    }

}

TODO, class 43
```