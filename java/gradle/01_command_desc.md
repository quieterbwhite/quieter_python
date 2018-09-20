#### gradle 命令解释

```
* gradle clean build

    构建，每次构建生成.gradle文件夹，生成build文件夹，并在 build/libs/ 下生成项目jar包

* gradle 安装的包路径

    /home/bwhite/.gradle/caches/modules-2/files-2.1

    构建的时候gradle把这个目录下需要的jar包打包到war包中
```

##### 修改项目源为aliyun
```
在 project-level 的 build.gradle中修改如下：

allprojects {
    repositories {
        //jcenter()
        //maven{ url 'http://maven.oschina.net/content/groups/public/'}
        maven{ url 'http://maven.aliyun.com/nexus/content/groups/public/'}
    }
}
```
