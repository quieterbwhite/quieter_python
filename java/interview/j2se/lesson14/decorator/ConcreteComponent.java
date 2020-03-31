package com.j2se.lesson14.decorator;

/**
 * 具体构建角色
 * Created by bwhite on 2017/10/8.
 */
public class ConcreteComponent implements Component {

    @Override
    public void doSomething() {

        // 具体的功能，比如读写文件
        System.out.println("ConcreteComponent - doSomething");
    }
}
