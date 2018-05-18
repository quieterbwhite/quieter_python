package com.mmall.util;

import org.apache.commons.lang3.StringUtils;

/**
 * Created by bwhite on 18-5-18.
 */
public class LevelUtil {

    public final static String SEPARATOR = ".";

    public final static String ROOT = "0";

    // 0
    // 0.1
    // 0.1.2
    // 0.1.3
    // 0.4
    public static String calculateLevel(String parentLevel, int parentId) {
        if (StringUtils.isBlank(parentLevel)) {
            // 首层
            return ROOT;
        } else {
            return StringUtils.join(parentLevel, SEPARATOR, parentId);
        }
    }
}
