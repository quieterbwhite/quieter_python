package com.j2se.lesson10;

import java.lang.annotation.ElementType;
import java.lang.annotation.Target;

/**
 * Created by bwhite on 2017/10/7.
 */
// 定义的这个注解只能用于修饰方法
@Target(ElementType.METHOD)
public @interface MyTarget {

   String value();
}
