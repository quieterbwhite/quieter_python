package com.j2se.lesson6;

import java.util.HashSet;

/**
 * Created by bwhite on 17-10-5.
 */
public class SetTest2 {

    public static void main(String[] args) {

        HashSet set = new HashSet();

        set.add(new People("zhangsan"));
        set.add(new People("lisi"));
        set.add(new People("zhangsan"));

        People p1 = new People("tiger");
        set.add(p1);
        set.add(p1); // 相同的对象不能再次添加

        String a1 = new String("a1");
        String a2 = new String("a2"); // hash code 值是一样的
        set.add(a1); // equals string 比较的是字面值
        set.add(a2); // 虽然a1, a2是两个对象，但是仍然只有一个添加进去

        System.out.println(set);

    }
}

class People {

    String name;

    public People(String name) {
        this.name = name;
    }
}