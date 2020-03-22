package com.j2se.lesson7;

/**
 * Created by bwhite on 2017/10/6.
 */
public interface ParentInterface<T1, T2> {

    public void setFoo1(T1 foo1);

    public void setFoo2(T2 foo2);

    public T1 getFoo1();

    public T2 getFoo2();
}
