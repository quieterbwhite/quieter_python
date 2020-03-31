package com.j2se.lesson9.proxy;

/**
 * Created by bwhite on 2017/10/7.
 */
public class ProxySubject extends Subject {

    private RealSubject realSubject;// 代理角色内部引用了真实角色

    @Override
    public void request() {

        this.preRequest();  // 在真实角色操作之前

        if (null == realSubject) {
            realSubject = new RealSubject();
        }

        realSubject.request(); // 真实角色完成事情

        this.postRequest(); // 在真实角色操作之后
    }

    // 代理角色自己的方法，如收中介费。就像python中的装饰器一样
    private void preRequest() {
        System.out.println("pre request");
    }

    private void postRequest() {
        System.out.println("post request");
    }
}
