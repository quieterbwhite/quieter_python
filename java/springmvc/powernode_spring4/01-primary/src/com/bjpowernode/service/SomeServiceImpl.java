package com.bjpowernode.service;

/**
 * Created by bwhite on 2016/12/3.
 */
public class SomeServiceImpl implements ISomeService {

    /**
     * 创建无参构造器用于观察对象什么时候初始化
     */
    public SomeServiceImpl() {
        System.out.println("正在创建 SomeServiceImpl 对象");
    }

    /**
     * 测试用的方法
     */
    @Override
    public void doSome() {
        System.out.println("执行 doSome. ");
    }
}
