package com.example.demo;

import java.io.IOException;
import java.util.Properties;

/**
 * Created by bwhite on 2019/1/26.
 */
public class SingletonStaticBlock {

    public static final SingletonStaticBlock INSTANCE;
    private String info;

    static {

        // 获取到类加载器就可以加载类路径下面的资源，就是 src 目录下的文件资源
        try {
            Properties pro = new Properties();

            pro.load(SingletonStaticBlock.class.getClassLoader().getResourceAsStream("single.properties"));

            System.out.println(pro.getProperty("info"));
            INSTANCE = new SingletonStaticBlock(pro.getProperty("info"));
            // INSTANCE = new SingletonStaticBlock("test");
        } catch (IOException e) {
            // e.printStackTrace();
            // 改为下面这一行，变成运行时异常，失败的话，外部就知道
            throw new RuntimeException(e);
        }
    }

    private SingletonStaticBlock(String info){
        this.info = info;
    }

    @Override
    public String toString() {
        return "SingletonStaticBlock{" +
                "info='" + info + '\'' +
                '}';
    }

    public String getInfo() {
        return info;
    }

    public void setInfo(String info) {
        this.info = info;
    }
}
