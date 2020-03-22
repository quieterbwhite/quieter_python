package com.j2se.lesson7;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;

/**
 * T 可选的类型为 实现了 List 接口的类型
 * Created by bwhite on 2017/10/6.
 */
public class ListGenericFoo<T extends List> {

    private T[] fooArray;

    public T[] getFooArray() {
        return fooArray;
    }

    public void setFooArray(T[] fooArray) {
        this.fooArray = fooArray;
    }

    public static void main(String[] args) {

        ListGenericFoo<LinkedList> foo1 = new ListGenericFoo<LinkedList>();
        ListGenericFoo<ArrayList> foo2 = new ListGenericFoo<ArrayList>();

        LinkedList[] linkedLists = new LinkedList[10];
        foo1.setFooArray(linkedLists);

        ArrayList[] arrayLists = new ArrayList[10];
        foo2.setFooArray(arrayLists);

        // ListGenericFoo<HashMap> foo2 = new ListGenericFoo<HashMap>();

    }
}
