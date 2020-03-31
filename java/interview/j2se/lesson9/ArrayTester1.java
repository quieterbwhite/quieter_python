package com.j2se.lesson9;

import java.lang.reflect.Array;

/**
 * Array 类可以new 一个数组对象，数组本身也是对象，设置对象，取出对象
 * Created by bwhite on 2017/10/7.
 */
public class ArrayTester1 {

    public static void main(String[] args) throws Exception {

        Class<?> classType = Class.forName("java.lang.String");

        // 创建一个数组对象，第一个参数是数组内容的类型，第二个参数是数组长度
        Object array = Array.newInstance(classType, 10);

        Array.set(array, 5, "hello");

        String value = (String)Array.get(array, 5);

        System.out.println(value);

    }
}
