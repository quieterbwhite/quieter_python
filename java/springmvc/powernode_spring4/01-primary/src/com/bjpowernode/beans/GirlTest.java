package com.bjpowernode.beans;

import com.bjpowernode.myaspectj.ITheService;
import org.junit.Before;
import org.junit.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

/**
 * Created by bwhite on 18-4-30.
 */
public class GirlTest {

    @Test
    public void testAdd(){
        ApplicationContext ac = new ClassPathXmlApplicationContext("applicationContext.xml");
        IMyGirlService service = (IMyGirlService) ac.getBean("girlService");
        service.addGirl(new Girl(1, "B", 22));
    }

    @Test
    public void testRemove() {
//        service.removeGirl(2);
    }
}
