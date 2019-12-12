# 搭建 java 环境

## 目录
```
1. java环境
2. tomcat
3. gradle
```

## 配置环境变量
```
export JAVA_HOME=/home/bwhite/software/jdk1.8.0_231
export CLASSPATH=$:CLASSPATH:$JAVA_HOME/lib/
export PATH=$PATH:$JAVA_HOME/bin

export M2_HOME=/home/bwhite/software/apache-maven-3.6.3
export CLASSPATH=$CLASSPATH:$M2_HOME/lib
export PATH=$PATH:$M2_HOME/bin

export NODE_HOME=/home/bwhite/software/node-v6.11.5-linux-x64
export PATH=$NODE_HOME/bin:$PATH
```


##搭建java环境
```
http://www.runoob.com/java/java-environment-setup.html

官网下载安装包：
http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html

其实tar.gz解压就是安装，只要解压到既定目录，然后配置正确就行。

* 配置环境变量

    编辑 ~/.bashrc 文件

    JAVA_HOME=/opt/jdk1.8.0_112
    PATH=$JAVA_HOME/bin:$JAVA_HOME/jre/bin:$PATH
    CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar:$JAVA_HOME/lib:$JAVA_HOME/jre/lib:$JAVA_HOME/jre/lib/rt.jar:$CLASSPATH

    或者:

    export JAVA_HOME=/home/bwhite/software/jdk1.8.0_231
    export CLASSPATH=$:CLASSPATH:$JAVA_HOME/lib/
    export PATH=$PATH:$JAVA_HOME/bin

    source ~/.bashrc

* 测试是否安装成功

    java -version

    test.java

    public class test {
        
        public static void main(String args[]) {
            System.out.println("A new jdk test!");
        }
    }

    javac test.java
    java test.class

    print "A new jdk test!"
```

## 安装tomcat
```
下载安装包  apache-tomcat-8.5.8.tar.gz
解压到 /opt/apache-tomcat-8.5.8

# InteliJ Idea 需要权限
sudo chmod 777 -R /opt/apache-tomcat-8.5.8

编辑 /bin/startup.sh 文件, 添加:

JAVA_HOME=/opt/jdk1.8.0_112
JRE_HOME=${JAVA_HOME}/jre
PATH=$JAVA_HOME/bin:$PATH
CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
TOMCAT_HOME=/opt/apache-tomcat-8.5.8

exec "$PRGDIR"/"$EXECUTABLE" start "$@"

保存退出

测试是否安装成功:
sudo ./bin/startup.sh

输出:
Using CATALINA_BASE:   /opt/apache-tomcat-8.5.8
Using CATALINA_HOME:   /opt/apache-tomcat-8.5.8
Using CATALINA_TMPDIR: /opt/apache-tomcat-8.5.8/temp
Using JRE_HOME:        /opt/jdk1.8.0_112
Using CLASSPATH:       /opt/apache-tomcat-8.5.8/bin/bootstrap.jar:/opt/apache-tomcat-8.5.8/bin/tomcat-juli.jar
Tomcat started.

打开浏览器 http://localhost:8080 查看到tomcat 页面表示安装成功

关闭 tomcat
sudo ./bin/shutdown.sh

ps, 每次进到tomcat目录再输入 startup.sh 命令很繁琐。配置一个启动文件.

cd /etc/init.d/
vim tomcat

------------------------------------
cd /opt/apache-tomcat-8.5.8
#./bin/startup.sh
case "$1" in
start)
./bin/startup.sh
exit 1;;
stop)
./bin/shutdown.sh
exit 1;;
esac

:wq
-----------------------------------

sudo chmod 777 tomcat

# 启动 tomcat
sudo /etc/init.d/tomcat start
# 关闭 tomcat
sudo /etc/init.d/tomcat stop
```

## 安装 gradle
```
1、在官网下载最新的Gradle版本。http://www.gradle.org/downloads

2、解压安装包到目录     

3、打开环境文件  
 sudo vim /etc/profile

 4、写入环境变量:    
 export GRADLE_HOME=/opt/gradle/gradle-2.0 
 export PATH=$GRADLE_HOME/bin:$PATH
  
  5、环境变量生效source /etc/profile

  6、检查结果

  gradle -v
  
或者:

解压到 /opt/gradle-3.2
修改 文件 .bashrc
GRADLE_HOME=/opt/gradle-3.2
PATH=$GRADLE_HOME/bin:$PATH
:wq
source .bashrc
```


## 安装 google protobuf
```
下载 https://github.com/google/protobuf/releases
解压并配置环境变量即可

vim .bashrc

PROTOC_HOME=/home/bwhite/software/protoc-3.3.0-linux-x86_64
PATH=$PROTOC_HOME/bin:$PATH

:wq
source .bashrc
which protoc

可以下载语言对应的包 protobuf-java-3.3.0.zip

还要通过 maven/gradle 安装对应语言的工具包 Installation - With Maven
search.maven.org
    search for: 
	protobuf-java
	protobuf-java-util
```

