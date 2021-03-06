package com.example.demo;

/**
 * 赋值=, 最后计算
 * = 右边的从左到右加载值一次压入操作数栈
 * 实际先运算那个看运算符优先级
 * 自增，自减操作都是直接修改变量的值，不经过操作数栈
 * 最后的赋值之前，临时结果也是存储在操作数栈中
 * Created by bwhite on 2019/1/26.
 */
public class IntAddSelfMem {

    public static void main(String[] args) {
        int i = 1;

        // 等号右边的先算，赋值操作最后算
        // ++ 在后面要后算
        // 1. 把i的值压入操作数栈, 此时，操作数栈中的值为1
        // 2. i变量自增1, 局部变量表中的i, 1+1=2
        // 3. 赋值, 把操作数栈中的1，赋值给局部变量表中的i，2被覆盖，得到 i=1
        i = i++;

        // 1. 把 i=1 压栈，
        // 2. 局部变量表中 i+1 = 2
        // 3. 栈中的 1 赋值给 j = 1
        // 4. 此时 j=2, i=2
        int j = i++;

        // 从左至又压栈最后运算
        int k = i + ++i * i++;

        System.out.println("i=" + i);
        System.out.println("j=" + j);
        System.out.println("k=" + k);
    }
}
