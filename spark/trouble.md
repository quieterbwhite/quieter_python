#### Spark Trouble Shooting



##### No implicits found for parameter evidence$6: Encoder[Unit]

[解决升级Spark2.0之后，DataFrame map操作报错](https://www.cnblogs.com/dongxiucai/p/10002697.html)

　　当我们在使用spark1.6的时候，当我们创建SQLContext读取一个文件之后,返回DataFrame类型的变量可以直接.map操作，不会报错。但是升级之后会包一个错误，如下：

　　报错：No implicits found for parameter evidence$6: Encoder[Unit]

　　　　![img](https://img2018.cnblogs.com/blog/1452644/201811/1452644-20181122173431724-166514985.png)

　　主要的错误原因为：　

```
　　******error: Unable to find encoder for type stored in a Dataset. Primitive types (Int, String, etc) and Product types (case classes) are supported by importing spark.implicits._ Support for serializing other types will be added in future releases. resDf_upd.map(row => {******
```

　　此时有三种解决方案：

　　第一种：

　　　　![img](https://img2018.cnblogs.com/blog/1452644/201811/1452644-20181122174044656-443652878.png)

　　然后大家发现不会在报错误了。

　　第二种：

　　![img](https://img2018.cnblogs.com/blog/1452644/201811/1452644-20181122174228339-1009463220.png)

　　这样也可以

　　第三种：

　　这种是最麻烦的一种，可以参考官网

　　![img](https://img2018.cnblogs.com/blog/1452644/201811/1452644-20181122174825928-1926669472.png)

　　官网上给的是让自定义一个 Encoders，然后下面是我根据官网的例子，写的样例：

　　![img](https://img2018.cnblogs.com/blog/1452644/201811/1452644-20181122175552915-2034167824.png)

　　可以看到，也是可以用的，但是相比较上面两个是非常的麻烦的，所以推荐第一种和第二种，强推第二种，简单。

　　说明：

　　　　以上代码中我用的是SparkSession创建的，当然也可以用SQLContext来创建，但是SQLContext已经过时，不再推荐。

　　　　若是在用SQLContext时，遇到以上错误，同理解决。

---

---



# Failed to execute goal net.alchim31.maven:scala-maven-plugin:3.2.2:testCompile问题解决

[达微](https://www.jianshu.com/u/c7e63930e97b)

2018.12.28 16:52 字数 575 阅读 1269评论 0喜欢 0

## **解决方法1**

## 转载：<http://www.cnblogs.com/war3blog/p/7864804.html>

在编译spark源码的时候老师报类似的错误然后在spark 文件夹下的pom.xml里加入如下依赖，源码编译就没有报错成功编译出来了

修改spark源码下的 pom.xml 文件

<dependency>

```
    <groupId>net.alchim31.maven</groupId>
```

<artifactId>scala-maven-plugin</artifactId>

<version>3.2.0</version></dependency>

## **解决方法2**

转载：<https://blog.csdn.net/Poppy_Evan/article/details/79895799>

### 问题概述

idea运行Scala代码时，出现Failed to execute goal org.scala-tools:maven-scala-plugin:2.15.2:compile(default) on Project DataFus

### 原因

idea里的Scala版本与Windows里的Scala版本不兼容

这是idea的Scala版本（在pom.xml文件里查看）

![img](https://upload-images.jianshu.io/upload_images/4594052-4113417a4617c540?imageMogr2/auto-orient/strip%7CimageView2/2/w/305/format/webp)

image

这是Windows里的Scala的版本

![img](https://upload-images.jianshu.io/upload_images/4594052-68cf852b831ed550?imageMogr2/auto-orient/strip%7CimageView2/2/w/548/format/webp)

image

这个情况说明是 idea里的版本高于Windows的，这就是错误原因

### 所以

Windows里的Scala版本必须高于idea的Scala版本

所以，解决方案就是：本地安装高版本的Scala 或者 安装低版本的idea

## **解决方法3**

pom.xml报下图中的错误，解决办法：在 plugins 的外层加标签

![img](https://upload-images.jianshu.io/upload_images/4594052-eeb81573586f6a91.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/714/format/webp)

image

[图片上传失败...(image-8cc282-1545987119744)]

这样maven+scala的项目就成功搭建了。

## **解决方法4**

scala项目maven的编译打包

有可能会遇到：

原因是mvn clean package默认只处理java源代码的编译、打包，而不管scala，所以编译时遇到Hello这个由scala语言编写的class，此时scala还没编译生成class，所以找不到相应的调用入口。

解决办法：

mvn clean scala:compile compile package

![img](https://upload-images.jianshu.io/upload_images/4594052-68c1aa0731e13461?imageMogr2/auto-orient/strip%7CimageView2/2/w/661/format/webp)

image

如上，在compile前加入scala:compile，这是maven-scala-plugin插件提供的选项，表示编译scala，这样一来，先编译scala，再编译java，最后打包，妥妥滴！