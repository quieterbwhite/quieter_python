package com.j2se.lesson15;

import java.io.*;

/**
 * Created by bwhite on 2017/10/8.
 */
public class SerializableTest1 {

    public static void main(String[] args) throws Exception {

        Person p1 = new Person("libo", 10, 99.9);
        Person p2 = new Person("spider", 90, 912.2);
        Person p3 = new Person("bob", 44, 32.2);

        FileOutputStream pos = new FileOutputStream("person.txt");

        ObjectOutputStream oos = new ObjectOutputStream(pos);

        // 会自动检查哪些能序列化,哪些不能
        // 写成二进制文件
        oos.writeObject(p1);
        oos.writeObject(p2);
        oos.writeObject(p3);

        oos.close();

        //////////////////////////////////

        FileInputStream fis = new FileInputStream("person.txt");
        ObjectInputStream ois = new ObjectInputStream(fis);

        Person p = null;

        for (int i = 0; i < 3; i++) {
            p = (Person)ois.readObject();
            System.out.println(p.age + "," + p.age + "," + p.height);
        }

        ois.close();

    }
}

/**
 * writeObject, readObject, 两个私有方法可以控制序列化和反序列化过程
 */
class Person implements Serializable {

    // 不会被序列化
    transient String name;

    int age;

    double height;

    public Person(String name, int age, double height) {
        this.age = age;
        this.name = name;
        this.height = height;
    }
}
