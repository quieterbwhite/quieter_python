package com.j2se.lesson14.decorator;

/**
 * 装饰角色
 * Created by bwhite on 2017/10/8.
 */
public class Decorator implements Component {

    private Component component;

    public Decorator(Component component) {
        this.component = component;
    }

    @Override
    public void doSomething() {
        component.doSomething();
    }
}
