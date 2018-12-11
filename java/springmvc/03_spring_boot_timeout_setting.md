#### [SpringBoot 超时设置](https://www.cnblogs.com/hongdada/p/9628923.html)

#### 1.RestTemplate超时

###### 设置配置HttpComponentsClientHttpRequestFactory中的RequestConfig属性

RestTemplateConfig：

```
import lombok.extern.slf4j.Slf4j;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.http.client.HttpComponentsClientHttpRequestFactory;
import org.springframework.web.client.RestTemplate;

/**
 * Created by qhong on 2018/9/10 17:53
 **/
@Slf4j
@Configuration
public class RestTemplateConfig {

    @Bean
    @ConfigurationProperties(prefix = "rest.connection")
    public HttpComponentsClientHttpRequestFactory httpRequestFactory() {
        return new HttpComponentsClientHttpRequestFactory();
    }

    @Bean
    public RestTemplate customRestTemplate(){
        return new RestTemplate(httpRequestFactory());
    }
}
```

application.properties:

```
#restTemplate配置
rest.connection.connectionRequestTimeout=30000
rest.connection.connectTimeout=30000
rest.connection.readTimeout=30000
```

或者：

```
#restTemplate配置
rest.connection.connection-request-timeout=30000
rest.connection.connect-timeout=30000
rest.connection.read-timeout=30000
```

上面这两种格式的配置都可以。

##### 参考：

<https://blog.csdn.net/wtopps/article/details/80990464>

<https://www.cnblogs.com/yangzhilong/p/6640207.html>

<https://www.jianshu.com/p/60174c9eb735>

<https://github.com/jadyer/seed/blob/master/seed-boot/src/main/java/com/jadyer/seed/boot/RestTemplateConfiguration.java>

------

#### 2.HttpUrlConnection超时

##### 参考：

<http://ju.outofmemory.cn/entry/23483>

<http://m635674608.iteye.com/blog/2265958>