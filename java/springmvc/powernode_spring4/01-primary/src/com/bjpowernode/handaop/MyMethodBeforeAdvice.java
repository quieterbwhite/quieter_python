package com.bjpowernode.handaop;

import org.springframework.aop.MethodBeforeAdvice;

import java.lang.reflect.Method;

/**
 * Created by bwhite on 18-4-21.
 * 前置通知, 在目标方法之前执行
 */
public class MyMethodBeforeAdvice implements MethodBeforeAdvice {

    @Override
    public void before(Method method, Object[] objects, Object o) throws Throwable {
        System.out.println("目标方法执行之前, 对目标对象的增强代码就是写在这里的");
    }
}
