#! /bin/bash

# 每个文件一个日期分区导入文书数据到hive,
# 参数1，开始日期（倒推）
# 参数2，数据所在的目录
# 参数3，要导入的hive表名

start_date=$1
dir=$2
table_name=$3
table_name_tmp=$3"_tmp"

start_sec=`date -d "$start_date" "+%s"`

for file_n in `ls ${dir}`
do
    day=$(date -d "@$start_sec" "+%Y-%m-%d")
    echo "--------------------start----------------------------"
    echo "1,--------------load data local inpath ${dir}/${file_n} into table dp.${table_name_tmp};"
    hive  -e "load data local inpath '${dir}/${file_n}' into table dp.${table_name_tmp};"
    echo "2,--------------insert into table dp.${table_name} partition(ct='${day}') select data from dp.${table_name_tmp};"
    hive  -e "insert into table dp.${table_name} partition(ct='${day}') select data from dp.${table_name_tmp};"
    echo  "3,--------------truncate table dp.${table_name_tmp}"
    hive  -e "truncate table dp.${table_name_tmp}"
    echo "--------------------end----------------------------"
    start_sec=$[${start_sec}-86400]
done
