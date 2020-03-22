package com.j2se.lesson14;

import java.io.BufferedReader;
import java.io.InputStreamReader;

/**
 * Created by bwhite on 2017/10/8.
 */
public class StreamTest2 {

    public static void main(String[] args) throws Exception {

        // 标准输入转字符流对象
        InputStreamReader isr = new InputStreamReader(System.in);

        BufferedReader br = new BufferedReader(isr);

        String str;

        while(null != (str = br.readLine())) {
            System.out.println(str);
        }

        br.close();

    }
}
