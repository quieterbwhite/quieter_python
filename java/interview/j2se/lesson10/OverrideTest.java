package com.j2se.lesson10;

/**
 * 注解 @Override
 * Created by bwhite on 2017/10/7.
 */
public class OverrideTest {

    @Override
    public String toString() {
        return "This is override test";
    }

    public static void main(String[] args) {
        OverrideTest test = new OverrideTest();
        System.out.println(test);
    }
}
