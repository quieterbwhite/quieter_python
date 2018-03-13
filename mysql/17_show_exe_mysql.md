# show mysql
> https://www.cnblogs.com/huangtailang/p/a38e021a46051b99b36a32c6313f1cf5.html  

## By log
```
1.进入Mysql

2.启用Log功能(general_log=ON)

    SHOW VARIABLES LIKE "general_log%";
    
    SET GLOBAL general_log = 'ON';

3.设置Log文件地址(所有Sql语句都会在general_log_file里)

    SET GLOBAL general_log_file = 'c:\mysql.log';

4.下载BareTail专门查看Log文件的绿色软件(提供免费版本仅220k)

5.执行mysql命令然后在BareTail里查看
```
