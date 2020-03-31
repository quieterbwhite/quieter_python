package com.j2se.lesson7.strategy;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by bwhite on 2017/10/6.
 */
public class Client {

    public static void main(String[] args) {

        Person p1 = new Person();
        p1.setName("tom");
        p1.setId(1);
        p1.setAge(10);

        Person p2 = new Person();
        p2.setName("andy");
        p2.setId(2);
        p2.setAge(23);

        List<Person> list = new ArrayList<Person>();

        list.add(p1);
        list.add(p2);

        Environment env = new Environment();

        UpNameSort uns = new UpNameSort();

        env.setSortInterface(uns);

        env.sort(list);

    }
}
