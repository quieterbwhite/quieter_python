# trouble shotting
> Created Time: 2015年12月31日 星期四 16时25分08秒

```
1. 继承 AbstractUser 后直接使用报错
2. 线上环境, 蓝绿部署
3. Django, after upgrade: MySQL server has gone away
```

## 继承 AbstractUser 后直接使用报错
```
通常，当想往标准的 django User model 中增加自定义字段时，我们会通过继承
AbstractUser来实现。
但是，如果继承并添加字段后直接使用是不行的。这时候会提示 用户方面的东西找不到
或冲突。这是django用户验证模型不知道是使用 默认的用户模型 User 还是我们继承
的子类 Users。
所以，指定一个就行了。
方法是，配置文件里面 增加配置:
    AUTH_USER_MODEL = `myapp.MyUser`
```

## 线上环境, 蓝绿部署
```
Nginx配置 —— 我们有两套环境在线上同时运行，可以称为a环境和b环境，主要用于
上线以及线上突然出现问题时回滚
```

## Django, after upgrade: MySQL server has gone away
> https://stackoverflow.com/questions/26958592/django-after-upgrade-mysql-server-has-gone-away  
> https://zhaojames0707.github.io/post/django_mysql_gone_away/  
> https://code.djangoproject.com/ticket/21597#comment:29  
```
To prevent connection timeout error you should set CONN_MAX_AGE in settings.py to value which is less than wait_timeout in MySQL config (my.cnf). In that case Django detects that connection need to be reopen earlier than MySQL throws it. Default value for MySQL 5.7 is 28800 seconds.

settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'CONN_MAX_AGE': 3600,
        <other params here>
    }
}
Documentation: https://docs.djangoproject.com/en/1.7/ref/settings/#conn-max-age

my.cnf:

wait_timeout = 28800
Documentation: https://dev.mysql.com/doc/refman/5.7/en/server-system-variables.html#sysvar_wait_timeout

方法1是针对 Model 操作间隔一定很长的情况，如果某个时间段内需要很频繁的操作数据库，那么频繁关闭-新建数据库连接无疑是低效的。而且，connection 是与默认的数据库的连接，即 settings 中定义的 default 数据库。如果项目配置了多个数据库(列如主从数据库)，那么 connection.close()则不能与关闭其他数据库的连接，问题仍未解决。
方法2直接修改数据库超时时间，很容易影响别的服务，会带来很多潜在的问题。
```
