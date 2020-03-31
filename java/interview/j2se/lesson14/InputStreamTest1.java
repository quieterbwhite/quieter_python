package com.j2se.lesson14;

import java.io.FileInputStream;
import java.io.InputStream;

/**
 * Created by bwhite on 2017/10/8.
 */
public class InputStreamTest1 {

    public static void main(String[] args) throws Exception {

        InputStream is = new FileInputStream("d:/hello.txt");

        byte[] buffer = new byte[200];

        int length = 0;

        // 每次最多读200到buffer中
        while( -1 != (length = is.read(buffer, 0, 200))){
            String str = new String(buffer, 0, length);

            System.out.println(str);
        }

        is.close();

    }
}
