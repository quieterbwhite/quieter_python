package com.j2se.lesson15;


/**
 * Created by bwhite on 2017/10/8.
 */
public class ThreadTest3 {

    public static void main(String[] args) {

        Runnable r = new HelloThread();

        Thread t1 = new Thread(r);
        Thread t2 = new Thread(r);

        t1.start();
        t2.start();
    }


}

class HelloThread implements Runnable {

    // 成员变量
    // new了一个对象, 两个线程共享这一个成员变量,
    int i;

    @Override
    public void run() {

        // 局部变量
        // 每个线程有一份局部变量的拷贝, 他们之间互不影响
        // int i = 0;

        while (true) {

            System.out.println("number: " + i++);

            try {
                Thread.sleep((long)Math.random()*1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

            if(50 == i) {
                break;
            }

        }
    }
}
