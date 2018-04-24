package com.bjpowernode.leadinaop;

/**
 * Created by bwhite on 18-4-21.
 * 工具类，提供静态方法给外部使用， 可以对主业务进行增强
 * 也存在问题：
 *  系统级服务和主业务也是混杂在一起的，因为也需要编码到业务代码中去。
 *  代码可读性差
 *
 * 所以需要把系统级服务和主业务分开，剥离出来.
 *  代理
 *  声明式编程
 */
public class SomeUtils {

    public static void doTransaction() {
        System.out.println("Do Transaction.");
    }

    public static void doLog() {
        System.out.println("Do Log");
    }
}
