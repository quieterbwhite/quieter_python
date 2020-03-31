package com.j2se.lesson7;

import java.util.ArrayList;
import java.util.Collection;

/**
 * Created by bwhite on 2017/10/6.
 */
public class ForTest {

    public static void main(String[] args) {

        int[] arr = {1, 2, 3, 4, 5};

        // old
        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i]);
        }

        System.out.println("--------------");

        // new
        for (int element : arr) {
            System.out.println(element);
        }

        Collection<String> col = new ArrayList<String>();
        col.add("a");
        col.add("b");
        col.add("c");

        for (String str : col) {
            System.out.println(str);
        }

    }
}
