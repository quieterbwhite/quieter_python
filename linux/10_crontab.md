#### crontab

> https://crontab.guru/#0_*/2_*_*_*
> https://tool.lu/crontab/

##### 编辑crontab文件
```
crontab -e

*/1 * * * * sh /home/bwhite/tmp/b.sh

0 */2 * * * echo `date` >> /tmp/crontab-test.log
```

##### b.sh
```shell
#!/bin/sh

# 环境变量
export PATH=/home/bwhite/software/protoc-3.5.1-linux-x86_64/bin:/home/bwhite/
software/apache-maven-3.5.2/bin:/home/bwhite/software/gradle-4.4.1/bin:/home/
bwhite/software/jdk1.8.0_152/bin:/home/bwhite/software/jdk1.8.0_152/jre/bin:/
home/bwhite/bin:/home/bwhite/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/s
bin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/home/bwhite/software/nod
e-v8.9.4-linux-x64/bin:/snap/bin:/snap/bin

cd /home/bwhite/work/debt && pipenv run python manage.py closepoll 22
```

##### Defaults
```
Type the following command to view default entries:

    $ sudo tail -f /var/log/syslog

OR better use the grep command to find cron job in that file:

    $ sudo grep -i cron /var/log/syslog
```

##### Use systemctl command
```
You can also use the following command to just see latest CRON task related entries on Ubuntu v16.04 LTS+ only:

    $ sudo systemctl status cron
```

##### Use journalctl command to display log
```
Type the following command to see cron logs on Ubuntu v16.04 LTS+ only:

$ sudo journalctl -u cron
$ sudo journalctl -u cron -b | more
$ sudo journalctl -u cron -b | grep something
$ sudo journalctl -u cron -b | grep -i error
```

##### crontab 规则
> http://man.linuxde.net/crontab
>
> https://www.cnblogs.com/longjshz/p/5779215.html
>
> http://linuxtools-rst.readthedocs.io/zh_CN/latest/base/06_monitor.html

**crontab命令**被用来提交和管理用户的需要周期性执行的任务，与windows下的计划任务类似，当安装完成操作系统后，默认会安装此服务工具，并且会自动启动crond进程，crond进程每分钟会定期检查是否有要执行的任务，如果有要执行的任务，则自动执行该任务。

---

**crontab 脚本错误日志和正确的输出写入到文件**
https://blog.csdn.net/u012129607/article/details/80418149

如果crontab不重定向输出，并且crontab所执行的命令有输出内容的话，是一件非常危险的事情。因为该输出内容会以邮件的形式发送给用户，内容存储在邮件文件

/var/spool/mail/$user

如果命令执行比较频繁（如每分钟一次），或者命令输出内容较多，会使这个邮件文件不断追加内容，文件越来越大。而邮件文件一般存放在根分区，根分区一般相对较小，所以会造成根分区写满而无法登录服务器。

**不输出内容**
***/5 * * * * /root/XXXX.sh &>/dev/null 2>&1** 

**将正确和错误日志都输出到 /tmp/load.log**
***/1 * * * * /root/XXXX.sh > /tmp/load.log 2>&1 &**

**只输出正确日志到 /tmp/load.log**
***/1 * * * * /root/XXXX.sh > /tmp/load.log &  等同于   */1 * * * * /root/XXXX.sh 1>/tmp/load.log &**

**只输出错误日志到 /tmp/load.log**
***/1 * * * * /root/XXXX.sh 2> /tmp/load.log &** 

名词解释

在shell中，每个进程都和三个系统文件相关联：标准输入stdin，标准输出stdout和标准错误stderr，三个系统文件的文件描述符分别为0，1和2。所以这里2>&1的意思就是将标准错误也输出到标准输出当中。

> 就相当于 1> 也就是重定向标准输出，不包括标准错误。通过2>&1，就将标准错误重定向到标准输出了（stderr已作为stdout的副本），那么再使用>重定向就会将标准输出和标准错误信息一同重定向了。如果只想重定向标准错误到文件中，则可以使用2> file。
> 



---

### 语法 

```
crontab(选项)(参数)
```

### 选项 

```
-e：编辑该用户的计时器设置；
-l：列出该用户的计时器设置；
-r：删除该用户的计时器设置；
-u<用户名称>：指定要设定计时器的用户名称。
```

### 参数 

crontab文件：指定包含待执行任务的crontab文件。

### 知识扩展 

Linux下的任务调度分为两类：**系统任务调度**和**用户任务调度**。

**系统任务调度：**系统周期性所要执行的工作，比如写缓存数据到硬盘、日志清理等。在`/etc`目录下有一个crontab文件，这个就是系统任务调度的配置文件。

`/etc/crontab`文件包括下面几行：

```
SHELL=/bin/bash
PATH=/sbin:/bin:/usr/sbin:/usr/bin
MAILTO=""HOME=/

# run-parts
51 * * * * root run-parts /etc/cron.hourly
24 7 * * * root run-parts /etc/cron.daily
22 4 * * 0 root run-parts /etc/cron.weekly
42 4 1 * * root run-parts /etc/cron.monthly
```

前四行是用来配置crond任务运行的环境变量，第一行SHELL变量指定了系统要使用哪个shell，这里是bash，第二行PATH变量指定了系统执行命令的路径，第三行MAILTO变量指定了crond的任务执行信息将通过电子邮件发送给root用户，如果MAILTO变量的值为空，则表示不发送任务执行信息给用户，第四行的HOME变量指定了在执行命令或者脚本时使用的主目录。

**用户任务调度：**用户定期要执行的工作，比如用户数据备份、定时邮件提醒等。用户可以使用 crontab 工具来定制自己的计划任务。所有用户定义的crontab文件都被保存在`/var/spool/cron`目录中。其文件名与用户名一致，使用者权限文件如下：

```
/etc/cron.deny     该文件中所列用户不允许使用crontab命令
/etc/cron.allow    该文件中所列用户允许使用crontab命令
/var/spool/cron/   所有用户crontab文件存放的目录,以用户名命名
```

crontab文件的含义：用户所建立的crontab文件中，每一行都代表一项任务，每行的每个字段代表一项设置，它的格式共分为六个字段，前五段是时间设定段，第六段是要执行的命令段，格式如下：

```
minute   hour   day   month   week   command     顺序：分 时 日 月 周
```

其中：

- minute： 表示分钟，可以是从0到59之间的任何整数。
- hour：表示小时，可以是从0到23之间的任何整数。
- day：表示日期，可以是从1到31之间的任何整数。
- month：表示月份，可以是从1到12之间的任何整数。
- week：表示星期几，可以是从0到7之间的任何整数，这里的0或7代表星期日。
- command：要执行的命令，可以是系统命令，也可以是自己编写的脚本文件。

在以上各个字段中，还可以使用以下特殊字符：

- 星号（*）：代表所有可能的值，例如month字段如果是星号，则表示在满足其它字段的制约条件后每月都执行该命令操作。
- 逗号（,）：可以用逗号隔开的值指定一个列表范围，例如，“1,2,5,7,8,9”
- 中杠（-）：可以用整数之间的中杠表示一个整数范围，例如“2-6”表示“2,3,4,5,6”
- 正斜线（/）：可以用正斜线指定时间的间隔频率，例如“0-23/2”表示每两小时执行一次。同时正斜线可以和星号一起使用，例如*/10，如果用在minute字段，表示每十分钟执行一次。

**crond服务**

```
/sbin/service crond start    //启动服务
/sbin/service crond stop     //关闭服务
/sbin/service crond restart  //重启服务
/sbin/service crond reload   //重新载入配置
```

查看crontab服务状态：

```
service crond status
```

手动启动crontab服务：

```
service crond start
```

查看crontab服务是否已设置为开机启动，执行命令：

```
ntsysv
```

加入开机自动启动：

```
chkconfig –level 35 crond on
```

### 实例 

每1分钟执行一次command

```
* * * * * command
```

每小时的第3和第15分钟执行

```
3,15 * * * * command
```

在上午8点到11点的第3和第15分钟执行

```
3,15 8-11 * * * command
```

每隔两天的上午8点到11点的第3和第15分钟执行

```
3,15 8-11 */2 * * command
```

每个星期一的上午8点到11点的第3和第15分钟执行

```
3,15 8-11 * * 1 command
```

每晚的21:30重启smb 

```
30 21 * * * /etc/init.d/smb restart
```

每月1、10、22日的4 : 45重启smb 

```
45 4 1,10,22 * * /etc/init.d/smb restart
```

每周六、周日的1:10重启smb

```
10 1 * * 6,0 /etc/init.d/smb restart
```

每天18 : 00至23 : 00之间每隔30分钟重启smb 

```
0,30 18-23 * * * /etc/init.d/smb restart
```

每星期六的晚上11:00 pm重启smb 

```
0 23 * * 6 /etc/init.d/smb restart
```

每一小时重启smb 

```
* */1 * * * /etc/init.d/smb restart
```

晚上11点到早上7点之间，每隔一小时重启smb

```
* 23-7/1 * * * /etc/init.d/smb restart
```

每月的4号与每周一到周三的11点重启smb 

```
0 11 4 * mon-wed /etc/init.d/smb restart
```

一月一号的4点重启smb

```
0 4 1 jan * /etc/init.d/smb restart
```

每小时执行`/etc/cron.hourly`目录内的脚本

```
01 * * * * root run-parts /etc/cron.hourly
```
