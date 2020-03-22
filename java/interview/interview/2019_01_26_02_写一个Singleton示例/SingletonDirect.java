package com.example.demo;

/**
 * 饿汉式: 直接创建对象，不存在线程安全问题
 *      直接实例化(简洁直观), 类初始化的时候就会创建，不管你是否需要这个对象
 *
 * 1. 构造器私有化
 * 2. 自行创建，并且用静态变量保存
 * 3. 向外提供这个实例
 * 4. 强调这是一个单例，我们可以用final修饰
 * Created by bwhite on 2019/1/26.
 */
public class SingletonDirect {

    public static final SingletonDirect INSTANCE = new SingletonDirect();

    private SingletonDirect(){}
}
