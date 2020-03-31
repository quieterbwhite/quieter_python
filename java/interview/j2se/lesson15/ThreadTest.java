package com.j2se.lesson15;

/**
 * Created by bwhite on 2017/10/8.
 */
public class ThreadTest {

    public static void main(String[] args) {

        Thread2 t2 = new Thread2();
        Thread1 t1 = new Thread1();

        // start() 方法首先为线程的执行准备好系统资源,然后再去调用run()方法
        t1.start();
        t2.start();

        // 只是普通的run方法
        // t1.run();
        // t2.run();
    }
}


class Thread1 extends Thread {

    @Override
    public void run() {
        for (int i = 0; i < 100; i++) {
            System.out.println("hello " + i);
        }
    }
}

class Thread2 extends Thread {
    @Override
    public void run() {
        for (int i = 0; i < 100; i++) {
            System.out.println("welcome " + i);
        }
    }
}