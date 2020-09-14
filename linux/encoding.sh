#!/bin/bash
### 这个方法比较蠢,安装unar，自动处理编码问题
### 将 values_here 替换为输入编码
FROM_ENCODING="gb18030"
### 输出编码 (UTF-8)
TO_ENCODING="UTF-8"
### 转换命令
CONVERT=" iconv  -f   $FROM_ENCODING  -t   $TO_ENCODING"
### 使用循环转换多个文件
for  file  in  *.txt; do
$CONVERT   "$file"   -o  "${file%.txt}"
done
exit 0
