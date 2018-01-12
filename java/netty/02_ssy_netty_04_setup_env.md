# SSY Netty Class 04 项目环境搭建与环境配置

## 安装 gradle
[下载gradle](https://gradle.org/install/)
```
解压到 /home/bwhite/software/gradle-4.0.1

修改文件 .bashrc

	GRADLE_HOME=/home/bwhite/software/gradle-4.0.1
	PATH=$GRADLE_HOME/bin:$PATH
	:wq
	source .bashrc

测试

	$ gradle -v
```

## 创建 gradle 项目
```
创建基于 gradle 的 java 项目
```

## 项目结构
```
settings.gradle 文件基本不会改变，除非是项目用到多模块，那么会用include把其他模块引入进来。

对于 gradle 来说，最重要的是 build.gradle 文件。类似与 maven 中的 pom.xml 文件。

进行依赖管理，项目构建最为核心的文件。

build.gradle 解释:

    // 源码编译级别
    sourceCompatibility = 1.8

    // 目标编译级别, 需要新增
    targetCompatibility = 1.8

    // 修改仓库地址
    repositories {
        // mavenCentral()
        maven {
            url "http://maven.aliyun.com/nexus/content/groups/public"
        }
    }

    // 修改 dependencies 结构为更简洁的方式
    dependencies {
        testCompile (
            "junit:junit:4.12"
        )

        compile (
            "io.netty:netty-all:4.1.19.Final"
        )
    }

寻找包的坐标:

    search.maven.org

    如, 需要找 netty 的 gradle 描述。搜索 netty-all, 然后找需要的版本就行。


```
