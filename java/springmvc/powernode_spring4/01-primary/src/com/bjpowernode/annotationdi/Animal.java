package com.bjpowernode.annotationdi;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Scope;
import org.springframework.stereotype.Component;

import javax.annotation.PostConstruct;
import javax.annotation.PreDestroy;

/**
 * Created by bwhite on 18-4-18.
 *
 * @Component 注解，表明这个类是个组件, 容器创建的这个组件对象名称为 myStudent, 相当于 <bean></bean> 的id属性
 * 与本注解具有相同功能的注解还有三个
 * @Repository:    注解在 Dao 接口的实现类上，表示当前 Dao 类为组件
 * @Service:       注解在 Service 接口的实现类上，表示当前 Service 类为组件
 * @Controller:    注解在 Controller 类上，表示当前 Controller 类为组件
 */
//@Component("myAnimal")
@Scope("singleton")     // 设置 Bean 的作用范围[singleton, prototype]，默认是 singleton
public class Animal {

    @Value("李四")       // 为 name 属性赋值, @Value, 给的是普通属性的值
    private String name;

    private int age;

//    @Resource(name = "myHouse")   // byName 方式自动注入
//    @Resource  // byType 方式自动注入
    @Autowired  // byType 方式自动注入
//    @Qualifier("myHouse")   // byName 方式自动注入, 这个需要和 Autowired 一起使用
    private House house;

    @Override
    public String toString() {
        return "Animal{" +
                "name='" + name + '\'' +
                ", age=" + age +
                ", house=" + house +
                '}';
    }

    public House getHouse() {
        return house;
    }

    public void setHouse(House house) {
        this.house = house;
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

    // 初始化完毕之后
    @PostConstruct
    public void postInit() {
        System.out.println("初始化完毕之后");
    }

    // 销毁之前
    // singleton scope 才行, 容器要关闭, 才会有效果
    @PreDestroy
    public void preDestroy() {
        System.out.println("销毁之前");
    }

}
