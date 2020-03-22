package com.j2se.lesson10;

import com.fasterxml.classmate.Annotations;

import java.lang.annotation.Annotation;
import java.lang.reflect.Method;

/**
 * Created by bwhite on 2017/10/7.
 */
public class MyReflection {

    public static void main(String[] args) throws Exception {

        MyTest test = new MyTest();

        // 获取到类对象
        Class<MyTest> c = MyTest.class;

        Method method = c.getMethod("output", new Class[]{});

        if (method.isAnnotationPresent(MyAnnotation.class)) {
            method.invoke(test, new Object[]{});

            // 上面已经判断有这个注解，那么现在获取到这个注解的实例
            MyAnnotation myAnnotation = method.getAnnotation(MyAnnotation.class);

            String hello = myAnnotation.hello();
            String world = myAnnotation.world();

            System.out.println(hello + ", " + world);
        }

        Annotation[] annotations = method.getAnnotations();

        for (Annotation annotation : annotations) {
            System.out.println(annotation.getClass().getName());
        }

    }
}
