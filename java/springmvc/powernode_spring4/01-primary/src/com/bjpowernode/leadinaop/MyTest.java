package com.bjpowernode.leadinaop;

import org.junit.Test;

import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;
import java.lang.reflect.Proxy;

/**
 * Created by bwhite on 18-4-21.
 */
public class MyTest {

    @Test
    public void test11() {
        ILeadService service = new LeadServiceImpl();
        service.doSome();
        service.doSecond();
    }

    @Test
    public void Test2() {
        ILeadService service = new LeadServiceImpl2();
        service.doSome();
        service.doSecond();
    }

    @Test
    public void test4() {
        ILeadService service4 = new LeadServiceImpl4();
        service4.doSome();
        service4.doSecond();
    }

    @Test
    public void test5() {

        final ILeadService target = new LeadServiceImpl5();

        ILeadService proxy = (ILeadService)Proxy.newProxyInstance(
                target.getClass().getClassLoader(),// 类加载器
                target.getClass().getInterfaces(), // 他妈的，看书没啥用，实际写一次就明白了
                new InvocationHandler() {

                    // AOP 的工作原理, 底层用的也是代理
                    // 有接口用动态代理，没接口用 CGLIB 代理
                    // 织入，工具类业务切入到主业务中, 就是在这里完成的
                    @Override
                    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {

                        SomeUtils.doTransaction();
                        Object result = method.invoke(target, args);
                        SomeUtils.doLog();

                        return result;
                    }
                }
        );


        proxy.doSome();
        proxy.doSecond();
    }
}
