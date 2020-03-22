package com.j2se.lesson6;

import java.util.TreeSet;

/**
 * Created by bwhite on 17-10-5.
 */
public class TreeSetTest {

    public static void main(String[] args) {

        TreeSet set = new TreeSet();

        set.add("a");
        set.add("b");
        set.add("c");

        // 自然顺序输出
        System.out.println(set);

    }

}