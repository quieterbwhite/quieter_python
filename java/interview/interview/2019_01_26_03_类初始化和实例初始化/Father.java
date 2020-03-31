package com.example.demo;

/**
 * 父类的初始化<clinit>
 *     1, j = method();
 *     2, 父类的静态代码块
 *
 * 父类的实例化方法
 * 1, super()(最前)
 * 2, i = test()
 * 3, 父类的非静态代码块
 * 4, 父类的无参构造(最后)
 *
 * 非静态方法前面其实有一个默认的this
 * this在构造器(或<init>)它表示的是正在创建的对象, 因为这里是在创建Son对象，
 * 所以test()执行的是子类重写的代码(面向对象的多态)
 *
 * 这里 i=test() 执行的是子类重写的test()方法
 *
 * Created by bwhite on 2019/1/26.
 */
public class Father {

    private int i = test();

    private static int j = method();

    // 静态代码块
    static {
        System.out.println("(1)");
    }

    // 构造器
    Father() {
        System.out.println("(2)");
    }

    // 非静态代码块
    {
        System.out.println("(3)");
    }

    public int test() {
        System.out.println("(4)");
        return 1;
    }

    public static int method() {
        System.out.println("(5)");
        return 1;
    }

}
