package com.j2se.lesson15;

/**
 * Created by bwhite on 2017/10/9.
 */
public class MainTest {

    public static void main(String[] args) {

        Sample sample = new Sample();

        Thread t1 = new IncreaseThread(sample);
        Thread t2 = new DecreaseThread(sample);
        Thread t3 = new IncreaseThread(sample);
        Thread t4 = new DecreaseThread(sample);

        t1.start();
        t2.start();
        t3.start();
        t4.start();

    }
}
