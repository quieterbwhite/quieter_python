package com.j2se.lesson8;

/**
 * Created by bwhite on 2017/10/6.
 */
public enum Coin {

    penny("hello"), quarter("hello world");

    private String value;

    public String getValue(){
        return value;
    }

    Coin(String value) {
        this.value = value;
    }

    public static void main(String[] args) {
        Coin coin = Coin.quarter;

        System.out.println(coin.getValue());
    }
}
