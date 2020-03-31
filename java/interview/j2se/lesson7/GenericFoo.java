package com.j2se.lesson7;


/**
 * Created by bwhite on 2017/10/6.
 */
public class GenericFoo<T> {

    // 重点！把T通过<>传进来了，看成员变量定义方式，可以理解为把类型传进来了
    private T foo;

    public T getFoo() {
        return foo;
    }

    public void setFoo(T foo) {
        this.foo = foo;
    }

    public static void main(String[] args) {
        GenericFoo<Boolean> foo1 = new GenericFoo<Boolean>();
        GenericFoo<Integer> foo2 = new GenericFoo<Integer>();

        foo1.setFoo(new Boolean(false));
        foo2.setFoo(new Integer(1));

        Boolean b = foo1.getFoo();
        Integer i = foo2.getFoo();

        System.out.println(b);
        System.out.println(i);
    }
}
