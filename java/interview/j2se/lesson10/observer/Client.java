package com.j2se.lesson10.observer;

/**
 * Created by bwhite on 2017/10/7.
 */
public class Client {

    public static void main(String[] args) {

        Watched girl = new ConcreteWatched();

        Watcher watcher1 = new ConcreteWatcher();
        Watcher watcher2 = new ConcreteWatcher();
        Watcher watcher3 = new ConcreteWatcher();

        girl.addWatcher(watcher1);
        girl.addWatcher(watcher2);
        girl.addWatcher(watcher3);

        girl.notifyWatcher("nidaye");

    }
}
