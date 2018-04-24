package com.bjpowernode.leadinaop;

/**
 * Created by bwhite on 18-4-21.
 * 用动态代理实现 系统级业务 插入 主业务
 */
// 目标类
public class LeadServiceImpl5 implements ILeadService {

    // 目标方法
    @Override
    public void doSome() {
        System.out.println("exe doSome()");
    }

    // 目标方法
    @Override
    public String doSecond() {
        System.out.println("exe doSecond()");
        return null;
    }
}
