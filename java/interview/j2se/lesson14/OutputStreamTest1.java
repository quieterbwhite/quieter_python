package com.j2se.lesson14;

import java.io.FileOutputStream;
import java.io.OutputStream;

/**
 * Created by bwhite on 2017/10/8.
 */
public class OutputStreamTest1 {

    public static void main(String[] args) throws Exception {

        // append 追加或覆盖， 没有文件的话会创建
        OutputStream os = new FileOutputStream("d:/tiger.txt", true);

        String str = "hello tiger";
        byte[] buffer = str.getBytes();

        os.write(buffer);

        os.close();

    }
}
