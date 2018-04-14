package com.bjpowernode.test;

import com.bjpowernode.service.*;
import org.junit.Test;
import org.springframework.beans.factory.BeanFactory;
import org.springframework.beans.factory.xml.XmlBeanFactory;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
import org.springframework.core.io.ClassPathResource;

/**
 * Created by bwhite on 2016/12/3.
 */
public class MyTest {

    // 不使用 Spring 容器
    // 代码中的问题是: SomeServiceImpl 这个类, 完全耦合到了测试类中
    @Test
    public void test01() {
        ISomeService someService = new SomeServiceImpl();
        someService.doSome();
    }

    // 从容器中获取 Bean, 使 Bean 类与测试类解耦合
    @Test
    public void test02() {
        // 创建容器
        ApplicationContext ac = new ClassPathXmlApplicationContext("applicationContext.xml");
        ISomeService someService = (ISomeService) ac.getBean("someService");
        someService.doSome();
    }

    // 还可以使用 FileSystemXmlApplicationContext 来加载文件路径中的 ac 配置文件
    // 基本不用，所以就不写例子了

    // ApplicationContext 容器: 在初始化容器时, 就将容器中所有对象进行了创建  一开始创建全部对象,占用内存,效率高
    // BeanFactory 容器, 使用时才创建  需要对象时才创建,节约内存,效率低 基本不用
    // 直接使用 BeanFactory 容器的例子:
    @Test
    public void test03() {
        // 创建容器
        BeanFactory bf = new XmlBeanFactory(new ClassPathResource("applicationContext.xml"));
        ISomeService someService = (ISomeService) bf.getBean("someService");
        someService.doSome();
    }

    /**
     * Bean的装配 - 动态工厂Bean 例子
     */
    @Test
    public void test04() {
        // 创建容器
        ApplicationContext ac = new ClassPathXmlApplicationContext("applicationContext.xml");

        // 测试类与工厂类耦合到了一起
        SomeFactory someFactory = (SomeFactory)ac.getBean("someFactory");
        ISomeService service = someFactory.getSomeService();
        service.doSome();
    }

    /**
     * Bean的装配 - 动态工厂Bean 例子
     */
    @Test
    public void test05() {
        // 创建容器
        ApplicationContext ac = new ClassPathXmlApplicationContext("applicationContext.xml");

        // 较 test04() 没有了工厂
        // 动态工厂Bean将测试类与工厂的耦合问题解决了
        ISomeService service = (SomeServiceImpl)ac.getBean("someServiceByFactory");
        service.doSome();
    }

    /**
     * Bean的装配 - 静态工厂Bean 例子
     */
    @Test
    public void test06() {
        // 创建容器
        ApplicationContext ac = new ClassPathXmlApplicationContext("applicationContext.xml");

        ISomeService service = (SomeServiceImpl)ac.getBean("someServiceByFactoryStatic");
        service.doSome();
    }

    /**
     *
     */
    @Test
    public void test07() {
        // 创建容器
        ApplicationContext ac = new ClassPathXmlApplicationContext("applicationContext.xml");

        Student student = (Student)ac.getBean("student");
        System.out.println(student);

        Teacher teacher = (Teacher)ac.getBean("teacher");
        System.out.println(teacher);
    }
}
