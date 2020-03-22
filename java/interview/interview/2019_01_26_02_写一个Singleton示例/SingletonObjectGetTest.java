package com.example.demo;

import java.util.concurrent.*;

/**
 * 测试
 * 获取 SingletonDirect.INSTANCE
 * Created by bwhite on 2019/1/26.
 */
public class SingletonObjectGetTest {

    public static void main(String[] args) throws ExecutionException,InterruptedException {

        // 1 直接方式
        SingletonDirect singletonDirect = SingletonDirect.INSTANCE;
        System.out.println(singletonDirect);

        // 2 枚举类方式
        SingletonEnum singletonEnum = SingletonEnum.INSTANCE;
        System.out.println(singletonEnum);

        // 3 静态内部类方式
        // SingletonStaticBlock singletonStaticBlock = SingletonStaticBlock.INSTANCE;
        // System.out.println(singletonStaticBlock);

        // 4 普通延迟加载对象模式
        /*
        SingletonLazy singletonLazy = SingletonLazy.getSingletonLazy();
        SingletonLazy singletonLazy1 = SingletonLazy.getSingletonLazy();
        // 地址相同就是一个对象
        System.out.println(singletonLazy == singletonLazy1);
        System.out.println(singletonLazy);
        System.out.println(singletonLazy1);
        */

        // 4 多线程测试
        Callable<SingletonLazy> c = new Callable<SingletonLazy>() {
            @Override
            public SingletonLazy call() throws Exception {
                return SingletonLazy.getSingletonLazy();
            }
        };
        // 新建一个线程池
        ExecutorService es = Executors.newFixedThreadPool(2);
        // 提交任务
        Future<SingletonLazy> f1 = es.submit(c);
        Future<SingletonLazy> f2 = es.submit(c);

        SingletonLazy s1 = f1.get();
        SingletonLazy s2 = f2.get();

        System.out.println(s1 == s2);
        System.out.println(s1);
        System.out.println(s2);
        es.shutdown();

        // 5 增加同步锁
        Callable<SingletonLazySynchronized> d = new Callable<SingletonLazySynchronized>() {
            @Override
            public SingletonLazySynchronized call() throws Exception {
                return SingletonLazySynchronized.getSingletonLazy();
            }
        };
        // 新建一个线程池
        ExecutorService es2 = Executors.newFixedThreadPool(2);
        // 提交任务
        Future<SingletonLazySynchronized> h1 = es2.submit(d);
        Future<SingletonLazySynchronized> h2 = es2.submit(d);

        SingletonLazySynchronized x1 = h1.get();
        SingletonLazySynchronized x2 = h2.get();

        System.out.println(x1 == x2);
        System.out.println(x1);
        System.out.println(x2);
        es2.shutdown();

        // 6 测试 SingletonLazySynchronizedEfficient
    }
}
