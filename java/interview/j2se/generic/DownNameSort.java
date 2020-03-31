package com.j2se.generic;

import java.util.Comparator;
import java.util.List;

/**
 * Created by bwhite on 2017/8/19.
 */
public class DownNameSort implements SortInterface, Comparator<Person> {

    @Override
    public void sort(List<Person> list) {

    }

    @Override
    public int compare(Person o1, Person o2) {

        int result = o2.getName().compareTo(o1.getName());

        if (0 == result) {
            return o1.getId() - o2.getId();
        }

        return result;
    }
}
