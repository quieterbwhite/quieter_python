#!/bin/bash  

# 修改此脚本的权限为 777
  
step=4 #间隔的秒数，不能大于60  
  
for (( i = 0; i < 60; i=(i+step) )); do  
    $(/home/bwhite/software/node-v10.15.3-linux-x64/bin/node '/home/bwhite/mygithub/quieter_python/frontend/nightmare/wenshu_content_html.js' >> /tmp/node_spider.log)  
    sleep $step  
done  
  
exit 0