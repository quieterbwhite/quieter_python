package com.j2se.lesson14.decorator;

/**
 * Created by bwhite on 2017/10/8.
 */
public class ConcreteDecorator1 extends Decorator {

    // 找不到父类的不带参数的构造方法
    public ConcreteDecorator1(Component component) {
        super(component);
    }

    @Override
    public void doSomething() {
        super.doSomething();

        this.doAnotherThing();
    }

    public void doAnotherThing() {
        System.out.println("ConcreteDecorator1 - doAnotherThing");
    }
}
