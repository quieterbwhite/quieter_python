package com.j2se.lesson7.strategy;

import java.util.Collections;
import java.util.Comparator;
import java.util.List;

/**
 * 根据名字升序排序
 * 这里将 Comparator 和 sort 实现在了一起
 * Created by bwhite on 2017/10/6.
 */
public class UpNameSort implements SortInterface, Comparator<Person> {

    @Override
    public void sort(List<Person> list) {
        // this 表示当前对象的引用
        // this 本身实现了 Comparator<Person>
        Collections.sort(list, this);
    }

    @Override
    public int compare(Person o1, Person o2) {

        int result = o1.getName().compareTo(o2.getName());

        // 如果名字相同，根据 id 排序
        if (0 == result) {
            return o1.getId() - o2.getId();
        }

        return result;
    }
}
