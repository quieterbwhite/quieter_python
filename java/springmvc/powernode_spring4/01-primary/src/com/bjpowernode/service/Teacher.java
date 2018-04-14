package com.bjpowernode.service;

/**
 * Created by bwhite on 18-4-14.
 */
public class Teacher {

    private String name;

    // 没有执行
    public Teacher() {

    }

    public Teacher(String name) {
        this.name = name;
    }

    @Override
    public String toString() {
        return "Teacher{" +
                "name='" + name + '\'' +
                '}';
    }
}
