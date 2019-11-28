# 05 - hive安装及使用

```shell
1，将hive安装包：apache-hive-2.3.5-bin.tar.gz，上传到dp-hadoop3中，并解压到目录/bigdata中

2，修改hive配置文件

vim /bigdata/hive-2.3.5/conf/hive-env.sh

添加内容为：

HADOOP_HOME=/bigdata/hadoop-2.6.4/

export HIVE_CONF_DIR=/bigdata/hive-2.3.5/conf/

修改hive-site.xml配置文件，内容如下：



<configuration>
<!-- WARNING!!! This file is auto generated for documentation purposes ONLY! -->
<!-- WARNING!!! Any changes you make to this file will be ignored by Hive. -->
<!-- WARNING!!! You must make your changes in hive-site.xml instead. -->
<!-- Hive Execution Parameters -->
  <property>
                        <name>javax.jdo.option.ConnectionURL</name>
                        <value>jdbc:mysql://192.168.56.101:3306/hive?createDatabaseIfNotExist=true</value>  
                </property>
                <property>
                        <name>javax.jdo.option.ConnectionDriverName</name>                       
                        <value>com.mysql.jdbc.Driver</value>
                </property>
                <property>
                       <name>javax.jdo.option.ConnectionUserName</name>
                       <value>root</value>
                </property>
                <property>
                      <name>javax.jdo.option.ConnectionPassword</name>                     
                      <value>111111</value>
                </property>
                  <property>
                          <name>hive.execution.engine</name>
                          <value>spark</value>
                  </property>

         <!--hive中spark的相关配置-->        

             <property>
                    <name>spark.home</name>
                    <value>/home/xieq/bigdata/spark-2.0.0-bin-hadoop2-without-hive/</value>
              </property>

 

           <!--也可以在spark default中设置-->        

             <property>
                    <name>spark.master</name>
                    <value>spark://hadoop1:7077</value>
              </property>

              <property>
                     <name>spark.eventLog.enabled</name>
                     <value>true</value>
             </property>

             <property>
                   <name>spark.eventLog.dir</name>
                   <value>hdfs://ns1/spark/spark-log</value>
              <description>必须要有这个目录</description>
             </property>
             <property>
                 <name>spark.executor.memory</name>
                 <value>1g</value>
              </property>
               <property>
                   <name>spark.driver.memory</name>
                    <value>1g</value>
                </property>
                <property>
                     <name>spark.serializer</name>
                     <value>org.apache.spark.serializer.KryoSerializer</value>
                </property>

<!--把spark jars下的jar包上传到hdfs上，yarn模式下减少集群间的分发-->  
                 <property>
                       <name>spark.yarn.jars</name>
                       <value>hdfs://ns1/spark-jars/*</value>
                    </property>
<property>
<name>hive.metastore.schema.verification</name>
<value>false</value>
</property>

                </property>

<!--把spark jars下的jar包上传到hdfs上，yarn模式下减少集群间的分发-->  
                 <property>
                       <name>spark.yarn.jars</name>
                       <value>hdfs://ns1/spark-jars/*</value>
                    </property>
<property>
<name>hive.metastore.schema.verification</name>
<value>false</value>
</property>



<!--一下为hive事务相关配置-->  

<property>

<name>hive.support.concurrency</name>

<value>true</value>

</property>

<property>

<name>hive.exec.dynamic.partition.mode</name>

<value>nonstrict</value>

</property>

<property>

<name>hive.txn.manager</name>

<value>org.apache.hadoop.hive.ql.lockmgr.DbTxnManager</value>

</property>

<property>

<name>hive.compactor.initiator.on</name>

<value>true</value>

</property>

<property>

<name>hive.compactor.worker.threads</name>

<value>1</value>

</property>
</configuration>

3，修改环境变量 vim /etc/profile

添加内容为：

export JAVA_HOME=/bigdata/jdk1.8.0_191/

export HADOOP_HOME=/bigdata/hadoop-2.6.4/

export HIVE_HOME=/bigdata/hive-2.3.5/

export PATH=$PATH:$JAVA_HOME/bin:$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$HIVE_HOME/bin



初始化元数据库：

./schematool -initSchema -dbType mysql

source /etc/profile

4，后台启动hiveserver2 ,执行如下命令：
nohup /bigdata/hive-2.3.5/bin/hiveserver2 &
5,启动hive客户端
/bigdata/hive-2.3.5/bin/beeline -u jdbc:hive2://
6.后台启动metastore
nohup /bigdata/hive-2.3.5/bin/hive --servcie metastore

将hive中的数导出为本地文件
 insert overwrite  local directory '/root/shixin-data' row format delimited fields terminated by ',' select data from ods_shixin where ct='2019-07-13';

若运行mr时内存不够可通过如下方式设置：
在运行hive sql前加上 ： （map） set mapreduce.map.memory.mb=2048 或者 （reduce） set mapreduce.reduce.memory.mb=2048

分组求top得使用

insert into table dw_shixin_new partition (ct="2019-07-13") select id,name,code_num,case_code,age,sexy,gist_id,business_entity,court,area,reg_date,gist_unit,duty,performance,disrupt_type_name,publish_date,ct from (select id,name,code_num,case_code,age,sexy,gist_id,business_entity,court,area,reg_date,gist_unit,duty,performance,disrupt_type_name,publish_date,ct,row_number() over (partition by code_num,case_code order by code_num desc) p_num from dw_shixin where ct='2019-07-13') a where a.p_num =1;
```

