package com.bjpowernode.service;

/**
 * Created by bwhite on 18-4-14.
 */
public class Student {

    private String name;

    private int age;

    private School school;

    @Override
    public String toString() {
        return "Student{" +
                "name='" + name + '\'' +
                ", age=" + age +
                ", school=" + school +
                '}';
    }

    public School getSchool() {
        return school;
    }

    public void setSchool(School school) {
        this.school = school;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        System.out.println("执行 setName()");
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        System.out.println("执行 setAge()");
        this.age = age;
    }

}
