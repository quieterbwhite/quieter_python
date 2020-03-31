package com.j2se.lesson8;

/**
 * Created by bwhite on 2017/10/6.
 */
public class ColorTest {

    public static void main(String[] args) {

        ColorEnum myColor = ColorEnum.Blue;

        System.out.println(myColor);

        for (ColorEnum color : ColorEnum.values()) {
            System.out.println(color);
        }
    }
}
