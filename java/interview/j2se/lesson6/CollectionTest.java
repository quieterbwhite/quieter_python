package com.j2se.lesson6;

import java.util.Collections;
import java.util.Comparator;
import java.util.Iterator;
import java.util.LinkedList;

/**
 * Created by bwhite on 2017/10/5.
 */
public class CollectionTest {

    public static void main(String[] args) {

        LinkedList list = new LinkedList();

        list.add(new Integer(10));
        list.add(new Integer(3));
        list.add(new Integer(-8));
        list.add(new Integer(99));

        // 排序一个集合
        Comparator r = Collections.reverseOrder();
        Collections.sort(list, r);
        for (Iterator iter=list.iterator(); iter.hasNext();) {
            System.out.println(iter.next() + " ");
        }

        // 换行
        System.out.println();

        // 打乱顺序
        Collections.shuffle(list);
        for (Iterator iter=list.iterator(); iter.hasNext();) {
            System.out.println(iter.next() + " ");
        }

        System.out.println("mix: " + Collections.min(list));
        System.out.println("max: " + Collections.max(list));

    }
}
