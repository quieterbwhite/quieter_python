package com.j2se.lesson9;

import java.lang.reflect.Constructor;

/**
 * Created by bwhite on 2017/10/7.
 */
public class ReflectTester {

    // 该方法实现对customer对象的拷贝操作
    public Object copy(Object object) throws Exception {

        // 新生成一个对象返回给调用端

        Class<?> classType = object.getClass();
        System.out.println(classType);

        // 不带参数的构造方法
        Constructor cons = classType.getConstructor(new Class[]{});
        Object obj = cons.newInstance(new Object[]{});

        // Constructor cons = classType.getConstructor(new Class[]{String.class, int.class});
        // Object obj = cons.newInstance(new Object[]{"hahh", 2});

        // 以上两行等价于下面一行
        Object obj2 = classType.newInstance();


        System.out.println(obj);

        return null;
    }

    public static void main(String[] args) throws Exception {
        ReflectTester test = new ReflectTester();

        test.copy(new Customer());
    }
}

class Customer {
    private Long id;

    private String name;

    private int age;

    public Customer() {

    }

    public Customer(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }
}
