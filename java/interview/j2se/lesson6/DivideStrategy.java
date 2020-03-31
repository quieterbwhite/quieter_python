package com.j2se.lesson6;

/**
 * Created by bwhite on 2017/10/6.
 */
public class DivideStrategy implements Strategy {

    @Override
    public int calculata(int a, int b) {
        return a / b;
    }
}
