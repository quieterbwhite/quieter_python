package com.j2se.lesson9;

import java.lang.reflect.Field;

/**
 * 在外部修改一个对象的私有属性
 * Created by bwhite on 2017/10/7.
 */
public class TestPrivate2 {

    public static void main(String[] args) throws Exception {

        Private2 p = new Private2();

        Class<?> classType = p.getClass();

        Field field = classType.getDeclaredField("name");
        field.setAccessible(true);

        field.set(p, "lisi");

        System.out.println(p.getName());

    }
}
