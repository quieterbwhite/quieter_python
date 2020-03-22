package com.j2se.lesson8;

import java.lang.reflect.Method;

/**
 * Created by bwhite on 2017/10/6.
 */
public class DumpMethods {

    public static void main(String[] args) throws Exception {

        // 获得了字符串所标识的类的class对象
        Class<?> classType = Class.forName("java.lang.String");

        Method[] methods = classType.getDeclaredMethods();

        for (Method method : methods) {
            System.out.println(method);
        }

    }
}
