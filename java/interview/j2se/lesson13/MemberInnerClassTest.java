package com.j2se.lesson13;

import java.lang.reflect.Member;

/**
 * Created by bwhite on 2017/10/7.
 */
public class MemberInnerClassTest {

    public static void main(String[] args) {
        MemberInner.Inner2 inner = (new MemberInner()).new Inner2();

        inner.doSomething();
    }
}

class MemberInner {
    private int a = 4;

    public class Inner2 {
        private int a = 5;

        public void doSomething() {
            // 对外部类的引用
            System.out.println(MemberInner.this.a);

            // System.out.println(a);
        }
    }
}
