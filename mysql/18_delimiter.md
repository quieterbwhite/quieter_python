# Mysql delimiter
> https://blog.csdn.net/qq_26941173/article/details/77872026  

```
delimiter是mysql分隔符，在mysql客户端中分隔符默认是分号（；）。
如果一次输入的语句较多，并且语句中间有分号，这时需要新指定一个特殊的分隔符。
```

``` 
mysql> delimiter //  
mysql> create trigger upd_check before update on account   
    -> for each row  
    -> begin  
    -> if new.amount < 0 then  
    ->  set new.amount=0;  
    -> elseif new.amount > 100 then  
    ->  set new.amount = 100;  
    -> end if;  
    -> end;  
    -> //  
Query OK, 0 rows affected (0.00 sec)  
  
mysql> delimiter ;

上面就是，先将分隔符设置为 //, 
直到遇到下一个 //,才整体执行语句。
执行完后，最后一行， delimiter ; 将mysql的分隔符重新设置为分号；
如果不修改的话，本次会话中的所有分隔符都以// 为准。
```

```
MySQL中delimit命令。
　　这个命令与存储过程没什么关系。
　　其实就是告诉mysql解释器，该段命令是否已经结束了，mysql是否可以执行了。
　　即改变输入结束符。
　　默认情况下，delimiter是分号“;”。
　　在命令行客户端中，如果有一行命令以分号结束，
　　那么回车后，mysql将会执行该命令。
　　但有时候，不希望MySQL这么做。因为可能输入较多的语句，且语句中包含有分号。
　　默认情况下，不可能等到用户把这些语句全部输入完之后，再执行整段语句。
　　因为mysql一遇到分号，它就要自动执行。
　　这种情况下，就可以使用delimiter，把delimiter后面换成其它符号，如//或$$。
　　此时，delimiter作用就是对整个小段语句做一个简单的封装。
　　此命令多用在定义子程序，触发程序等musql自己内嵌小程序中。
```
