package com.j2se.lesson7;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

/**
 * Created by bwhite on 2017/10/6.
 */
public class ArrayListTest {

    public static void main(String[] args) {

        // 泛型是字符串类型的，所以只能加字符串, 所以泛型的缺点不能添加各种类型的数据到list，但是程序不会做这种事情
        // 要是有不同类型的怎么办，用两个集合就可以了
        // 工作中使用集合一定要使用泛型
        List<String> list = new ArrayList<String>();

        list.add("a");
        list.add("b");
        list.add("c");

        for (int i = 0; i < list.size(); i++) {
            String value = list.get(i);
            System.out.println(value);
        }

        // 迭代器也指定好泛型，也就不再需要向下类型转换
        for (Iterator<String> iter = list.iterator(); iter.hasNext();) {
            String value = iter.next();
            System.out.println(value);
        }

    }
}
