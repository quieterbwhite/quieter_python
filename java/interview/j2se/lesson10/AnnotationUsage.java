package com.j2se.lesson10;

/**
 * Created by bwhite on 2017/10/7.
 */
public class AnnotationUsage {

    @AnnotationTest(value="nidaye", value2=EnumTest.Hello)
    public void method() {
        System.out.println("Usage of annotations");
    }

    public static void main(String[] args) {
        AnnotationUsage usage = new AnnotationUsage();

        usage.method();
    }
}
