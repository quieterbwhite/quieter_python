# 06 - hbase集群搭建

```shell
1，上传hbase安装包到dp-hadoop5上，并解压到目录：/bigdata中

2，拷贝hadoop的配置文件：core-site.xml,hdfs-site.xml到/bigdata/hbase-1.3.3/conf

3，vim /bigdata/hbase-1.3.3/conf/hbase-site.xml

内容为：

<configuration>
<!-- 指定hbase在HDFS上存储的路径 -->
<property>
<name>hbase.rootdir</name>
<value>hdfs://dp/hbase</value>
</property>
<!-- 指定hbase是分布式的 -->
<property>
<name>hbase.cluster.distributed</name>
<value>true</value>
</property>
<!-- 指定zk的地址，多个用“,”分割 -->
<property>
<name>hbase.zookeeper.quorum</name>
<value>172.16.0.83:2181,172.16.0.84:2181,172.16.0.85:2181</value>
</property>

<property>
<name>hbase.master.info.port</name>
<value>60010</value>
</property>

<!--zk超时后重启regionserver-->

<property>
<name>hbase.regionserver.restart.on.zk.expire</name>
<value>true</value>
</property>


</configuration>



4，vim /bigdata/hbase-1.3.3/conf/regionservers 

添加内容为：

172.16.0.83
172.16.0.84
172.16.0.85

5，将修改好的安装包拷贝的dp-hadoop4,dp-hadoop5中

6，启动hbase,执行命令： /bigdata/hbase-1.3.3/bin/start-hbase.sh

启动成功后可通过：http://172.16.0.85:60010/master-status 查看hbase相关信息
```



 