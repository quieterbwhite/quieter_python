package com.bjpowernode.service;

/**
 * Created by bwhite on 18-4-14.
 */
public class School {

    private String name;

    @Override
    public String toString() {
        return "School{" +
                "name='" + name + '\'' +
                '}';
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
