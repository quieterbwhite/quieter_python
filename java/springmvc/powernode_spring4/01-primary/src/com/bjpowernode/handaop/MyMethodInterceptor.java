package com.bjpowernode.handaop;

import org.aopalliance.intercept.MethodInterceptor;
import org.aopalliance.intercept.MethodInvocation;

/**
 * Created by bwhite on 18-4-21.
 * 环绕通知
 */
public class MyMethodInterceptor implements MethodInterceptor {

    @Override
    public Object invoke(MethodInvocation methodInvocation) throws Throwable {

        System.out.println("目标方法执行之前");
        // 调用目标方法
        Object result = methodInvocation.proceed();
        System.out.println("目标方法执行之后");

        if (result != null) {
            System.out.println("修改结果值");
        }

        return result;

    }
}
