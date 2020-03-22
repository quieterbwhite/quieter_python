package com.j2se.lesson9.dynamicproxy;

/**
 * Created by bwhite on 2017/10/7.
 */
public class RealSubject implements Subject {

    @Override
    public void request() {
        System.out.println("From real subject");
    }
}
