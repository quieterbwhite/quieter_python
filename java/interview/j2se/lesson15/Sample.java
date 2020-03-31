package com.j2se.lesson15;

/**
 * Created by bwhite on 2017/10/9.
 */
public class Sample {

    private int number;

    public synchronized void increase() {
        while (0 != number) {
            try {
                wait();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        number++;

        System.out.println("number: " + number);

        notify();
    }

    public synchronized void decrease() {
        while (0 == number) {
            try {
                wait();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        number--;

        System.out.println("number: " + number);

        notify();
    }
}
