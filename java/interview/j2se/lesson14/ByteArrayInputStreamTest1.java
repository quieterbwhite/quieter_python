package com.j2se.lesson14;

import java.io.ByteArrayInputStream;

/**
 * Created by bwhite on 2017/10/8.
 */
public class ByteArrayInputStreamTest1 {

    public static void main(String[] args) {

        String str = "hello world";

        // 输入源
        byte[] b = str.getBytes();

        ByteArrayInputStream in = new ByteArrayInputStream(b);

        for (int i = 0; i < str.length(); i++) {

            int c;

            // read 每次读一个字节
            while(-1 != (c = in.read())) {
                if (0 == i) {
                    System.out.println((char)c);
                } else {
                    System.out.println(Character.toUpperCase((char)c));
                }
            }

            System.out.println();

            in.reset();

        }

    }
}
