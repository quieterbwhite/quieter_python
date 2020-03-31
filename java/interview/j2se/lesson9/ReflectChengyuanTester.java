package com.j2se.lesson9;

import java.lang.reflect.Constructor;
import java.lang.reflect.Field;
import java.lang.reflect.Method;

/**
 * Created by bwhite on 2017/10/7.
 */
public class ReflectChengyuanTester {

    // 该方法实现对customer对象的拷贝操作 object -> objectCopy
    public Object copy(Object object) throws Exception {

        Class<?> classType = object.getClass();

        // 用类的不带参数的构造方法创建一个对象,该对象的属性没有值，后面的代码会设置
        Object objectCopy = classType.getConstructor(new Class[]{}).newInstance(new Object[]{});

        // 获得对象的所有成员变量
        Field[] fields = classType.getDeclaredFields();

        for (Field field : fields) {
            System.out.println(field.getName());
            String name = field.getName();

            // 获取首字母并转大写，用于后面字符串构造
            String firstLetter = name.substring(0, 1).toUpperCase();

            // substring(1), 实际是 substring(1, name.length) 的缩写，表示取1到最后
            String getMethodName = "get" + firstLetter + name.substring(1);
            String setMethodName = "set" + firstLetter + name.substring(1);

            System.out.println(getMethodName + " : " + setMethodName);

            Method getMethod = classType.getMethod(getMethodName, new Class[]{});
            Method setMethod = classType.getMethod(setMethodName, new Class[]{field.getType()});

            // 调用 object 的 getMethod 方法
            Object value = getMethod.invoke(object, new Object[]{});

            // 参数 objectCopy 是指要返回的对象, 调用该对象的set方法为其设置一个值
            setMethod.invoke(objectCopy, new Object[]{value});

        }

        return objectCopy;
    }

    public static void main(String[] args) throws Exception {

        Student student = new Student("andy", 20);
        student.setId(1L);

        ReflectChengyuanTester test = new ReflectChengyuanTester();

        Student student1 = (Student)test.copy(student);

        System.out.println(student1.getId() + ", " + student1.getName() + ", " + student1.getAge());
    }
}

class Student {
    private Long id;

    private String name;

    private int age;

    public Student() {

    }

    public Student(String name, int age) {
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
