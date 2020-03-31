package com.j2se.lesson10;

/**
 * Created by bwhite on 2017/10/7.
 */
@MyAnnotation(hello="ni", world = "shi")
public class MyTest {

    @MyAnnotation(hello="a", world = "b")
    @Deprecated
    @SuppressWarnings("unchecked")
    public void output() {
        System.out.println("output");
    }
}
