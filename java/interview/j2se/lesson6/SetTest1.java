package com.j2se.lesson6;

import java.util.HashSet;

/**
 * Created by bwhite on 17-10-5.
 */
public class SetTest1 {

    public static void main(String[] args) {

        HashSet set = new HashSet();

        // 放到集合中没有顺序,不重复

        System.out.println(set.add("a"));  // true
        set.add("b");
        set.add("c");
        System.out.println(set.add("a"));  // false, 已存在不能添加进去

        System.out.println(set);
    }
}