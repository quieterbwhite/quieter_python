package com.j2se.lesson5;

import org.hibernate.boot.jaxb.SourceType;

import java.util.ArrayList;

/**
 * Created by bwhite on 17-10-4.
 */
public class ArrayListTest1 {

    public static void main(String[] args) {

        ArrayList arrayList = new ArrayList();

        arrayList.add("hello");
        arrayList.add("world");
        arrayList.add("welcome");

        String s1 = (String)arrayList.get(0);
        String s2 = (String)arrayList.get(1);
        String s3 = (String)arrayList.get(2);

        System.out.println(s1);
        System.out.println(s2);
        System.out.println(s3);

        System.out.println("--------------------");

        for(int i = 0; i < arrayList.size(); i++) {
            System.out.println(arrayList.get(i));
        }

        System.out.println("--------------------");

        arrayList.clear();

        System.out.println(arrayList.size());

        System.out.println("--------------------");


    }
}
