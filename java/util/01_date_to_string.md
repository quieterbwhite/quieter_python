#### 日期 - 字符串 转换

##### 日期转字符串

```java
package com.test.dateFormat;
 
import java.text.SimpleDateFormat;
import java.util.Date;
 
import org.junit.Test;
 
public class Date2String {
    @Test
    public void test() {
        Date date = new Date();
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");
        System.out.println(sdf.format(date));
        sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
        System.out.println(sdf.format(date));
        sdf = new SimpleDateFormat("yyyy年MM月dd日 HH:mm:ss");
        System.out.println(sdf.format(date));
    }
}

output:

2016-10-24
2016-10-24 21:59:06
2016年10月24日 21:59:06
```

##### 字符串转日期

```java
package com.test.dateFormat;
 
import java.text.ParseException;
import java.text.SimpleDateFormat;
 
import org.junit.Test;
 
public class String2Date {
    @Test
    public void test() throws ParseException {
        String string = "2016-10-24 21:59:06";
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
        System.out.println(sdf.parse(string));
    }
}

output:

Mon Oct 24 21:59:06 CST 2016
```

