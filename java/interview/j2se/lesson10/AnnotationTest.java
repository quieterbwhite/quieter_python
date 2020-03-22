package com.j2se.lesson10;

/**
 * Created by bwhite on 2017/10/7.
 */
public @interface AnnotationTest {

    String value() default "hello";

    EnumTest value2();
}

enum EnumTest {
    Hello, World, Welcome;
}
