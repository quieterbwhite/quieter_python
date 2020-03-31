# readme_L08_装箱_枚举_反射

增强的for循环
```java
Collection<String> col = new ArrayList<String>();
col.add("a");
col.add("b");
col.add("c");

for (String str : col) {
    System.out.println(str);
}
```

```
自动装箱拆箱
    int a = 3;
    Collection<Integer> c = new ArrayList<Integer>();
    // 将int类型的3转换为Integer类型并放到集合中
    c.add(3);
    c.add(a + 3);
    for (Integer i : c) {
        System.out.println(i);
    }
```

```
Integer 类有一个缓存，它会缓存介于 -128-127之间的整数
Python中也有小整数缓存
```

```
可变参数

    private static int sum(int... nums) {
        int sum = 0;

        for (int num : nums) {
            sum += num;
        }

        return sum;
    }

可变参数实际就是数组，也可以照数组方式传值

可变参数必须放在所有参数末尾,且只能有一个
```

Enums 枚举
```
定义枚举类型时本质上就是在定义一个类别
只不过很多细节由编译器帮助完成了
所以某种程度上，enum关键字的作用就像class或interface

我们所定义的每个枚举类型都继承自java.lang.Enum类，
枚举中的每个成员默认都是 public static final 的。

而每个枚举的成员其实就是定义的枚举类型的一个实例（instance）
换句话说
当定义一个枚举类型后，在编译时刻就能确定该枚举类型有几个实例，分别是什么。
在运行期间我们无法再使用该枚举类型创建新的实例了
这些实例在编译期间就已经完全确定下来
```

##### 枚举替换常量
比如在传参的时候，常量可以是任何值。枚举就只能是指定值。  
缩小可传参数范围，增强健壮性。  
```java
package com.shengsiyuan.jdk5;

public class AccessControl {

    public static boolean checkRight(AccessRight accessRight) {
        
        if(accessRight == AccessRight.MANAGER) {
            return true;
        } else if(accessRight == AccessRight.DEPARTMENT) {
            return false;
        } else{
            return false;
        }
    }

    public static void main(String[] args) {
        AccessRight accessRight = AccessRight.valueOf("MANAGER");
        Systemout.out.println(checkRight(accessRight));
    }
}
```

```
反射

在运行时判断任意一个对象所属的类
在运行时构造任意一个类的对象
在运行时判断任意一个类所具有的成员变量和方法
在运行时调用任意一个对象的方法

也就是自省，在运行期所做的类似动态语言的行为。看透class的能力

java.lang.reflect 包下面的类，实现反射机制
```

```
Java里面无论生成多少个对象，这些对象都会对应class，还可以通过class
探知其有哪些对象
java中，无论生成某个类的多少个对象，这些对象都会对应同一个class对象
```
