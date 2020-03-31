package com.j2se.lesson14.decorator;

/**
 * 具体装饰角色
 * Created by bwhite on 2017/10/8.
 */
public class ConcreteDecorator2 extends Decorator {

    public ConcreteDecorator2(Component component) {
        super(component);
    }

    @Override
    public void doSomething() {
        super.doSomething();
        this.doAnotherThing();
    }

    public void doAnotherThing() {
        System.out.println("ConcreteDecorator2 - doAnotherThing");
    }
}
