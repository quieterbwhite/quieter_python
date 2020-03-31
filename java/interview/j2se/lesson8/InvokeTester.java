package com.j2se.lesson8;

import org.hibernate.boot.jaxb.SourceType;

import javax.sound.sampled.Line;
import java.lang.reflect.Method;

/**
 * Created by bwhite on 2017/10/6.
 */
public class InvokeTester {

    public int add(int param1, int param2) {
        return param1 + param2;
    }

    public String echo(String message) {
        return "hello " + message;
    }

    public static void main(String[] args) throws Exception {

        /*
        InvokeTester test = new InvokeTester();
        System.out.println(test.add(1, 3));
        System.out.println(test.echo("nidaye"));
        */

        // 反射第一步，获取想要操作的类的class对象
        Class<?> classType = InvokeTester.class;

        Object invokeTester = classType.newInstance();

        System.out.println(invokeTester instanceof InvokeTester);

        // 通过名字，参数唯一确定是要获取的哪个方法
        Method addMethod = classType.getMethod("add", new Class[]{int.class, int.class});

        // 返回object, 在invokeTester对象上调用，传参，装箱
        Object result = addMethod.invoke(invokeTester, new Object[]{1, 2});

        // 通过反射，总是返回原生数据类型的包装类
        System.out.println((Integer)result);

        System.out.println("-------------------------");

        Method echoMethod = classType.getMethod("echo", new Class[]{String.class});

        // 调用 invoke 并不知道返回类型, 所以用Object接收, 可以在使用的时候转换
        Object result2 = echoMethod.invoke(invokeTester, new Object[]{"nimenhao"});

        System.out.println((String)result2);






    }
}
