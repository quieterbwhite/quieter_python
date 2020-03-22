package com.j2se.lesson4;

/**
 * class 31
 * Created by bwhite on 2017/8/20.
 */
public class IntegerTest {

    public static void main(String[] args) {

        // 原生数据类型
        int a = 10;

        // 引用类型, 与上一个不同，概念都发生变化了
        // 位于 java.lang 包，不需要导入，直接用
        // 将整数a 转换成了它的包装类的对象，就可以方便的使用包装类里面的关于整型的很多方法
        Integer integer = new Integer(a);

        // 取值，返回包装的值
        int b = integer.intValue();

        // output: true
        System.out.println(a == b);
    }
}
