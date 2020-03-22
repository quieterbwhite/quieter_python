package com.j2se.lesson9;

import java.lang.reflect.Array;

/**
 * Created by bwhite on 2017/10/7.
 */
public class ArrayTester2 {

    public static void main(String[] args) {

        int[] dims = new int[]{1, 3, 5};

        // 创建的是dims代表的三维数组
        Object array = Array.newInstance(Integer.TYPE, dims);

        Object arrayObj = Array.get(array, 3);

        Class<?> classType = arrayObj.getClass().getComponentType();




        System.out.println(Integer.TYPE);
        System.out.println(Integer.class);
        /*
            int
            class java.lang.Integer
         */





    }
}
