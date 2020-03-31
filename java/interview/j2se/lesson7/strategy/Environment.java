package com.j2se.lesson7.strategy;


import java.util.List;

/**
 * Created by bwhite on 2017/10/6.
 */
public class Environment {

    private SortInterface sortInterface;

    public Environment(SortInterface sortInterface) {
        this.sortInterface = sortInterface;
    }

    public Environment() {}

    public void setSortInterface(SortInterface sortInterface) {
        this.sortInterface = sortInterface;
    }

    public void sort(List<Person> list) {
        this.sortInterface.sort(list);
    }
}
