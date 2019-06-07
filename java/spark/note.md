#### spark 日志清晰项目笔记

##### hadoop&hdfs 环境搭建
```
参考搭建单机环境官方文档:
http://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/SingleCluster.html

1. 安装jdk环境
2. 下载hadoop安装包 http://archive.cloudera.com/cdh5/cdh/5/
3. hadoop-env.sh 修改
4. core-site.xml 修改
5. hdfs-site.xml 修改
6. 格式化hdfs,只需安装时执行一次
7. 起停hdfs

cd /home/bwhite/software/hadoop-2.5.0-cdh5.3.6/etc/hadoop

hadoop-env.sh 修改

    export JAVA_HOME=/home/bwhite/software/jdk1.8.0_131

core-site.xml 修改
    
    <configuration>
        <property>
            <name>fs.defaultFS</name>
            <value>hdfs://localhost:9000</value>
        </property>
        
        <property>
            <name>hadoop.tmp.dir</name>
            <value>/home/bwhite/data/tmp</value>
        </property>
    </configuration>
    
hdfs-site.xml 修改

    <configuration>
        <property>
            <name>dfs.name.dir</name>
            <value>/home/bwhite/data/hadoop/namenode</value>
        </property>

        <property>
            <name>dfs.data.dir</name>
            <value>/home/bwhite/data/hadoop/datanode</value>
        </property>

        <property>
            <name>dfs.tmp.dir</name>
            <value>/home/bwhite/data/hadoop/tmp</value>
        </property>

        <property> 副本的数量
            <name>dfs.replication</name>
            <value>1</value>
        </property>

    </configuration>

格式化hdfs,只需安装时执行一次

    cd /home/bwhite/software/hadoop-2.5.0-cdh5.3.6/bin

    $ bin/hdfs namenode -format

开启hdfs

    cd /home/bwhite/software/hadoop-2.5.0-cdh5.3.6/sbin

    $ ./start-dfs.sh 
        19/06/07 17:00:18 WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
        Starting namenodes on [localhost]
        bwhite@localhost's password: 
        localhost: starting namenode, logging to /home/bwhite/software/hadoop-2.5.0-cdh5.3.6/logs/hadoop-bwhite-namenode-os.out
        bwhite@localhost's password: 
        localhost: starting datanode, logging to /home/bwhite/software/hadoop-2.5.0-cdh5.3.6/logs/hadoop-bwhite-datanode-os.out
        Starting secondary namenodes [0.0.0.0]
        bwhite@0.0.0.0's password: 
        0.0.0.0: starting secondarynamenode, logging to /home/bwhite/software/hadoop-2.5.0-cdh5.3.6/logs/hadoop-bwhite-secondarynamenode-os.out
        19/06/07 17:00:42 WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable

    $ jps
        11617 Jps
        11495 SecondaryNameNode
        11161 NameNode
        11309 
        
    浏览器访问 http://localhost:50070

    查看文件系统
    $ hadoop fs -ls /
        19/06/07 17:05:29 WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
        Found 2 items
        drwxr-xr-x   - bwhite supergroup          0 2019-05-31 22:28 /home
        -rw-r--r--   1 bwhite supergroup       1859 2019-06-01 17:46 /spark.txt

停止hdfs

    $ ./stop-dfs.sh
```
