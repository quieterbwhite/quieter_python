package com.bjpowernode.test;

import com.bjpowernode.annotationdi.Animal;
import org.junit.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

/**
 * Created by bwhite on 18-4-18.
 */
public class AnnotationTest {

    @Test
    public void test01() {
        ApplicationContext ac = new ClassPathXmlApplicationContext("applicationContext.xml");
        Animal animal = (Animal) ac.getBean("myAnimal");
        System.out.println(animal);
    }
}
