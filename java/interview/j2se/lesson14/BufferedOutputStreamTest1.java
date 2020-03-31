package com.j2se.lesson14;

import java.io.BufferedOutputStream;
import java.io.FileOutputStream;
import java.io.OutputStream;

/**
 * Created by bwhite on 2017/10/8.
 */
public class BufferedOutputStreamTest1 {

    public static void main(String[] args) throws Exception {

        // 也可以相对路径 new FileOutputStream("tiger.txt")
        OutputStream os = new FileOutputStream("d:/tiger.txt");

        // 加不加这个过滤流 效率是有差别的。 写到内存缓冲区
        BufferedOutputStream bos = new BufferedOutputStream(os);

        bos.write("http://github.com".getBytes());

        bos.close();
        os.close();

    }

}
