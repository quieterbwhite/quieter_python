#### Hbase 学习记录



##### 什么是Hbase

```shell
Google BigTable的开源实现

分布式数据库

列式存储

Nosql

基于HDFS和Zookeeper
```

##### 为什么使用Hbase

```shell
成熟
	社区成熟
	理论经过充分实践
	丰富的工具支持
	
高效
	将随机读写转化为顺序读写，适应高并发写入
	均衡效果好，读写性能和机器数保持线性相关
	行中没有保存数据的列不占存储空间
	
分布式特性，基于HDFS
	一致性，可用性，分区容忍性
	大数据存储
	易扩展
```

##### 如果正确使用Hbase

```shell
适用场景
	列族结构经常调整
	高并发写入
	结构化数据,半结构化存储
	key-value存储
	有序存储
	固定集合(多版本)
	定时删除记录(TTL)
	
不适用场景
	事务
	join, union, group by 等查询与计算
	不按rowkey查询数据
	高并发随机读写
```

##### Hbase基本架构

```shell
客户端
zookeeper
Master, Master
Resion Server, Region Server
HDFS
```

##### Hbase表基本结构

```shell
Row Key - Time Stamp - ColumnFamily contents - ColumnFamily anchor

入门时看做 Map<row_key + falimy + column + timestamp, value>
```

##### 获取Hbase

```shell
Hortonworks - yahoo

cloudera mansger - hbase-0.98.1+cdh5.1.2+70
```

##### Hbase安装文件及安装

```shell
CDH与HDP

以下载rpm安装包为例
hbase-0.98.0.2.1.5.0-695.el6.noarch.rpm
hbase-master-0.98.0.2.1.5.0-695.el6.noarch.rpm
hbase-regionserver-0.98.0.2.1.5.0-695.el6.noarch.rpm

直接安装rpm包
$ rpm -ivh hbase-0.98.0.2.1.5.0-695.el6.noarch.rpm
依赖zookeeper >= 3.4.5
依赖Hadoop-hdfs

hbase-master 与 hbase-regionserver
service启动脚本
依赖hbase = 0.98.0.2.1.5.0-695.el6
```

##### Hbase目录结构详解

```shell
/usr/lib/hbase/
bin/
conf/
hbase-webapps/
include/
lib/
logs/
pids/

-------------------------------------

bin/
	*.rb
		工具脚本
		运行方式: hbase-jruby 脚本　参数
	hbase-cleanup.sh
		删除zk或hdfs内容, 一般集群发生问题时，用它清空zookeeper内容
	hbase
		/usr/bin/hbase最终调用的脚本
	hbase-config.sh
		启动环境配置脚本，一般不直接调用
	hbase-daemon.sh
		可以用service hbase-master 或 service hbase-regionserver 代替
		组件启动脚本
		
conf/
	hadoop-metrics.properties
	hadoop-metrics2-hbase.properties
		metric监控配置
	hbase-env.sh
		环境变量配置
	hbase-site.xml
		运行参数配置
	hbase-policy.xml
		安全策略配置
		应用场景比较少
	log4j.properties
		log配置
	regionservers
		所有regionserver, 用于启停
		不常用
		
hbase-webapps/
	web ui 页面目录
	
include/
	保存了thrift脚本
	
logs/
	日志目录
	
pids
	保存运行进程pid
	保存zookeeper中node路径
	
lib/
	依赖jar包
	
lib/ruby
	hbase shell 依赖脚本
```

##### 启动

```shell
最简配置

service hbase-master start

service hbase-regionserver start

常见错误
	查看 .log 和 .out, 能排查大多数问题
	
	目录权限
	
	依赖环境
		lzo
		机器名
		
	java版本
	
	hadoop版本与推荐配置不匹配
		没有正确建立软链接
		指定类不存在与任务jar包
		
	zookeeper版本与推荐不匹配
		通信无法成功
```

##### hbase shell

```shell
基于 jruby

http://abloz.com/hbase/book.html/#shell

包含常用工具

	状态查询(general)
	
	ddl, dml
	
	集群工具(tools)
	
	replication
	
	快照(snapshot)
	
	namespace
	
开启相应功能后才能使用的工具

	权限控制(security)
	
	身份标签(visibility labels)
		粒度更小的访问控制
		
神help

	help: 列出所有命令
	
	help '分组名' 列出分组命令详细用法
	
	help '命令名' 列出明星详细用法
	
	ddl 缺少细节
```

##### 常用表属性

```shell
READONLY
	表只读
	
MEMSTORE_FLUSHSIZE

MAX_FILESIZE

DEFERRED_LOG_FLUSH
```

##### 常用列族属性

```shell
每个属性都有默认值
> describe 'mopishv1'

DATA_BLOCK_ENCODING 设置压缩算法, 压缩保存数据的key-value块

	NONE, DIFF, FAST_DIFF, PREFIX_TREE
	
	搜索 "hbase DATA_BLOCK_ENCODING PREFIX_TREE"
	
COMPRESSION 设置压缩算法, 压缩生成的数据文件

	NONE, LZO, GZ, SHAPPY, LZ4
	
	GZ: CPU消耗少
	
	LZ4: 解压快，适应多线程
	
	http://code.google.com/p/lz4/
	
	SNAPPY 与 LZO: CPU 和 IO较平衡，最常用
	
http://blogs.apache.org/hbase/date/201404

	比较两者组合使用
	
	搜索 "hbase 实战系列　压缩与编码技术"
	
BLOOMFILTER

REPLICATION_SCOPE

VERSIONS

TTL与MIN_VERSIONS

KEEP_DELETED_CELLS

BLOCKSIZE

BLOCKCACHE 与 IN_MEMORY
```

##### 实战 hbase shell 操作

```shel
$ hbase shell

> create 'mopishv3', 'fml'  // 表名，列族名

> list // 查看表

> list_namespace // 查看nemespace

> list_namespace_tables 'hbase'
> list_namespace_tables 'default' // 查看某个namespace中的表

> describe 'mopishv3'

// 修改表结构
> alter 'mopishv3', {NAME=>'fml', BLOOMFILTER=>'NONE'}
> alter 'mopishv3', {MAX_FILESIZE => '134217728'} // 定义表的属性
```



https://www.bilibili.com/video/av46580288/?p=4 18:00











































