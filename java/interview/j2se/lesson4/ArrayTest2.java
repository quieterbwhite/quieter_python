package com.j2se.lesson4;

/**
 *
 * null指，存在这个对象但不指向任何引用
 *
 * 数组里面存的是对象的应用，对象在堆里面，是没办法直接操作的。
 *
 *
 * Created by bwhite on 2017/8/20.
 * Updated by bwhite on 2017/10/03.
 */
public class ArrayTest2 {

    public static void main(String[] args) {

        // 仅生成了一个Person类型的数组
        Person[] p = new Person[3];

        p[0] = new Person(10);
        p[1] = new Person(20);
        p[2] = new Person(30);

        for (int i = 0; i < p.length; i++) {
            System.out.println(p[i].age);
        }
    }
}

class Person {

    int age;

    public Person(int age) {
        this.age = age;
    }
}
