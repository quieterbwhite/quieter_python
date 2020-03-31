package com.j2se.lesson6;

import java.util.HashSet;

/**
 * Created by bwhite on 17-10-5.
 */
public class SetTest3 {

    public static void main(String[] args) {

        HashSet set = new HashSet();

        Student s1 = new Student("lisi");
        Student s2 = new Student("lisi");

        set.add(s1);
        set.add(s1); // 增加不进去

        System.out.println(set);

    }
}

class Student {

    String name;

    public Student(String name) {
        this.name = name;
    }

    public int hashCode() {
        return this.name.hashCode();
    }

    public boolean equals(Object obj) {
        if(this == obj) {
            return true;
        }

        if(null != obj && obj instanceof Student) {
            // 向下类型转换
            Student s = (Student)obj;

            if(name.equals(s.name)) {
                return true;
            }
        }

        return false;
    }
}