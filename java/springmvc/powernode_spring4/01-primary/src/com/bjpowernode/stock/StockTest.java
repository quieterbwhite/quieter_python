package com.bjpowernode.stock;

import com.bjpowernode.myaspectj.ITheService;
import org.junit.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

/**
 * Created by bwhite on 18-5-3.
 */
public class StockTest {

    @Test
    public void test01() throws Exception {

        ApplicationContext ac = new ClassPathXmlApplicationContext("applicationContext.xml");

//        IStockProcessService service = (IStockProcessService)ac.getBean("stockService");
        IStockProcessService service = (IStockProcessService)ac.getBean("stockServiceProxy");  // 使用代理

//        service.openAccount("libo", 44);
//        service.openStock("tiger",10);

        service.buyStock("libo", 22, "tiger", 2);

    }
}
