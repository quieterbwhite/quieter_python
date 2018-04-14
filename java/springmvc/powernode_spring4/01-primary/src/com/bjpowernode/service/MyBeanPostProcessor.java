package com.bjpowernode.service;

import org.springframework.beans.BeansException;
import org.springframework.beans.factory.config.BeanPostProcessor;

import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;
import java.lang.reflect.Proxy;

/**
 * Created by bwhite on 2016/12/3.
 */
public class MyBeanPostProcessor implements BeanPostProcessor {

    // bean: 当前正在初始化的Bean
    // beanName: 当前正在被初始化的bean的id
    // 在其他Bean的所有属性均被初始化完毕之 前 执行该方法
    @Override
    public Object postProcessBeforeInitialization(Object bean, String beanName) throws BeansException {
        System.out.println("postProcessBeforeInitialization 执行Bean后处理器的 before 方法");
        return bean;
    }

    // 在其他Bean的所有属性均被初始化完毕之 后 执行该方法
    @Override
    public Object postProcessAfterInitialization(Object bean, String beanName) throws BeansException {

        System.out.println("postProcessAfterInitialization 执行Bean后处理器的 after 方法");

        // 可以在这里对符合条件的 对象实例化 进行特殊处理
        if("someService1".equals(beanName)) {

            // TODO 没懂
            // 使用动态代理来对 bean 来做特殊处理
            Object serviceProxy = (ISomeService)Proxy.newProxyInstance(
                    bean.getClass().getClassLoader(),
                    bean.getClass().getInterfaces(),
                    new InvocationHandler() {
                        @Override
                        public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {

                            Object result = method.invoke(bean, args);
                            // return 的是目标方法的计算结果
                            return ((String)result).toUpperCase();
                        }
                    }
            );
            return serviceProxy;
        }
        return bean;
    }
}
