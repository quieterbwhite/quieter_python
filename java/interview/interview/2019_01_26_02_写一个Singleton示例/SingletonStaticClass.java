package com.example.demo;

/**
 * 在内部类被加载和初始化时，才创建INSTANCE实例对象
 * 静态内部类不会随着外部类的加载和初始化而初始化，它是要单独加载和初始化的
 * 内部类加载和初始化的。是类加载器完成的。是线程安全的。
 * Created by bwhite on 2019/1/26.
 */
public class SingletonStaticClass {

    private SingletonStaticClass(){}

    private static class Inner {
        private static final SingletonStaticClass INSTANCE = new SingletonStaticClass();
    }

    public static SingletonStaticClass getInstance() {
        return Inner.INSTANCE;
    }
}
