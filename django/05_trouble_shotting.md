# trouble shotting
> Created Time: 2015年12月31日 星期四 16时25分08秒

```
1. 继承 AbstractUser 后直接使用报错
2. 线上环境
```


```
1. 继承 AbstractUser 后直接使用报错

    通常，当想往标准的 django User model 中增加自定义字段时，我们会通过继承
    AbstractUser来实现。
    但是，如果继承并添加字段后直接使用是不行的。这时候会提示 用户方面的东西找不到
    或冲突。这是django用户验证模型不知道是使用 默认的用户模型 User 还是我们继承
    的子类 Users。
    所以，指定一个就行了。
    方法是，配置文件里面 增加配置:
        AUTH_USER_MODEL = `myapp.MyUser`

    搞定！
```

```
Nginx配置 —— 我们有两套环境在线上同时运行，可以称为a环境和b环境，主要用于
上线以及线上突然出现问题时回滚
```
