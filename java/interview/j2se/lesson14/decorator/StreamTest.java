package com.j2se.lesson14.decorator;

import java.io.*;

/**
 * Created by bwhite on 2017/10/8.
 */
public class StreamTest {

    public static void main(String[] args) throws Exception {
        FileOutputStream fos = new FileOutputStream("d:/nidaye.txt");

        OutputStreamWriter osw = new OutputStreamWriter(fos);

        BufferedWriter bw = new BufferedWriter(osw);

        bw.write("http://baidu.com");
        bw.write("\n");
        bw.write("http://google.com");

        bw.close();

        ////////////////////////////////////////

        FileInputStream fis = new FileInputStream("d:/nidaye.txt");
        InputStreamReader isr = new InputStreamReader(fis);
        BufferedReader br = new BufferedReader(isr);

        System.out.println(br.readLine());
        System.out.println(br.readLine());

        br.close();
    }
}
