package com.j2se.lesson3;

import com.sun.xml.internal.bind.v2.runtime.unmarshaller.XsiNilLoader;

/**
 * 懒加载模式这里没有写。懒加载模式在多线程模式下可能会出问题的。
 * Created by bwhite on 2017/8/20.
 */
public class SingletonTest {

    public static void main(String[] args) {
        Singleton singleton = Singleton.getSingleton();
        Singleton singleton1 = Singleton.getSingleton();

        System.out.println(singleton == singleton1);
    }
}

class Singleton {

    private static Singleton singleton = new Singleton();

    private Singleton(){

    }

    public static Singleton getSingleton() {
        return singleton;
    }

}
