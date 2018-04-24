package com.bjpowernode.handaop;

import org.springframework.aop.AfterReturningAdvice;

import java.lang.reflect.Method;

/**
 * Created by bwhite on 18-4-21.
 * 后置通知, 能获取到目标方法的返回值，但是不能改变
 */
public class MyAfterReturningAdvice implements AfterReturningAdvice {

    @Override
    public void afterReturning(Object returnValue, Method method, Object[] objects, Object o1) throws Throwable {

        System.out.println("目标方法执行之后，目标方法返回值为: " + returnValue);

        if (returnValue != null) {

        }

    }
}
