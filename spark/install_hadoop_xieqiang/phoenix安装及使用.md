# phoenix安装及使用

```shell
开发：/bigdata/phoenix-4.14.2/bin/sqlline.py dp-hadoop3,dp-hadoop4,dp-hadoop5





生产：/root/software/phoenix-4.14.2-HBase-1.3-bin/bin/sqlline.py dp-hadoop3,dp-hadoop4,dp-hadoop5



异步创建索引：

CREATE INDEX SX_CASECODE_INDEX ON DP.SX(CASE_CODE,NAME,CODE_NUM) ASYNC;
./hbase org.apache.phoenix.mapreduce.index.IndexTool --schema dp --data-table sx --index-table SX_CASECODE_INDEX --output-path hdfs:///dp/phoenix-sx-casecode-index
```

