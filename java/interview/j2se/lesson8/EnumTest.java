package com.j2se.lesson8;

/**
 * Created by bwhite on 2017/10/6.
 */
public class EnumTest {

    public static void doOp(OpConstant opConstant) {

        switch (opConstant) {
            case TURN_LEFT:
                System.out.println("turn_left");
                break;
            case TURN_RIGHT:
                System.out.println("turn_right");
                break;
            case SHOOT:
                System.out.println("shoot");
                break;
        }
    }

    public static void main(String[] args) {
        doOp(OpConstant.TURN_LEFT);
    }
}

enum OpConstant {
    TURN_LEFT, TURN_RIGHT, SHOOT
}
