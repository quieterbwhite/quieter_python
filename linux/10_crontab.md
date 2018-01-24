# crontab

## 编辑crontab文件
```
crontab -e

*/1 * * * * sh /home/bwhite/tmp/b.sh
```

## b.sh
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

## Defaults
```
Type the following command to view default entries:

    $ sudo tail -f /var/log/syslog

OR better use the grep command to find cron job in that file:

    $ sudo grep -i cron /var/log/syslog
```

## Use systemctl command
```
You can also use the following command to just see latest CRON task related entries on Ubuntu v16.04 LTS+ only:

    $ sudo systemctl status cron
```

## Use journalctl command to display log
```
Type the following command to see cron logs on Ubuntu v16.04 LTS+ only:

$ sudo journalctl -u cron
$ sudo journalctl -u cron -b | more
$ sudo journalctl -u cron -b | grep something
$ sudo journalctl -u cron -b | grep -i error
```

## crontab 规则
```
TODO
```
