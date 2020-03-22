package com.j2se.lesson14;

import java.io.*;

/**
 * Created by bwhite on 2017/10/8.
 */
public class DataStream1 {

    public static void main(String[] args) throws Exception {

        // 龙哥学的时候也是不能理解为什么一层包一层的,不知道哪个该包哪个
        // 这里封装了几层，dos 功能被增强了
        DataOutputStream dos = new DataOutputStream(new BufferedOutputStream(
                new FileOutputStream("d:/nidaye.txt")));

        byte b = 3;
        int i = 12;
        char ch = 'n';
        float f = 3.3f;

        // 类型的信息也保存到文件里面去了, 文件里有机制表示各数据类型
        // DataOutputStream 可以写基本数据类型, 写进去是乱码，实际是二进制文件。
        dos.writeByte(b);
        dos.writeInt(i);
        dos.writeChar(ch);
        dos.writeFloat(f);

        // 最外层的关闭，里面的也就全部关闭了
        dos.close();

        ///////////////////////////////////////////

        DataInputStream dis = new DataInputStream(new BufferedInputStream(
                new FileInputStream("d:/nidaye.txt")));

        // 读和写的顺序保持一致, 从二进制文件读数据, 如果跨数据类型长度读，整个数据就乱了
        System.out.println(dis.readByte());
        System.out.println(dis.readInt());
        System.out.println(dis.readChar());
        System.out.println(dis.readFloat());

        dis.close();

    }
}
