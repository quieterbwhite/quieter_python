package com.j2se.generic;

import java.util.Collections;
import java.util.Comparator;
import java.util.List;

/**
 * 按照名字的升序排列
 * Created by bwhite on 2017/8/19.
 */
public class UpNameSort implements SortInterface, Comparator<Person> {


    @Override
    public void sort(List<Person> list) {

        /**
         * list, 第一个参数，待排序的列表
         * this, 当前对象，比较的时候会使用当前对象的 compare 方法
         */
        Collections.sort(list, this);
    }

    // 根据名字进行排序
    public int compare(Person o1, Person o2) {
        int result = o1.getName().compareTo(o2.getName());

        if (0 == result) {
            return o1.getId() - o2.getId();
        }

        return result;
    }
}
