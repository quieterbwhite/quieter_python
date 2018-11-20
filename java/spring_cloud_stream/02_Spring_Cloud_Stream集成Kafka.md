# Spring Cloud Stream集成Kafka

> https://majing.io/posts/10000008561247

这里演示使用Spring Boot ，Spring Cloud集成Kafka来实现一个简单的实时流系统。

### 添加依赖

可以在[https://start.spring.io](https://start.spring.io/)创建一个基于spring boot的maven项目。

需要添加的主要依赖：spring-cloud-stream以及spring-cloud-starter-stream-kafka，如下：

```xml
<dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-actuator</artifactId>
  </dependency>
  <dependency>
      <groupId>org.springframework.cloud</groupId>
      <artifactId>spring-cloud-stream</artifactId>
  </dependency>
  <dependency>
      <groupId>org.springframework.cloud</groupId>
      <artifactId>spring-cloud-starter-stream-kafka</artifactId>
  </dependency>
```

添加dependencyManagement

```xml
<dependencyManagement>
  <dependencies>
    <dependency>
      <!-- Import dependency management from Spring Boot -->
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-dependencies</artifactId>
      <version>${spring-boot.version}</version>
      <type>pom</type>
      <scope>import</scope>
    </dependency>
    <dependency>
      <groupId>org.springframework.cloud</groupId>
      <artifactId>spring-cloud-stream-dependencies</artifactId>
      <version>${spring-cloud-stream.version}</version>
      <type>pom</type>
      <scope>import</scope>
    </dependency>
  </dependencies>
    </dependencyManagement>
```

在<repository>节点添加：

```xml
<repository>
  <id>spring-milestones</id>
  <name>Spring Milestones</name>
  <url>http://repo.spring.io/libs-milestone</url>
  <snapshots>
    <enabled>false</enabled>
  </snapshots>
</repository>
```

定义kafka stream

```java
package demo.streamkafka.stream;

import org.springframework.cloud.stream.annotation.Input;
import org.springframework.cloud.stream.annotation.Output;
import org.springframework.messaging.MessageChannel;
import org.springframework.messaging.SubscribableChannel;  

public interface GreetingsStreams {
    String INPUT = "input";
    String OUTPUT = "output";

    @Input(INPUT)
    SubscribableChannel inboundGreetings();

    @Output(OUTPUT)
    MessageChannel outboundGreetings();
}
```

这里分别定义了一个输出流和一个输入流：

- outboundGreetings：输出流，它用于把消息写入Kafka的topic里
- inboundGreetings：输入流，它用于消费kafka的消息。

Spring会用一个Java代理来试下GreetingsStreams接口。

### 配置Spring Cloud Stream

接着我们需要配置Spring Cloud Stream来绑定stream到GreetingsStreams：

```java
package demo.streamkafka.config;

import demo.streamkafka.stream.GreetingsStreams;
import org.springframework.cloud.stream.annotation.EnableBinding;

@EnableBinding(GreetingsStreams.class)
public class StreamsConfig {
}
```

使用注释@EnableBinding启动绑定。

### 配置Kafka属性

spring boot的默认配置文件为src/main/resources/application.properties，或者是一个application.yaml。

使用application.yaml配置如下：

```
spring:
  cloud:
    stream:
      kafka:
        binder:
          brokers: localhost:9092
      bindings:
        greetings-in:
          destination: greetings
          contentType: application/json
        greetings-out:
          destination: greetings
          contentType: application/json
```

配置文件里设置了：

- kafka服务器的连接地址
- kafka的topic为greetings
- 发送消息的contentType为json

### 新建消息模型

```java
package demo'.streamkafka.model;

public class Greetings {
    private long timestamp;
    private String message;
    //get/set方法
}
```

### 在Service层写消息到Kafka

```java
package demo.streamkafka.service;

import demo.streamkafka.model.Greetings;
import demo.streamkafka.stream.GreetingsStreams;
import org.springframework.messaging.MessageChannel;
import org.springframework.messaging.MessageHeaders;
import org.springframework.messaging.support.MessageBuilder;
import org.springframework.stereotype.Service;
import org.springframework.util.MimeTypeUtils;

@Service
public class GreetingsService {
    private final GreetingsStreams greetingsStreams;

    public GreetingsService(GreetingsStreams greetingsStreams) {
        this.greetingsStreams = greetingsStreams;
    }

    public void sendGreeting(final Greetings greetings) {

        MessageChannel messageChannel = greetingsStreams.outboundGreetings();
        messageChannel.send(MessageBuilder
                .withPayload(greetings)
                .setHeader(MessageHeaders.CONTENT_TYPE, MimeTypeUtils.APPLICATION_JSON)
                .build());
    }
```

在sendGreeting()方法接收消息对象Greetings，使用messageChannel来发送消息。

触发写消息Rest API

使用spring mvc来创建一个RestController，它提供一个Rest API让我们触发写消息到Kafka。GreetingsController会调用GreetingsService来发送消息。

```java
package demo.streamkafka.web;

import demo.streamkafka.model.Greetings;
import demo.streamkafka.service.GreetingsService;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestController; 

@RestController
public class GreetingsController {
    private final GreetingsService greetingsService;

    public GreetingsController(GreetingsService greetingsService) {
        this.greetingsService = greetingsService;
    }

    @GetMapping("/greetings")
    @ResponseStatus(HttpStatus.ACCEPTED)
    public void greetings(@RequestParam("message") String message) {
        Greetings greetings = Greetings.builder()
            .message(message)
            .timestamp(System.currentTimeMillis())
            .build();

        greetingsService.sendGreeting(greetings);
    }
}
```

### 监听kafka的topic

GreetingsListener 是一个监听器，它用来监听kafka的主题是否有消息。

```java
package demo.streamkafka.service;

import demo.streamkafka.model.Greetings;
import demo.streamkafka.stream.GreetingsStreams;
import org.springframework.cloud.stream.annotation.StreamListener;
import org.springframework.messaging.handler.annotation.Payload;
import org.springframework.stereotype.Component;

@Component
public class GreetingsListener {
    @StreamListener(GreetingsStreams.INPUT)
    public void handleGreetings(@Payload Greetings greetings) {
        System.out.println("Received greetings: " +  greetings);
    }
}
```

StreamListener为GreetingsStreams.INPUT。如果有消息进入kafka就会被GreetingsListener监听到，并在handleGreetings()处理消费消息。

### 启动应用

最后就是要实现一个Spring Boot的Application用于启动应用。

```java
package demo.streamkafka;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class StreamKafkaApplication {

    public static void main(String[] args) {
        SpringApplication.run(StreamKafkaApplication.class, args);
    }
}
```

到此就完成了一个简单的kafka消息流处理。使用rest api可以触发消息的发送。