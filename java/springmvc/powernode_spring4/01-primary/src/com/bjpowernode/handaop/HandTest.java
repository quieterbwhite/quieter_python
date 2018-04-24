package com.bjpowernode.handaop;

import org.junit.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

/**
 * Created by bwhite on 18-4-21.
 */
public class HandTest {

    @Test
    public void test01() {
        ApplicationContext ac = new ClassPathXmlApplicationContext("applicationContext.xml");
        IHandService service = (IHandService)ac.getBean("serviceProxy");
        service.doLeft();
        service.doRight();
    }
}
