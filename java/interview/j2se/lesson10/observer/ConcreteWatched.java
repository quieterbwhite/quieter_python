package com.j2se.lesson10.observer;

import java.util.ArrayList;
import java.util.List;

/**
 * 具体的主题角色
 * Created by bwhite on 2017/10/7.
 */
public class ConcreteWatched implements Watched {

    // 成员变量 存放观察者
    private List<Watcher> list = new ArrayList<Watcher>();

    @Override
    public void addWatcher(Watcher watcher) {
        list.add(watcher);
    }

    @Override
    public void removeWatcher(Watcher watcher) {
        list.remove(watcher);
    }

    @Override
    public void notifyWatcher(String str) {
        for (Watcher watcher : list) {
            watcher.update(str);
        }
    }
}
