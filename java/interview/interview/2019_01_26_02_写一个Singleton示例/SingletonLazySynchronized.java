package com.example.demo;

/**
 * 懒汉式：
 *      延迟加载这个实例对象
 *
 * 1. 构造器私有化
 * 2. 用一个静态变量保存这个唯一的实例
 * 3. 提供一个静态方法，获取这个实例对象
 * 4. 增加同步锁，避免多线程问题
 * Created by bwhite on 2019/1/26.
 */
public class SingletonLazySynchronized {

    private static SingletonLazySynchronized singletonLazy;

    private SingletonLazySynchronized(){}

    public static SingletonLazySynchronized getSingletonLazy(){

        synchronized (SingletonLazySynchronized.class) {
            if (singletonLazy == null) {
                try {
                    Thread.sleep(100);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                singletonLazy = new SingletonLazySynchronized();
            }
        }
        return singletonLazy;
    }
}
