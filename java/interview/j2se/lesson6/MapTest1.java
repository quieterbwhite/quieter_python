package com.j2se.lesson6;

import java.util.HashMap;

/**
 * Created by bwhite on 2017/10/6.
 */
public class MapTest1 {

    public static void main(String[] args) {
        HashMap map = new HashMap();

        map.put("a", "zhangsan");
        map.put("b", "lisi");
        map.put("c", "wangwu");

        System.out.println(map);

        String value = (String)map.get("b");
        System.out.println(value);
    }
}
