package com.j2se.lesson14;

import java.io.ByteArrayOutputStream;
import java.io.FileOutputStream;
import java.io.OutputStream;

/**
 * Created by bwhite on 2017/10/8.
 */
public class ByteArrayOutputStreamTest1 {

    public static void main(String[] args) throws Exception {

        ByteArrayOutputStream f = new ByteArrayOutputStream();

        String str = "hello world";

        byte[] buffer = str.getBytes();

        // 把 buffer 里的东西写到 f 中
        f.write(buffer);

        // 将流里面的数据转换成字节数组
        byte[] result = f.toByteArray();

        for (int i = 0; i < result.length; i++) {
            System.out.println((char)result[i]);
        }

        OutputStream os = new FileOutputStream("d:/nidaye.txt");

        f.writeTo(os);

        f.close();
        os.close();

    }
}
