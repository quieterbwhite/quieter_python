package com.j2se.lesson5;

import java.util.ArrayList;

/**
 * Created by bwhite on 17-10-4.
 */
public class ArrayListTest4 {

    public static void main(String[] args) {

        ArrayList list = new ArrayList();

        list.add(new Integer(1));
        list.add(new Integer(1));
        list.add(new Integer(1));
        list.add(new Integer(1));
        list.add(new Integer(1));

        // error
        // Integer[] in = (Integer[])list.toArray();

        Object[] in = list.toArray();

        for (int i = 0; i < in.length; i++) {

            System.out.println(((Integer)in[i]).intValue());

        }

    }
}
