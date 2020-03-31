package com.example.demo;

/**
 * 饿汉式: 直接创建对象，不存在线程安全问题
 *      枚举式(最简洁)
 *
 * 枚举类型，表示该类型的对象是有限的几个
 * 我们可以限定成一个，就成了单例
 * Created by bwhite on 2019/1/26.
 */
public enum SingletonEnum {
    INSTANCE
}
