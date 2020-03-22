package com.j2se.lesson7;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

/**
 * Created by bwhite on 2017/10/6.
 */
public class GenericTest<T> {

    private T foo;

    public T getFoo() {
        return foo;
    }

    public void setFoo(T foo) {
        this.foo = foo;
    }

    public static void main(String[] args) {
        GenericTest<? extends List> ge = null;

        ge = new GenericTest<ArrayList>();
        ge = new GenericTest<LinkedList>();

    }
}
