package com.j2se.lesson10.observer;

/**
 * 具体的观察者角色
 * Created by bwhite on 2017/10/7.
 */
public class ConcreteWatcher implements Watcher {

    @Override
    public void update(String str) {
        System.out.println("update " + str);
    }
}
