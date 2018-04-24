package com.bjpowernode.annotationdi;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

/**
 * Created by bwhite on 18-4-21.
 */
@Component("myHouse")
public class House {

    @Value("爱的家园")
    private String name;

    public House() {
    }

    public House(String name) {
        this.name = name;
    }

    @Override
    public String toString() {
        return "House{" +
                "name='" + name + '\'' +
                '}';
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
