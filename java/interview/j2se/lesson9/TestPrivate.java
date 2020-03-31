package com.j2se.lesson9;

import java.lang.reflect.Method;

/**
 * 在外部访问一个对象的私有方法
 * Created by bwhite on 2017/10/7.
 */
public class TestPrivate {

    public static void main(String[] args) throws Exception {

        Private p = new Private();

        Class<?> classType = p.getClass();
        Method method = classType.getDeclaredMethod("sayHello", new Class[]{String.class});
        method.setAccessible(true);// 压制java的访问控制检查

        String str = (String)method.invoke(p, new Object[]{"nidaye"});

        System.out.println(str);

    }
}
