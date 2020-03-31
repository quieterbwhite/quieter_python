package com.j2se.lesson6;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Set;

/**
 * Created by bwhite on 2017/10/6.
 */
public class MapTest2 {

    public static void main(String[] args) {

        HashMap map = new HashMap();

        map.put("a", "zhangsan");
        map.put("b", "zhangsan");

        System.out.println(map);

        //////////////////////////////

        // 遍历map
        Set set = map.keySet();
        for (Iterator iter = set.iterator(); iter.hasNext();) {
            String key = (String)iter.next();
            String value = (String)map.get(key);

            System.out.println(key + " = " + value);
        }

    }
}
