package com.j2se.lesson14.decorator;

/**
 * Created by bwhite on 2017/10/8.
 */
public class Client {

    public static void main(String[] args) {

        // 节点流
        Component component = new ConcreteComponent();

        // 过滤流
        Component component1 = new ConcreteDecorator1(component);

        // 过滤流
        Component component2 = new ConcreteDecorator2(component1);

        component2.doSomething();
    }
}
