package com.bjpowernode.leadinaop;

/**
 * Created by bwhite on 18-4-21.
 * 版本1， 硬编码
 */
public class LeadServiceImpl implements ILeadService {

    @Override
    public void doSome() {
        System.out.println("open transaction");
        System.out.println("exe doSome()");
        System.out.println("print log");
    }

    @Override
    public String doSecond() {
        System.out.println("open transaction");
        System.out.println("exe doSecond()");
        System.out.println("print log");
        return "china";
    }
}
