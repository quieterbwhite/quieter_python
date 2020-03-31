package com.j2se.lesson3;

/**
 * Created by bwhite on 2017/8/20.
 */
public class EqualsTest {

    public static void main(String[] args) {

        Student s1 = new Student("tiger");
        Student s2 = new Student("tiger");

        // 对比地址，两个对象地址不同，所以不相等
        System.out.println(s1 == s2);
        // 对象比较，equals方法继承自object(==), 没有重写equals方法的话，仍然使用的是 ==
        System.out.println(s1.equals(s2));

        System.out.println("============================");

        // new 就会创建新的对象, new 出来是在堆中
        // false
        String str = new String("aaa");
        // 创建了新对象
        String str2 = new String("aaa");
        System.out.println(str);
        System.out.println(str2);
        System.out.println(str == str2);

        System.out.println("============================");

        // true  字面值。字符串是常量，值不能改变。

        // 这种方式创建是在栈中
        // 在字符串池中查找"bbb", 此时没有 "bbb", 新建对象并str3指向它
        String str3 = "bbb";
        // 字符串池中查找 "bbb", 此时有 "bbb", 不在新建对象，str4也指向它
        String str4 = "bbb";
        // 所以两个指向的对象，地址是相同的
        System.out.println(str3 == str4);

        System.out.println("============================");

    }
}

class Student {

    String name;

    public Student(String name) {
        this.name = name;
    }

    @Override
    public boolean equals(Object obj) {
        if(obj == this) {
            return true;
        }

        if (obj instanceof Student) {
            Student student = (Student)obj;
            if(student.name.equals(this.name)) {
                return true;
            }
        }

        return false;
    }
}
