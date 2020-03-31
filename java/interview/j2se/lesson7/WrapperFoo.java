package com.j2se.lesson7;

import org.omg.CORBA.INTERNAL;

/**
 * 泛型的泛型
 * Created by bwhite on 2017/10/6.
 */
public class WrapperFoo<T> {

    private GenericFoo3<T> foo;

    public static void main(String[] args) {

        GenericFoo3<Integer> foo = new GenericFoo3<Integer>();
        foo.setFoo(new Integer(3));

        WrapperFoo<Integer> wapper = new WrapperFoo<Integer>();
        wapper.setFoo(foo);

        GenericFoo3<Integer> g = wapper.getFoo();
        System.out.println(g.getFoo());

    }

    public GenericFoo3<T> getFoo() {
        return foo;
    }

    public void setFoo(GenericFoo3<T> foo) {
        this.foo = foo;
    }
}

class GenericFoo3<T> {

    private T foo;

    public T getFoo() {
        return foo;
    }

    public void setFoo(T foo) {
        this.foo = foo;
    }
}
