#### MVN 命令

##### 手动安装jar包到本地仓库中
```
mvn install:install-file -Dfile=d:\setup\dubbo-2.8.4.jar -DgroupId=com.alibaba -DartifactId=dubbo -Dversion=2.8.4 -Dpackaging=jar

mvn install:install-file -DgroupId=org.csource.fastdfs -DartifactId=fastdfs -Dversion=1.2 -Dpackaging=jar -Dfile=/home/bwhite/Download/fastdfs-1.2.jar
```
