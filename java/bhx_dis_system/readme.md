# 尚学堂分布式项目笔记

```
搭建maven私服

从 http://mvnrepository.com/ 获取maven包, 类似 pypi
```

```
maven 命令 clean install 打成war包放到Tomcat
```

```
maven配置文件可以继承, 子项目会继承父项目的pom.xml

一个Tomcat可以部署多个服务.
```

```
需要支持 dubbo 和 rest 两种协议
注意 rt 异常, runtime异常
```

```
用 Java -jar xx.jar 提供服务,并且要负载均衡(用dubbo)
不会放到 tomcat 等web 容器里面
```

```
zookeeper 注册中心
kryo 实现序列化 

引入通用常量类
引用通用DAO类, BaseJdbcDao & JsonRowMapper
引入通过Util类, Encrypt, FastJsonConvert, GzipFilter
```

```
搭建 3个实例的zookeeper集群
```

```
SSO 单点登录

如, 在不同的网站都用微信登录
```