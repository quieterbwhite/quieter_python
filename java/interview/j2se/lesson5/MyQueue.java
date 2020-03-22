package com.j2se.lesson5;

import java.util.LinkedList;

/**
 * Created by bwhite on 17-10-5.
 */
public class MyQueue {

    private LinkedList list = new LinkedList();

    public void put(Object o) {
        list.addLast(o);
    }

    public Object get() {
        return list.removeFirst();
    }

    public boolean isEmpty() {
        return list.isEmpty();
    }

    public static void main(String[] args) {
        MyQueue queue = new MyQueue();

        queue.put("one");
        queue.put("two");

        System.out.println(queue.get());
        System.out.println(queue.get());

        System.out.println(queue.isEmpty());

    }
}