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
