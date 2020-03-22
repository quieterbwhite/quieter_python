package com.j2se.lesson14;

import java.io.FileWriter;

/**
 * class 95 没有详细看
 * Created by bwhite on 2017/10/8.
 */
public class FileWriter1 {

    public static void main(String[] args) throws Exception{

        String str = "hello world spider python";

        char[] buffer = new char[str.length()];

        str.getChars(0, str.length(), buffer, 0);

        System.out.println(buffer);

        FileWriter fw = new FileWriter("d:/nidaye.txt");

        for (int i = 0; i < buffer.length; i++) {
            fw.write(buffer);
        }

        fw.close();

    }
}
