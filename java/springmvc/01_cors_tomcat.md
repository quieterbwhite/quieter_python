# Enable CORS on Tomcat 8.0.30
> https://stackoverflow.com/questions/38354664/enable-cors-on-tomcat-8-0-30  

## SimpleCORSFilter.java
```java
import java.io.IOException;

import javax.servlet.Filter;
import javax.servlet.FilterChain;
import javax.servlet.FilterConfig;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;
import javax.servlet.http.HttpServletResponse;

public class SimpleCORSFilter implements Filter {

    public void doFilter(ServletRequest req, ServletResponse res, FilterChain chain) throws IOException, ServletException {
        HttpServletResponse response = (HttpServletResponse) res;
        response.setHeader("Access-Control-Allow-Origin", "*");
        response.setHeader("Access-Control-Allow-Methods", "POST, GET, OPTIONS, DELETE");
        response.setHeader("Access-Control-Max-Age", "3600");
        response.setHeader("Access-Control-Allow-Headers", "Content-Type, x-requested-with, X-Custom-Header, Authorization, token");
        chain.doFilter(req, res);
    }

    public void destroy() {
        // TODO Auto-generated method stub

    }

    public void init(FilterConfig arg0) throws ServletException {
        // TODO Auto-generated method stub

    }

}
```

## web.xml
```xml
<!--放到web.xml中，filter的最前面 -->

<filter>
    <filter-name>SimpleCORSFilter</filter-name>
    <filter-class>com.example.util.SimpleCORSFilter</filter-class>
</filter>
<filter-mapping>
    <filter-name>SimpleCORSFilter</filter-name>
    <url-pattern>/*</url-pattern>
</filter-mapping>
```
