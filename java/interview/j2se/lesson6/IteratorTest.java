package com.j2se.lesson6;

import java.util.Iterator;
import java.util.HashSet;


/**
 * 迭代器，用的频率相当高
 * Created by bwhite on 17-10-5.
 */
public class IteratorTest {

    public static void main(String[] args) {

        HashSet set = new HashSet();

        set.add("a");
        set.add("b");
        set.add("c");

        System.out.println(set);

        // 获得迭代器
        Iterator iter = set.iterator();

        // 循环获取
        while(iter.hasNext()) {
            String value = (String)iter.next();
            System.out.println(value);
        }

        for(Iterator iter2=set.iterator(); iter2.hasNext();) {
            String value = (String)iter2.next();
            System.out.println(value);
        }

    }

}