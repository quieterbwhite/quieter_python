# 服务注册与服务发现

      购票               查询用户信息  
用户 ------> 电影微服务 --------------> 用户微服务  

## Basic
```

如何解决硬编码问题

服务发现

    服务提供者 注册 到服务发现组件

    服务消费者 注册 到服务发现组件

    心跳, 30s, 3 times, 检测服务时候仍然可用, 剔除不可用服务

    服务消费者 调用 服务提供者

服务发现组件的功能

    服务注册表

        服务注册表是一个记录当前可用服务实例的网络信息的数据库，是服务发现机制的核心。
        服务注册表提供查询API和管理API, 使用查询API获得可用的服务实例，使用管理API实现注册和注销。

    服务注册

    健康检查

    Eureka 通过心跳检测，健康检查，客户端缓存等机制，确保了系统的可用性，灵活性和可伸缩性。

服务发现的方式

    客户端发现

        Eureka

        Zookeeper

    服务端发现

        Nginx + Consul

术语解释
```

## 服务发现组件 Eureka
```
Why Eureka

    Eureka 来自生产环境, NetFlix 开源的服务发现框架

    Sprint Cloud 对它支持最好

Eureka 简介

Eureka 原理

    Region 和 Zone 的关系

    region1

        zone1
        
            eureka1
            eureka2
            eureka3

        zone2

            eureka4
            eureka5
            eureka6

实现一个 Eureka Server

实现一个 Eureka Client
```
