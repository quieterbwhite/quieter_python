package com.j2se.lesson6;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;

/**
 * Created by bwhite on 2017/10/6.
 */
public class MapTest3 {

    public static void main(String[] args) {
        HashMap map = new HashMap();

        map.put("a", "zhangsan");
        map.put("b", "lisi");

        Set set = map.entrySet();

        for (Iterator iter = set.iterator(); iter.hasNext();) {
            Map.Entry entry = (Map.Entry)iter.next();

            String key = (String)entry.getKey();
            String value = (String)entry.getValue();

            System.out.println(key + " : " + value);
        }
    }
}
