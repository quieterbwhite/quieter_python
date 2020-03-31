package com.example.demo;

/**
 * 懒汉式：
 *      延迟加载这个实例对象
 *
 * 1. 构造器私有化
 * 2. 用一个静态变量保存这个唯一的实例
 * 3. 提供一个静态方法，获取这个实例对象
 * Created by bwhite on 2019/1/26.
 */
public class SingletonLazy {

    private static SingletonLazy singletonLazy;

    private SingletonLazy(){}

    public static SingletonLazy getSingletonLazy(){
        if (singletonLazy == null) {
            try {
                Thread.sleep(100);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            singletonLazy = new SingletonLazy();
        }
        return singletonLazy;
    }
}
