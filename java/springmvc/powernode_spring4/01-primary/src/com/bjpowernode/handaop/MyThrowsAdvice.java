package com.bjpowernode.handaop;

import org.springframework.aop.ThrowsAdvice;

/**
 * Created by bwhite on 18-4-21.
 * 切面
 * 异常处理通知
 */
public class MyThrowsAdvice implements ThrowsAdvice {

    // 若发生 UserNameException， 则该方法会被自动调用执行
    public void afterThrowing(UserNameException ex) {
        System.out.println("用户名异常， 异常信息: " + ex.getMessage());
    }

    // 若发生 PasswordException， 则该方法会被自动调用执行
    public void afterThrowing(PasswordException ex) {
        System.out.println("密码异常， 异常信息: " + ex.getMessage());
    }
}
