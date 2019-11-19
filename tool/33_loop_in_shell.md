#### Shell 命令执行循环

##### 循环复制文件到远程服务器
```shell
#! /bin/bash

# 每个文件一个日期复制到服务器

start_date=$1
dir=$2

start_sec=`date -d "$start_date" "+%s"`

for file_n in `ls ${dir}`
do
    day=$(date -d "@$start_sec" "+%Y-%m-%d")
    echo "--------------------start----------------------------"
    echo "1,--------------scp ${dir}/${file_n} libo@idc-cdh-data1:/data/tmp/sifa_tar;"
    #scp ${dir}/${file_n} libo@idc-cdh-data1:/data/tmp/sifa_tar;
    echo "--------------------end----------------------------"
    start_sec=$[${start_sec}-86400]
done
```

##### 循环解压
```

```
