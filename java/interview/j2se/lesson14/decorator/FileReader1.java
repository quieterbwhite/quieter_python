package com.j2se.lesson14.decorator;

import java.io.BufferedReader;
import java.io.FileReader;

/**
 * Created by bwhite on 2017/10/8.
 */
public class FileReader1 {

    public static void main(String[] args) throws Exception {

        FileReader fe = new FileReader("d:/nidaye.txt");

        BufferedReader br = new BufferedReader(fe);

        String str;

        while(null != (str = br.readLine())) {
            System.out.println(str);
        }

        br.close();


    }
}
