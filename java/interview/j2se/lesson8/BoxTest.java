package com.j2se.lesson8;


import java.util.ArrayList;
import java.util.Collection;

/**
 * Created by bwhite on 2017/10/6.
 */
public class BoxTest {

    public static void main(String[] args) {

        int a = 3;
        Collection<Integer> c = new ArrayList<Integer>();
        // 将int类型的3转换为Integer类型并放到集合中
        c.add(3);
        c.add(a + 3);
        for (Integer i : c) {
            System.out.println(i);
        }

    }
}
