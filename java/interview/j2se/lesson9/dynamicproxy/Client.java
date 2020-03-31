package com.j2se.lesson9.dynamicproxy;

import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Proxy;

/**
 * Created by bwhite on 2017/10/7.
 */
public class Client {

    public static void main(String[] args) {

        // 我没懂，这里命名都直接初始化了真实角色了
        RealSubject realSubject = new RealSubject();

        InvocationHandler handler = new DynamicSubject(realSubject);

        // 获取class对象
        Class<?> classType = handler.getClass();

        // 运行期间动态生成一个class类，然后生成class类的对象, 就是subject
        //　这个类实现了　realSubject.getClass().getInterfaces()　这些接口
        // 先生成类本身，再生成对象

        // 下面的代码一次性生成代理

        // 第一个参数 class loader，通过class对象获取class loader, 类装载器
        // 第二个参数 class 类型的数组，classType 所标识的类实现哪些接口, handler本身实现哪些接口，那么它也是
        // 最后一个参数 invocation handler 实例
        Subject subject = (Subject)Proxy.newProxyInstance(classType.getClassLoader(), realSubject.getClass().getInterfaces(), handler);

        subject.request();

        System.out.println(subject.getClass());





    }
}
