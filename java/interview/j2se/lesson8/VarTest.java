package com.j2se.lesson8;

/**
 * Created by bwhite on 2017/10/6.
 */
public class VarTest {

    private static int sum(int... nums) {
        int sum = 0;

        for (int num : nums) {
            sum += num;
        }

        return sum;
    }

    public static void main(String[] args) {
        int result = VarTest.sum(1, 2);

        System.out.println(result);
    }
}
