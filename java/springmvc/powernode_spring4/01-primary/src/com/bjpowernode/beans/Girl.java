package com.bjpowernode.beans;

/**
 * Created by bwhite on 18-4-30.
 */
public class Girl {

    private Integer id;

    private String cup_size;

    private int age;

    public Girl() {

    }

    public Girl(Integer id, String cup_size, int age) {
        this.id = id;
        this.cup_size = cup_size;
        this.age = age;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getcup_size() {
        return cup_size;
    }

    public void setcup_size(String cup_size) {
        this.cup_size = cup_size;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    @Override
    public String toString() {
        return "Girl{" +
                "id=" + id +
                ", cup_size='" + cup_size + '\'' +
                ", age=" + age +
                '}';
    }
}
