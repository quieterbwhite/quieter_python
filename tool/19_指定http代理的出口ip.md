#### 在多网络接口(IP)环境下Squid，Tinyproxy和DeleGate如何指定出口(IP)

发布时间：2018-04-25 来源：未知 浏览：

> http://www.site-digger.com/html/articles/20180425/143.html

[新动态](http://weibo.com/u/5581662372)

------

在多网络接口（即多IP）环境下，如何设置代理程序使用的出口（IP）呢？

这里的出口（IP）指的是代理程序访问目标网站的时候采用的接口（IP），就是目标网站能够检测到的访问者IP。默认情况下，代理程序都是走的默认路由（接口）。

本文的前提是你已经设置好了路由规则，每个接口（IP）都能正常的工作了，如何你还不清楚如何设置多IP环境下的路由，可以参考这篇文章：<http://www.plugged.in/linux/add-multiple-gateways-multiple-nics-ubuntu-server.html>

**1. Squid**

Squid无疑是Linux下代理软件的王者，以功能强大和稳定闻名天下。它提供了tcp_outgoing_address选项，用于指定使用特定的出口IP。

直接看官方文档（<http://www.squid-cache.org/Doc/config/tcp_outgoing_address/>）里面的例子（如下）：

[view plain](http://www.site-digger.com/html/articles/20180425/143.html#)[copy to clipboard](http://www.site-digger.com/html/articles/20180425/143.html#)[print](http://www.site-digger.com/html/articles/20180425/143.html#)[?](http://www.site-digger.com/html/articles/20180425/143.html#)

1. acl normal_service_net src 10.0.0.0/24  
2. acl good_service_net src 10.0.2.0/24  
3.   
4. tcp_outgoing_address 10.1.0.1 normal_service_net  
5. tcp_outgoing_address 10.1.0.2 good_service_net  

不难理解，目的是让：来自接口10.0.0.0/24段的请求，通过10.1.0.1接口访问目标网站；来自接口10.0.2.0/24段的请求，通过 10.1.0.2接口访问目标网站。

**2. Tinyproxy**

Tinyproxy的主页在这里：[http://tinyproxy.github.io](http://tinyproxy.github.io/)，源码在这里：<https://github.com/tinyproxy/tinyproxy>。

它的特定是简单易用，不需要复杂的配置，它的参数也很容易理解。

它提供了一个BindSame参数，当其值为yes时，出口将采用和入口相同的IP。例如，服务器上存在某IP 61.134.1.4，当你请求该IP对应的Tinyproxy代理时，Tinyproxy也通过61.134.1.4出口访问目标网站。

**3. DeleGate**

好多人对DeleGate不熟悉，但是它功能异常强大，它不但支持HTTP协议，还支持FTP,  SMTP, POP, IMAP, Telnet, SOCKS, DNS等多种协议。它的主页是：<http://delegate.hpcc.jp/delegate/>。

由于网上DeleGate相关的资料比较少，加之它的文档（<http://delegate.hpcc.jp/delegate/Manual.shtml>）比较复杂，在很长的一段时间里我们都以为它不支持指定出口IP。抱着试试的态度给作者发了个邮件咨询该问题，没想到作者竟然给回复了。那就是使用SRCIF参数（<http://delegate.hpcc.jp/delegate/Manual.shtml?SRCIF>），例如，如下是一个启动DeleGate代理完整的命令行实例：

[view plain](http://www.site-digger.com/html/articles/20180425/143.html#)[copy to clipboard](http://www.site-digger.com/html/articles/20180425/143.html#)[print](http://www.site-digger.com/html/articles/20180425/143.html#)[?](http://www.site-digger.com/html/articles/20180425/143.html#)

1. ./delegate -P117.40.5.183:8888 SERVER=http PERMIT="*:*:*"  AUTHORIZER="-list{test:test}" AUTH=viagen:- ADMIN="redice@163.com" SRCIF="117.40.5.183:*:*:*:*"  

DeleGate监听117.40.5.183:8888，并且使用117.40.5.183访问目标网站(SRCIF参数限定出口IP)。

下面是两次对比测试的截图：

所在机器的默认路由接口对应的IP是182.84.192.214。

**图1** - 没有使用SRCIF参数指定出口IP。DeleGate代理使用了默认的路由出口访问目标网站（http://httpbin.org/ip），和不使用代理时返回的IP一样，都是182.84.192.214；

![delegate没有使用SRCIF参数限定出口IP时测试截图](http://www.site-digger.com/uploads/allimg/201804/delegate_no_srcif.png)

图2 - 使用SRCIF参数指定了出口IP为117.40.5.183（和监听的IP相同），DeleGate代理使用了117.40.5.183访问目标网站(http://httpbin.org/ip)，返回的IP是117.40.5.183。

![delegate使用了SRCIF参数限定出口IP时测试截图](http://www.site-digger.com/uploads/allimg/201804/delegate_with_srcif.png)

顺便说一下，Squid，Tinyproxy以及DeleGate都是开源的。