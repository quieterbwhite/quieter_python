package com.j2se.lesson13;

/**
 * 静态的只能访问静态的
 * 非静态的什么都可以访问
 *
 * Created by bwhite on 2017/10/7.
 */
public class StaticInnerClassTest {

    public static void main(String[] args) {

        StaticInner.Inner inner = new StaticInner.Inner();

        inner.test();
    }
}

class StaticInner {

    private static int a = 4;

    // 定义一个静态内部类
    public static class Inner {
        public void test() {
            System.out.println("a " + a);
        }
    }

}