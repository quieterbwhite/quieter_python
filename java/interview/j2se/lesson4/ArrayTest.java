package com.j2se.lesson4;

/**
 * Created by bwhite on 2017/8/20.
 * Updated by bwhite on 2017/10/03
 */
public class ArrayTest {

    public static void main(String[] args) {

        // 定义数组,并指定长度, 注意是通过 new 生成的数组，所以，数组是对象
        int[] a = new int[4];

        a[0] = 1;
        a[1] = 2;
        a[2] = 3;
        a[3] = 4;

        System.out.println(a[3]);

        ///////////////////////////////////
        // 赋值方式2
        int[] b = {1, 2, 3, 4};
        System.out.println(b[3]);

        // 赋值方式3
        int[] c = new int[]{1, 2, 3, 4};
        System.out.println(c[3]);

        ///////////////////////////////////

        // array.length 数组的长度
        int[] d = new int[100];

        for (int i = 0; i < d.length; i++) {
            d[i] = i+1;
        }
        for (int j = 0; j < d.length; j++) {
            System.out.println(d[j]);
        }

        ////////////////////////////////////

        // 定义数组时不赋值。会给默认值。
        boolean[] e = new boolean[4];
        System.out.println(e[0]);

        ////////////////////////////////////

        // f是一个引用, 指向的是数组的首地址，f[0] 的地址，内存结构图是这样的, 连续的
        int[] f = {1, 2, 3};
        int[] g = {1, 2, 3};

        // 注意
        // 下面行结果是false, 对于数组内容的比较一定不要使用 equals() 方法
        // 因为是沿用 object 的 equals 方法，比较的是地址，不是内容本身, 这里是两个数组，地址是不同的
        System.out.println(f.equals(g));

        ////////////////////////////////////


    }


}
