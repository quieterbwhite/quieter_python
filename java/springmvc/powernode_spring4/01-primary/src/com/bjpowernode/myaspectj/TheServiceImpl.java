package com.bjpowernode.myaspectj;

/**
 * Created by bwhite on 18-4-30.
 */
public class TheServiceImpl implements ITheService {

    @Override
    public void doSome() {
        System.out.println("MyAspect - TheServiceImpl - doSome");
    }

    @Override
    public String doAnother() {
        return "hah";
    }
}
