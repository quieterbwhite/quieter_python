package com.j2se.lesson9.proxy;

/**
 * Created by bwhite on 2017/10/7.
 */
public class Client {

    public static void main(String[] args) {
        ProxySubject proxySubject = new ProxySubject();

        proxySubject.request();
    }
}
