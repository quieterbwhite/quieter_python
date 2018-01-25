# gradle wrapper

## gradlew 主要作用
```
在本机没有安装gradle的前提下，依然可以通过一个简单的命令来构建gradle项目
```

## 使用
```
新建项目，构建项目方式使用推荐的方式，gradlew

配置文件: gradle-wrapper.properties


// 构建
./gradlew clean build

    自动从远程下载 gradle, 下载目录 /usr/bwhite/.gradle/wrapper/dists
```

## 修改 build.gradle
```
task wrapper(type: Wrapper) {
    gradleVersion = '3.4'
    distributionType = 'all'
}

执行命令:
gradle wrapper
```
