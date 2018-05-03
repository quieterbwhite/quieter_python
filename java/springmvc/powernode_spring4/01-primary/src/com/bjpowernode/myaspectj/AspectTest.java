package com.bjpowernode.myaspectj;

import com.bjpowernode.service.ISomeService;
import com.bjpowernode.service.SomeServiceImpl;
import org.junit.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

/**
 * Created by bwhite on 18-4-30.
 */
public class AspectTest {

    @Test
    public void test01() {

        ApplicationContext ac = new ClassPathXmlApplicationContext("applicationContext.xml");

        ITheService service = (ITheService)ac.getBean("theService");
        service.doSome();

    }
}
