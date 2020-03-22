package com.j2se.lesson9.proxy;

/**
 * 相当于房东
 * Created by bwhite on 2017/10/7.
 */
public class RealSubject extends Subject {

    @Override
    public void request() {
        System.out.println("From real subject");
    }
}
