package com.j2se.lesson4;

/**
 * StringBuffer 是可变的。String 是不可变的。
 *
 * thread safe
 *
 * StringBuilder, NOT a thread safe object
 *
 * Created by bwhite on 2017/8/20.
 */
public class StringBufferTest {

    public static void main(String[] args) {

        // StringBuffer 对象并不是一个 String 对象
        StringBuffer sb = new StringBuffer();

        sb.append("hello").append(" world").append(" welcome").append(100).append(false);

        // 最终我们需要的是一个 String 对象，所以转换, 返回一个字符串
        String result = sb.toString();
        // output: hello world welcome100false
        System.out.println(result);

        // 测试不同类型 拼接
        String a = "abc";
        int b = 100;
        Boolean c = true;
        String s = a + b + c;
        // output: abc100true
        System.out.println(s);

        // output: 100200
        // 凡是和字符串拼接(+)的非字符串变量都会先转换为字符串再拼接
        System.out.println("100" + 200);

        // 错误的语法
        // System.out.println(false + true);



        // sb.append("hello");
        // sb.append(" world");
        // sb.append(" welcome");

    }

}
