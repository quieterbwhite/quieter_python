package com.j2se.lesson10;

import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;

/**
 * Created by bwhite on 2017/10/7.
 */
// 默认值是 .CLASS, 会被编译到字节码文件，运行期并不能被反射获取到
@Retention(RetentionPolicy.RUNTIME)
public @interface MyAnnotation {

    String hello() default "nidaye";

    String world();


}
