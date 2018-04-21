package com.bjpowernode.annotationdi;

import org.springframework.beans.factory.annotation.Autowire;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/**
 * Created by bwhite on 18-4-21.
 * 相当于 Spring 的配置文件
 */
@Configuration  // 表明当前POJO类将会被当做配置文件使用, 即Spring容器
public class JavaConfig {

    @Bean(name = "myHouse")   // 表明当前方法的返回值为一个Bean对象
    public House myHouseCreator() {
        return new House("野鸡大学");
    }

    @Bean(name = "myAnimal", autowire = Autowire.BY_TYPE)  // byType 方式自动注入
    public Animal myAnimalCreator() {
        return new Animal("hah", 26);
    }
}
