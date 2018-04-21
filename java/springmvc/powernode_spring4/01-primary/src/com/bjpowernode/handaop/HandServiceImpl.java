package com.bjpowernode.handaop;

/**
 * Created by bwhite on 18-4-21.
 */
public class HandServiceImpl implements IHandService {

    @Override
    public void doRight() {
        System.out.println("do right");
    }

    @Override
    public String doLeft() {
        System.out.println("do left");
        return "Tiger";
    }
}
