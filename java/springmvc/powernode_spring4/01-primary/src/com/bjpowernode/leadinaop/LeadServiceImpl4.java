package com.bjpowernode.leadinaop;

/**
 * Created by bwhite on 18-4-21.
 * 版本4， 调用外部工具的静态方法
 * SomeUtils.java
 */
public class LeadServiceImpl4 implements ILeadService {

    @Override
    public void doSome() {
        SomeUtils.doTransaction();
        System.out.println("exe doSome()");
        SomeUtils.doLog();
    }

    @Override
    public String doSecond() {
        SomeUtils.doTransaction();
        System.out.println("exe doSecond()");
        SomeUtils.doLog();
        return null;
    }
}
