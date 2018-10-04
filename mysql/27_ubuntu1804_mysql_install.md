#### ubuntu18.04 首次登录mysql未设置密码或忘记密码解决方法

2018年07月17日 23:54:55 [syrdbt](https://me.csdn.net/qq_38737992) 阅读数：843

版权声明：转载请注明出处	https://blog.csdn.net/qq_38737992/article/details/81090373

1.首先输入以下指令：

```
sudo cat /etc/mysql/debian.cnf
```

运行截图如下：

![img](https://img-blog.csdn.net/20180831144759364?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NzM3OTky/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

\2. 再输入以下指令：

```
mysql -u debian-sys-maint -p
//注意! 
//这条指令的密码输入是输入第一条指令获得的信息中的 password = ZCt7QB7d8O3rFKQZ 得来。
//请根据自己的实际情况填写！
```

运行截图如下：**(注意! 这步的密码输入的是 ZCt7QB7d8O3rFKQZ，密码是由第一条指令获得的信息中的**

**password = ZCt7QB7d8O3rFKQZ 得来，每个人不一样，请根据自己的实际情况输入，输入就可以得到以下运行情况）**

![img](https://img-blog.csdn.net/20180717234206251?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NzM3OTky/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

\3. 修改密码，本篇文章将密码修改成 root , 用户可自行定义。

```
use mysql;
// 下面这句命令有点长，请注意。
update mysql.user set authentication_string=password('root') where user='root' and Host ='localhost';
update user set plugin="mysql_native_password"; 
flush privileges;
quit;
```

![img](https://img-blog.csdn.net/20180717234900348?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NzM3OTky/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

\4. 重新启动mysql:

```
sudo service mysql restart
mysql -u root -p // 启动后输入已经修改好的密码：root
```

![img](https://img-blog.csdn.net/20180717235251402?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NzM3OTky/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

![img](https://img-blog.csdn.net/20180717235329735?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4NzM3OTky/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)