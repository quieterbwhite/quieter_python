# java SE Lesson 4

```
包装类(Wrapper Class)。针对原生数据类型的包装。所有的包装类(8个)都位于java.lang包下。
分别是: Byte, Short, Integer, Long, Float, Double, Character, Boolean
他们的使用方式是一样的，可以实现原生数据类型与包装类型的双向转换。
```

```
j2se.lesson4.ArrayTest.java

数组，Array, 相同类型数据的集合就叫数组

如何定义数组
    定义数组,并指定长度, 注意是通过 new 生成的数组，所以，数组是对象
    type[] 变量名 = new type[数组中元素的个数]; 如:
    int[] a = new int[10];

数组中的元素索引是从0开始的。对于数组来说，最大的索引==数组的长度-1
```

```
Java中的每个数组都有一个名为length的属性，表示数组的长度。
length属性是public，final，int的。数组长度一旦确定，就不能改变大小。
```

```
int[] a = new int[10], 其中a是一个引用，它指向了生成的数组对象的首地址，
数组中每个元素都是int类型，其中仅存放数据值本身。
```

```
j2se.lesson4.ArrayTest2.java
null指，这个引用不指向任何对象，但存在这个引用。

数组里面存的是对象的应用，对象在堆里面，是没办法直接操作的。
只能通过引用间接操作对象。数组里装的从来都是引用。
```

```
比较两个数组
需要使用 util 包下面的 Arrays 的静态方法。
Arrays.equals(a, b);
数组原生的比较方法是比较地址的不是比较内容的。
```

```
拷贝数组

int[] a = new int[]{1, 2, 3, 4};
int[] b = new int[4];

System.arraycopy(a, 0, b, 0, 4);
```
