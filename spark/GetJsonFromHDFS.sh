#! /bin/bash

# 从hdfs上拉取文件到本地

start_date=20190625

start_sec=`date -d "$start_date" "+%s"`

end_date='2019-06-24'

for i in `seq 1 100`

    do
         day=$(date -d "@$start_sec" "+%Y-%m-%d")
         echo $day
         hadoop fs -get hdfs://dp-hadoop2:9000/sifa_json/$day/*.json /tmp/sifa/$day.json

    if [[ $day == $end_date ]]
        then
           break
    fi
        echo ${i}

    start_sec=$[${start_sec}-86400]

done
