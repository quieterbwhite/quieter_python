#### Install Sentry Via Python

>   https://docs.sentry.io/server/installation/python/

#### 安装

os: ubuntu

```shell
# install dependences
$ sudo apt install python-setuptools python-dev libxslt1-dev gcc libffi-dev libjpeg-dev libxml2-dev libxslt-dev libyaml-dev libpq-dev

# 创建虚拟环境并安装
$ mkdir /home/bwhite/software/sentry && cd /home/bwhite/software/sentry
$ pipenv --two
$ pipenv install sentry
## 如果虚拟环境安装不成功，有可能会报依赖错误，这个解决不了。可以直接在宿主机pip安装。

# 配置文件
$ pipenv run sentry init /home/bwhite/software/sentry/
配置redis
配置数据库postgresql
配置邮件

# 安装postgresql客户端
$ sudo apt install postgresql-client-9.5

# 创建数据库
$ pipenv run createdb -E utf-8 -h 127.0.0.1 -p 54321 -U postgres -W sentry
#创建表结构
$ pipenv run sentry --config /home/bwhite/software/sentry/ upgrade
707295770@qq.com & b__white@163.com
tiger & yunhe5
superuser

# 开启web
$ pipenv run sentry --config /home/bwhite/software/sentry/ run web
# 开启worker
$ pipenv run sentry --config /home/bwhite/software/sentry/ run worker
# 开启corn
$ pipenv run sentry --config /home/bwhite/software/sentry/ run cron

# 访问
visit http://localhost:9000
```

#### 后台启动

```shell
# 安装 supervisor
$ sudo apt install supervisor

# 配置文件 /etc/supervisor/conf.d/sentry.conf
[program:sentry-web]
user=bwhite
directory=/home/bwhite/software/sentry/
environment=SENTRY_CONF="/home/bwhite/software/sentry"
command=pipenv run sentry run web
autostart=true
autorestart=true
redirect_stderr=true
stdout_logfile=syslog
stderr_logfile=syslog

[program:sentry-worker]
user=bwhite
directory=/home/bwhite/software/sentry/
environment=SENTRY_CONF="/home/bwhite/software/sentry"
command=pipenv run sentry run worker
autostart=true
autorestart=true
redirect_stderr=true
stdout_logfile=syslog
stderr_logfile=syslog

[program:sentry-cron]
user=bwhite
directory=/home/bwhite/software/sentry/
environment=SENTRY_CONF="/home/bwhite/software/sentry"
command=pipenv run sentry run cron
autostart=true
autorestart=true
redirect_stderr=true
stdout_logfile=syslog
stderr_logfile=syslog

$ sudo supervisor update
```

