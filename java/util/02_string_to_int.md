#### String to Int



**int -> String**

int i=12345;
String s="";
第一种方法：s=i+"";
第二种方法：s=String.valueOf(i);
这两种方法有什么区别呢？作用是不是一样的呢？是不是在任何下都能互换呢？

**String -> int**

s="12345";
int i;
第一种方法：i=Integer.parseInt(s);
第二种方法：i=Integer.valueOf(s).intValue();
这两种方法有什么区别呢？作用是不是一样的呢？是不是在任何下都能互换呢？

**以下是答案：**

第一种方法：s=i+"";   //会产生两个String对象
第二种方法：s=String.valueOf(i); //直接使用String类的静态方法，只产生一个对象

第一种方法：i=Integer.parseInt(s);//直接使用静态方法，不会产生多余的对象，但会抛出异常
第二种方法：i=Integer.valueOf(s).intValue();//Integer.valueOf(s) 相当于 new Integer(Integer.parseInt(s))，也会抛异常，但会多产生一个对象