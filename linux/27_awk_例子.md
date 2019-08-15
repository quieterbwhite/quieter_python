#### AWK 例子

##### 从json文件提取数据
```shell
gawk '{print $2}' /media/server/Seagate_data/wenshu_src_original/wenshu_superfast_bw.json | gawk -F ',' '{print $1}' | gawk '{gsub("\"", "");print}' > /media/server/Seagate_data/docid/wenshu_superfast_bw.json
```
