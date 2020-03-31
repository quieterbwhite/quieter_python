package com.j2se.lesson10.observer;

/**
 * 抽象主题角色
 * Created by bwhite on 2017/10/7.
 */
public interface Watched {

    public void addWatcher(Watcher watcher);

    public void removeWatcher(Watcher watcher);

    public void notifyWatcher(String str);
}
