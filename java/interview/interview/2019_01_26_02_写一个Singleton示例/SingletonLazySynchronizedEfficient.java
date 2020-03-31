package com.example.demo;

/**
 * 懒汉式：
 *      延迟加载这个实例对象
 *
 * 1. 构造器私有化
 * 2. 用一个静态变量保存这个唯一的实例
 * 3. 提供一个静态方法，获取这个实例对象
 * 4. 增加同步锁，避免多线程问题
 * 5. 增加一个判断，提升效率
 * Created by bwhite on 2019/1/26.
 */
public class SingletonLazySynchronizedEfficient {

    private static SingletonLazySynchronizedEfficient singletonLazy;

    private SingletonLazySynchronizedEfficient(){}

    public static SingletonLazySynchronizedEfficient getSingletonLazy(){
        if(singletonLazy == null) {
            synchronized (SingletonLazySynchronizedEfficient.class) {
                if (singletonLazy == null) {
                    try {
                        Thread.sleep(100);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                    singletonLazy = new SingletonLazySynchronizedEfficient();
                }
            }
        }
        return singletonLazy;
    }
}
