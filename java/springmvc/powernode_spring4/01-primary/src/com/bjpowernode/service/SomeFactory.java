package com.bjpowernode.service;

/**
 *
 * Bean的装配 - 动态工厂Bean 例子。
 * 实际不会这样做
 *
 * 把工厂放到容器里面，用容器获取工厂，工厂再获取对象
 *
 * Created by bwhite on 18-4-14.
 * 问题： SomeServiceImpl类与工厂类耦合到了一起
 */
public class SomeFactory {

    // 动态工厂
    public ISomeService getSomeService() {
        return new SomeServiceImpl();
    }

    // 静态工厂
    // 是通过类名直接调用的，所以不是传统的在容器中配置的方式来生成对象
    public static ISomeService getSomeServiceStatic() {
        return new SomeServiceImpl();
    }
}
