#### 安装 Hadoop

##### 过程
```

```

##### Trouble
```
很多人按照网上的各类教程搭建hadoop，但经常在安装好了后，启动hadoop时出现各类的错误，本文就“Error:JAVA_HOME is not set and could not be found ”这一错误提出解决办法。

针对这个错误，网上好多都说了java的路径设置有问题，但没有指出具体的修改方法，其实是hadoop里面hadoop-env.sh文件里面的java路径设置不对，hadoop-env.sh在hadoop/etc/hadoop目录下，具体的修改办法如下：

sudo vim hadoop/etc/hadoop/hdoop-env.sh

将语句      export JAVA_HOME=$JAVA_HOME     

修改为      export JAVA_HOME=/usr/java/jdk1.8.0_101

保存后退出。
```

```
Hive能正常执行任务，但出现“WARN: Establishing SSL connection without server’s identity verification is not recommended.”告警，翻译过来就是“不建议不使用服务器身份验证建立SSL连接。”

根据告警提示有两种解决方法：

1.设置useSSL=false 
这里有个坑就是hive的配置文件是.XML格式，而在xml文件中&amp；才表示&，所以正确的做法是在Hive的配置文件中，如hive-site.xml进行如下设置

  <property>
    <name>javax.jdo.option.ConnectionURL</name>
    <value>jdbc:mysql://localhost:3306/hive?createDatabaseIfNotExist=true&amp;useSSL=false</value>
    <description>JDBC connect string for a JDBC metastore</description>
  </property>
```

```
配置hive的坑 hive-site.xml:2787:3: The element type "configuration" must be terminated by the matching

解决方案
line 2783后面，官方模板缺少一个

<property>
```

```
 <!--开头和结尾，一定不要忘记-->
 <configuration>
 <property>
 <name>javax.jdo.option.ConnectionURL</name>
 <!--自己的主机名称或者localhost-->
 <value>jdbc:mysql://主机名称:3306/hive?createDatabaseIfNotExist=true</value>
 </property>
 <property>
 <name>javax.jdo.option.ConnectionDriverName</name>
 <value>com.mysql.jdbc.Driver</value>
 </property>
 <property>
 <name>javax.jdo.option.ConnectionUserName</name>
 <!--mysql的账号-->
 <value>root</value>
 </property>
 <property>
 <name>javax.jdo.option.ConnectionPassword</name>
 <!--自己mysql的密码哦-->
 <value></value>
 </property>
 </configuration>
```
