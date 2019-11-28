# 04 - spark集群搭建

```shell
1，上传spark-2.3.2-bin-hadoop2.6.tgz安装包到dp-hadoop1 /bigdata目录下

2，修改spark配置文件

 vim /bigdata/spark-2.3.3-bin-hadoop2.6/conf/spark-env.sh

添加如下内容：

export JAVA_HOME=/bigdata/jdk1.8.0_191/
export SPARK_MASTER=172.16.0.81
export SPARK_MASTER_PORT=7077
export SPARK_WORKER_CORES=2
export SPARK_WORKER_MEMORY=3g

 vim /bigdata/spark-2.3.3-bin-hadoop2.6/conf/slaves：

添加如下内容

172.16.0.81
172.16.0.82
172.16.0.83
172.16.0.84
172.16.0.85

3，将修改后的安装包拷贝到dp-hadoop2,dp-hadoop3,dp-hadoop4,dp-hadoop5的同目录中



4，在dp-hadoop1中执行如下命令启动spark集群：

 /bigdata/spark-2.3.3-bin-hadoop2.6/sbin/start-all.sh



启动成功后可通过：http://172.16.0.81:8080/ 查看spark集群信息
```



