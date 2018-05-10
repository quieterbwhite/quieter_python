# Imooc 权限管理系统

## 搭建 SpringBoot + SpringSecurity 环境搭建
```
只要能登录即可

    auth.inMemoryAuthentication().withUser("admin").password("111111").roles("ADMIN");
    
有指定的角色,每个角色有指定的权限

    ...
```

## Apache Shiro 推荐使用的安全框架
```
Application Code -> Subject(user) -> Shiro SecurityManager(mamage all subjects) -> Realm(access your security data)


```