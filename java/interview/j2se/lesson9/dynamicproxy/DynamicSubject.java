package com.j2se.lesson9.dynamicproxy;

import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;

/**
 * 该代理类的内部属性是Object类型，实际使用的时候通过该类的构造方法传递进来一个对象
 * 此外，该类还实现了invoke方法，该方法中的method.invoke其实就是调用被代理对象的将要
 * 执行的方法，方法参数是sub，表示该方法从属sub，通过动态代理类，我们可以在执行真实对象的方法前后
 * 加入自己的一些额外方法
 *
 *
 * 要想实现动态代理类必须实现 DynamicHandler
 * Created by bwhite on 2017/10/7.
 */
public class DynamicSubject implements InvocationHandler {

    // 可以代理任何真实角色
    private Object sub;

    // new 这个类的实例时，传入真实角色
    public DynamicSubject(Object obj) {
        this.sub = obj;
    }

    @Override
    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {

        System.out.println("before calling: " + method);

        method.invoke(sub, args);

        System.out.println("after calling: " + method);

        return null;
    }
}
