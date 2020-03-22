package com.j2se.lesson7;

import java.util.HashSet;
import java.util.Iterator;
import java.util.Set;

/**
 * Created by bwhite on 2017/10/6.
 */
public class SetTest {

    public static void main(String[] args) {

        HashSet<String> set = new HashSet<String>();

        set.add("a");
        set.add("b");
        set.add("c");

        for (Iterator<String> iter = set.iterator(); iter.hasNext();) {
            String value = iter.next();
            System.out.println(value);
        }

        System.out.println("-------------------------------");

        Set<People> set2 = new HashSet<People>();

        set2.add(new People("li", 20, "beijing"));
        set2.add(new People("zhang", 22, "chengdu"));
        set2.add(new People("zhao", 24, "tianjing"));

        for (Iterator<People> iter = set2.iterator(); iter.hasNext(); ) {
            People p = iter.next();
            System.out.println(p.getName() + " : " + p.getAge() + " : " + p.getAddress());
        }

    }
}


class People {
    private String name;

    private int age;

    private String address;

    public People(String name, int age, String address) {
        this.name = name;
        this.age = age;
        this.address = address;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        People people = (People) o;

        if (age != people.age) return false;
        if (name != null ? !name.equals(people.name) : people.name != null) return false;
        return address != null ? address.equals(people.address) : people.address == null;
    }

    @Override
    public int hashCode() {
        int result = name != null ? name.hashCode() : 0;
        result = 31 * result + age;
        result = 31 * result + (address != null ? address.hashCode() : 0);
        return result;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
}