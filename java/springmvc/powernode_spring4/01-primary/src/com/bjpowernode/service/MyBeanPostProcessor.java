package com.bjpowernode.service;

import org.springframework.beans.BeansException;
import org.springframework.beans.factory.config.BeanPostProcessor;

/**
 * Created by bwhite on 2016/12/3.
 */
public class MyBeanPostProcessor implements BeanPostProcessor {
    @Override
    public Object postProcessBeforeInitialization(Object o, String s) throws BeansException {
        System.out.println("postProcessBeforeInitialization 执行Bean后处理器的 before 方法");
        return o;
    }

    @Override
    public Object postProcessAfterInitialization(Object bean, String beanName) throws BeansException {
        System.out.println("postProcessAfterInitialization 执行Bean后处理器的 after 方法");

        // 可以在这里对符合条件的 对象实例化 进行特殊处理
        if("someService1".equals(beanName)) {
            // 使用动态代理来对 bean 来做特殊处理
            return bean;
        }
        return bean;
    }
}
