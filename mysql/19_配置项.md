# Mysql 配置项

## SQL_LOG_BIN = {ON | OFF}
```
如果在一连接中将该值设置为OFF，则该连接上客户端的所有更新操作在MYSQL二进制日志中不会记录日志。

对于数据库的操作，经常需要暂时停止对bin-log日志的写入，那就需要这个命令：set sql_log_bin=on/off

sql_log_bin 是一个动态变量，修改该变量时，可以只对当前会话生效（Session），也可以是全局的（Global），
当全局修改这个变量时，只会对新的会话生效 （这意味当对当前会话也不会生效），因此一般全局修改了这个变量后，都要把原来的所有连接 kill 掉。

mysql> select @@session.sql_log_bin; 

+-----------------------+

| @@session.sql_log_bin |

+-----------------------+

|                     1 |

+-----------------------+

1 row in set (0.00 sec)

mysql>

可以看出sql_log_bin的值是1|0, 当sql_log_bin的值为0的时候，本次连接mysql的session里面所输入的语句都不会被计入bin_log里面，也不会被丛库执行。

set sql_log_bin=0;
```
