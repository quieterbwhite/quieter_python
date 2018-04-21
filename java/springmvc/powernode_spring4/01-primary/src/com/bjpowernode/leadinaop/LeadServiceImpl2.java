package com.bjpowernode.leadinaop;

/**
 * Created by bwhite on 18-4-21.
 * 版本2， 用方法包装
 */
public class LeadServiceImpl2 implements ILeadService {

    @Override
    public void doSome() {
        doTransaction();
        System.out.println("LeadService2 - doSome");
        doLog();
    }

    @Override
    public String doSecond() {
        doTransaction();
        System.out.println("LeadService2 - doSecond");
        doLog();
        return null;
    }

    private void doTransaction() {
        System.out.println("open transaction");
    }

    private void doLog() {
        System.out.println("print log");
    }
}
