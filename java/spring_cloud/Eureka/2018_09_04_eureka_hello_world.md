#### Spring Cloud Eureka-服务注册与发现

[![img](https://s5.51cto.com//oss/201806/23/1b869568764673834d5ec288ad921edd.jpg?x-oss-process=image/resize,m_fixed,h_120,w_120)](http://blog.51cto.com/zero01)

ZeroOne01

2018-08-12 21:21:23

>   http://blog.51cto.com/zero01/2158534

### Spring Cloud Eureka

Spring Cloud是目前用于开发微服务的主流框架之一，我们都知道在微服务架构中最为基础、核心的模块，就是服务注册与发现。

在Spring Cloud里我们可以使用它的Eureka模块来实现服务注册与发现，Spring Cloud Eureka是基于Netflix Eureka做了二次封装，它主要负责完成各个微服务实例的自动化注册和发现功能。

Eureka由两个组件组成：

-   Eureka Server（注册中心）
-   Eureka Client （服务注册）

分布式系统中为什么需要服务发现：

>   在实际的分布式环境下，架构规模往往不再是几台服务器，而是每个独立服务都跑在多台机器上。例如A服务部署在10台机器上，B服务也部署在10台机器上，C服务部署在5台机器上。
>
>   现在A服务的一些功能需要调用B服务来实现，那么问题来了，A服务要如何才能调用B服务呢？通常情况下，我们可以想到将B服务所在的所有机器地址，通过配置文件来配置到A服务中，使其能够通过配置好的地址去发现并调用B服务。
>
>   这也的确是一个可行的方法，但是这些机器的地址都是有可能发生变化的，而且在生产环境中也会出现部分服务宕机的情况，这样就有可能导致一些连锁效应。随着业务的扩展，机器也会越来越多，也没办法再手动通过配置文件这种方式来配置机器地址了。
>
>   鉴于人类的懒惰天性。。。呸，鉴于人类对高效工作、美好生活的追求。所以专门用于服务注册与发现的工具被一一开发出来。有了服务治理框架后，服务发现就可以交由它来自动完成。这时候A服务只需要到注册中心进行服务注册，同样的B服务也到注册中心进行服务注册。注册之后，注册中心会通过类似心跳机制来确认服务的存活。如果确认某个服务宕机后，注册中心会把宕机的服务剔除掉。当A服务要调用B服务的时候，则到注册中心去获取B服务的调用地址即可，B服务调用A服务也是同理。注册中心就相当于一个服务与服务之间的桥梁或者说中间人，可以说帮我们管理了服务之间琐事。

Eureka服务治理体系如下：
![Spring Cloud Eureka-服务注册与发现](http://i2.51cto.com/images/blog/201808/12/d67cd6c62929c90649663e66fa184615.png?x-oss-process=image/watermark,size_16,text_QDUxQ1RP5Y2a5a6i,color_FFFFFF,t_100,g_se,x_10,y_10,shadow_90,type_ZmFuZ3poZW5naGVpdGk=)

Spring Cloud官网地址如下：

>   <https://projects.spring.io/spring-cloud/>

------

### Eureka Server

废话不多说，本小节我们来搭建一个Eureka Server，即服务注册中心。打开IDEA，新建一个Spring Initializr项目：
![Spring Cloud Eureka-服务注册与发现](http://i2.51cto.com/images/blog/201808/12/de26c8f269776f1559772b1b6ab8cc1c.png?x-oss-process=image/watermark,size_16,text_QDUxQ1RP5Y2a5a6i,color_FFFFFF,t_100,g_se,x_10,y_10,shadow_90,type_ZmFuZ3poZW5naGVpdGk=)
![Spring Cloud Eureka-服务注册与发现](http://i2.51cto.com/images/blog/201808/12/78f2c613b9d1d2b8d2ede61898cb2c31.png?x-oss-process=image/watermark,size_16,text_QDUxQ1RP5Y2a5a6i,color_FFFFFF,t_100,g_se,x_10,y_10,shadow_90,type_ZmFuZ3poZW5naGVpdGk=)

勾选Eureka Server模块：
![Spring Cloud Eureka-服务注册与发现](http://i2.51cto.com/images/blog/201808/12/b1f953ac1d3f434d09dba43dbb5ff54d.png?x-oss-process=image/watermark,size_16,text_QDUxQ1RP5Y2a5a6i,color_FFFFFF,t_100,g_se,x_10,y_10,shadow_90,type_ZmFuZ3poZW5naGVpdGk=)

完成项目的创建：
![Spring Cloud Eureka-服务注册与发现](http://i2.51cto.com/images/blog/201808/12/5986c5780e4d669abf8d17c0b7c72286.png?x-oss-process=image/watermark,size_16,text_QDUxQ1RP5Y2a5a6i,color_FFFFFF,t_100,g_se,x_10,y_10,shadow_90,type_ZmFuZ3poZW5naGVpdGk=)

项目生成的pom.xml文件内容如下：

```
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>org.zero</groupId>
    <artifactId>eureka</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <packaging>jar</packaging>

    <name>eureka</name>
    <description>Demo project for Spring Boot</description>

    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.0.4.RELEASE</version>
        <relativePath/> <!-- lookup parent from repository -->
    </parent>

    <properties>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
        <java.version>1.8</java.version>
        <spring-cloud.version>Finchley.SR1</spring-cloud.version>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-eureka-server</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.springframework.cloud</groupId>
                <artifactId>spring-cloud-dependencies</artifactId>
                <version>${spring-cloud.version}</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>
</project>
```

注：SpringBoot与SpringCloud组件的版本是有一个对应关系的，这个在官网上有详细的对照图。值得注意的是，SpringCloud不是以2.0.1这种数字的方式来标识版本号，而是以伦敦地铁站的名称来标识版本号，并且这些名称是符合字母顺序的。

项目创建好后，我们可以试着启动看看，但是在启动之前需要在启动类中加上`@EnableEurekaServer`注解，表示启用Eureka Server，否则访问就会报404。代码如下：

```
package org.zero.eureka;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.netflix.eureka.server.EnableEurekaServer;

@SpringBootApplication
@EnableEurekaServer
public class EurekaApplication {

    public static void main(String[] args) {
        SpringApplication.run(EurekaApplication.class, args);
    }
}
```

启动项目后，能够访问到如下Eureka注册中心的页面代表成功：
![Spring Cloud Eureka-服务注册与发现](http://i2.51cto.com/images/blog/201808/12/bb4b43b80ab78a7910612bd35222913f.png?x-oss-process=image/watermark,size_16,text_QDUxQ1RP5Y2a5a6i,color_FFFFFF,t_100,g_se,x_10,y_10,shadow_90,type_ZmFuZ3poZW5naGVpdGk=)

此时虽然能够正常访问到注册中心的页面，但是会发现控制台一直在报错，提示`Cannot execute request on any known server`。这是因为这个Eureka Server既是server的同时，也是一个client，它也是需要把自己注册到一个注册中心去的。因为我们并没有配置注册中心的地址，所以它没办法注册自己就会报这个错误。

既然如此，我们只需配置一下注册中心的地址即可，编辑application.yml配置文件内容如下：

```
eureka:
  client:
    service-url:
      defaultZone: http://localhost:8761/eureka/  # 指定注册中心的url
    register-with-eureka: false  # 指定不进行注册操作，默认为true，若进行注册的话，会显示在Eureka信息面板上
  server:
    enable-self-preservation: false  # 禁用eureka server的自我保护机制，建议在生产环境下打开此配置
spring:
  application:
    name: eureka  # 指定应用的名称
server:
  port: 8761  # 指定项目的端口号
```

注：由于server和client是采用心跳机制来确认存活的，所以在启动项目的过程可能依旧会报错。但是只要启动后不是一直报错，并且能正常访问Eureka信息面板页面的话，则代表项目是在正常运行的

------

### Eureka Client的使用

在上一小节中，我们简单介绍了如何创建、配置Eureka Server项目。既然我们已经知道了如何搭建Eureka Server，那么本小节我们将介绍Eureka Client的使用，会简单演示一下如何通过Eureka Client进行服务注册。

同样的，使用IDEA创建一个Spring Initializr项目，只不过在勾选模块的时候需要选择Eureka Discovery，如下:
![Spring Cloud Eureka-服务注册与发现](http://i2.51cto.com/images/blog/201808/12/d741cb3cf3009ee9a8c9a305604580ef.png?x-oss-process=image/watermark,size_16,text_QDUxQ1RP5Y2a5a6i,color_FFFFFF,t_100,g_se,x_10,y_10,shadow_90,type_ZmFuZ3poZW5naGVpdGk=)

项目生成的pom.xml文件内容如下：

```
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>org.zero.eureka</groupId>
    <artifactId>client</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <packaging>jar</packaging>

    <name>client</name>
    <description>Demo project for Spring Boot</description>

    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.0.4.RELEASE</version>
        <relativePath/> <!-- lookup parent from repository -->
    </parent>

    <properties>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
        <java.version>1.8</java.version>
        <spring-cloud.version>Finchley.SR1</spring-cloud.version>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.springframework.cloud</groupId>
                <artifactId>spring-cloud-dependencies</artifactId>
                <version>${spring-cloud.version}</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>
</project>
```

项目的依赖都加载完成后，在启动类中加上`@EnableDiscoveryClient`，声明这是一个eureka client，否则不会进行服务注册：

```
package org.zero.eureka.client;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;

@SpringBootApplication
@EnableDiscoveryClient
public class ClientApplication {

    public static void main(String[] args) {
        SpringApplication.run(ClientApplication.class, args);
    }
}
```

接着就是在application.yml配置文件中，配置注册中心即eureka server的地址，以及项目的名称和启动端口号。如下：

```
eureka:
  client:
    service-url:
      defaultZone: http://localhost:8761/eureka/
spring:
  application:
    name: eureka-client
server:
  port: 9088
```

完成以上配置后，即可启动项目。但是我这里启动项目的时候失败了，控制台输出如下警告信息：

>   Invocation of destroy method failed on bean with name 'scopedTarget.eurekaClient': org.springframework.beans.factory.BeanCreationNotAllowedException: Error creating bean with name 'eurekaInstanceConfigBean': Singleton bean creation not allowed while singletons of this factory are in destruction (Do not request a bean from a BeanFactory in a destroy method implementation!)

这是因为client里不包含Tomcat的依赖，所以Spring容器无法创建一些实例，从而导致项目无法启动，只需在pom.xml文件中，加上web依赖即可：

```
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-web</artifactId>
</dependency>
```

项目启动成功后，可以在eureka server的信息面板中查看到已注册的实例信息，如下：
![Spring Cloud Eureka-服务注册与发现](http://i2.51cto.com/images/blog/201808/12/5fe12c638fd13619fd6250ffa7d81834.png?x-oss-process=image/watermark,size_16,text_QDUxQ1RP5Y2a5a6i,color_FFFFFF,t_100,g_se,x_10,y_10,shadow_90,type_ZmFuZ3poZW5naGVpdGk=)

------

### Eureka的高可用

高可用是在服务架构设计中，频繁出现的词汇。微服务架构里自然也一样需要保证服务的高可用性，所以本小节将简单说明一下Eureka是如何实现高可用的。

在实际生产环境中服务器是很脆弱的，单台服务器肯定是无法满足高可用的需求，为了保证高可用性我们通常会准备多台服务器。但可以发现上文中所搭建的eureka server是单机的，若这个eureka server宕机，则会导致与之关联的全部微服务发生故障。

既然单机无法保证高可用，那么我们就加多一台机器好了，然后让这两个eureka server互相进行关联。例如我现在有两台eureka server。一台名叫eureka-server01跑在8761端口上，另一台名叫eureka-server02跑在8762端口上。然后只需要两个步骤即可实现高可用：

-   1.编辑这两台eureka server的配置文件，让它们的注册地址互相指向，即可关联在一起
-   2.在eureka client的配置文件中，配置上这两台eureka server的地址，让client能够同时注册到这两台eureka server上。这样即便其中一台eureka server挂掉，另一台依旧可以继续工作

1.编辑两台eureka server的配置文件，eureka-server01：

```
eureka:
  client:
    service-url:
      defaultZone: http://localhost:8762/eureka/  # 指向eureka-server02的url
    register-with-eureka: false
  server:
    enable-self-preservation: false 
spring:
  application:
    name: eureka-server01 
server:
  port: 8761 
```

eureka-server02：

```
eureka:
  client:
    service-url:
      defaultZone: http://localhost:8761/eureka/  # 指向eureka-server01的url
    register-with-eureka: false
  server:
    enable-self-preservation: false
spring:
  application:
    name: eureka-server02 
server:
  port: 8762 
```

2.编辑eureka client的配置文件，多个url使用英文逗号分隔：

```
eureka:
  client:
    service-url:
      defaultZone: http://localhost:8761/eureka/,http://localhost:8762/eureka/
spring:
  application:
    name: eureka-client
server:
  port: 9088
```

------

如果项目规模比较大，有两个以上的eureka server，那该如何在配置文件中配置呢？其实只需要每台eureka server分别配置除自己之外的eureka server机器，然后eureka client则配置所有的eureka server地址即可。如下图：
![Spring Cloud Eureka-服务注册与发现](http://i2.51cto.com/images/blog/201808/12/c3fd05cfdecc8806e78338ad7f176594.png?x-oss-process=image/watermark,size_16,text_QDUxQ1RP5Y2a5a6i,color_FFFFFF,t_100,g_se,x_10,y_10,shadow_90,type_ZmFuZ3poZW5naGVpdGk=)

配置文件示例，eureka-server01：

```
eureka:
  client:
    service-url:
      defaultZone: http://localhost:8762/eureka/,http://localhost:8763/eureka/
    register-with-eureka: false
spring:
  application:
    name: eureka-server01 
server:
  port: 8761 
```

配置文件示例，eureka-server02：

```
eureka:
  client:
    service-url:
      defaultZone: http://localhost:8761/eureka/,http://localhost:8763/eureka/
    register-with-eureka: false
spring:
  application:
    name: eureka-server02 
server:
  port: 8762 
```

配置文件示例，eureka-server03：

```
eureka:
  client:
    service-url:
      defaultZone: http://localhost:8761/eureka/,http://localhost:8762/eureka/
    register-with-eureka: false
spring:
  application:
    name: eureka-server03 
server:
  port: 8763 
```

eureka client的配置文件示例：

```
eureka:
  client:
    service-url:
      defaultZone: http://localhost:8761/eureka/,http://localhost:8762/eureka/,http://localhost:8763/eureka/
spring:
  application:
    name: eureka-client
server:
  port: 9088
```