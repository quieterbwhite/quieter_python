package com.j2se.lesson6;

import java.util.Comparator;
import java.util.Iterator;
import java.util.TreeSet;

/**
 * Created by bwhite on 2017/10/5.
 */
public class TreeSetTest3 {

    public static void main(String[] args) {
        TreeSet set = new TreeSet(new MyComparator());

        set.add("a");
        set.add("b");
        set.add("c");
        set.add("d");

        for (Iterator iter = set.iterator(); iter.hasNext();) {
            String value = (String)iter.next();
            System.out.println(value);
        }
    }
}

class MyComparator implements Comparator {

    @Override
    public int compare(Object o1, Object o2) {
        String s1 = (String)o1;
        String s2 = (String)o2;

        return s2.compareTo(s1);
    }
}