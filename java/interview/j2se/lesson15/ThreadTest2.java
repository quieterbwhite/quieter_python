package com.j2se.lesson15;

import com.sun.scenario.effect.impl.sw.sse.SSEBlend_SRC_OUTPeer;
import org.hibernate.jpa.internal.schemagen.ScriptTargetOutputToUrl;

/**
 * Created by bwhite on 2017/10/8.
 */
public class ThreadTest2 {

    public static void main(String[] args) {

        Thread t1 = new Thread(new MyThread());
        t1.start();
    }
}

class MyThread implements Runnable {

    @Override
    public void run() {
        for (int i = 0; i < 100; i++) {
            System.out.println("hello " + i);
        }
    }
}