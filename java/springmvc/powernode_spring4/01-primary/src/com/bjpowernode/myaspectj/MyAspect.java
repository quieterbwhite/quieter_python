package com.bjpowernode.myaspectj;

import org.aspectj.lang.JoinPoint;
import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.*;

/**
 * Created by bwhite on 18-4-30.
 * 定义切面
 */
@Aspect  // 表示当前POJO类为切面
public class MyAspect {

//    @Before("doSomePointCut()")
    @Before("execution(* *..myaspectj.*.doSome(..))")
    public void myBefore(JoinPoint joinPoint) {
        System.out.println(">>>>>>执行前置通知 jp+" + joinPoint);
    }

    @AfterReturning(value = "execution(* *..myaspectj.*.doAnother(..))", returning = "result")
    public void myAfter(Object result) {
        System.out.println("MyAspect - myAfter");
    }

    @Around("execution(* *..myaspectj.*.doAnother(..))")
    public Object myAround(ProceedingJoinPoint proceedingJoinPoint) throws Throwable {

        System.out.println("before");

        // 执行目标方法
        Object result = proceedingJoinPoint.proceed();

        // 可以这样改变返回值，但是代码健壮性不够, 多个不同的方法时就可能会出现空指针异常
        if (result != null) {
            result = ((String)result).toUpperCase();
        }

        System.out.println("after");

        return result;
    }

    @AfterThrowing(value = "execution(* *..myaspectj.*.doAnother(..))", throwing = "ex")
    public void myException(Exception ex) {
        System.out.println("myException ex=" + ex.getMessage());
    }

    // 最终通知
    @After("execution(* *..myaspectj.*.doAnother(..))")
    public void finalAfter() {
        System.out.println("finalAfter - 最终通知");
    }

    // 抽取出来切入点
    @Pointcut("execution(* *..myaspectj.*.doAnother(..))")
    public void doSomePointCut() {}
}
