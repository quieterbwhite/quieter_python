package com.j2se.lesson6;

import java.util.Comparator;
import java.util.TreeSet;

/**
 * Created by bwhite on 17-10-5.
 */
public class TreeSetTest2 {

    public static void main(String[] args) {
        TreeSet set = new TreeSet();

        Animal s1 = new Animal(10);
        Animal s2 = new Animal(20);
        Animal s3 = new Animal(30);

        set.add(s1);
        set.add(s2);
        set.add(s3);

        System.out.println(set);
    }

}

class Animal {
    
    int score;

    public Animal(int score) {
        this.score = score;
    }

    public String toString() {
        return String.valueOf(this.score);
    }

}

class AnimalComparator implements Comparator {
    @Override
    public int compare(Object o1, Object o2) {

        Animal ani1 = (Animal)o1;
        Animal ani2 = (Animal)o2;

        return ani1.score - ani2.score;
    }
}