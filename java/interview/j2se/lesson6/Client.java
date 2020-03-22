package com.j2se.lesson6;

/**
 * Created by bwhite on 2017/10/6.
 */
public class Client {

    public static void main(String[] args) {
        AddStrategy strategy = new AddStrategy();

        Environment env = new Environment(strategy);

        System.out.println(env.calculate(3, 4));
    }
}
