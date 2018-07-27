哪种代理适合用于Web数据采集

发布时间：2013-01-14 来源：未知 浏览：

[新动态](http://weibo.com/u/5581662372)

------

在Web数据采集中为了避免被服务器封锁而通过代理下载的情况很常见。但是，并非所有的代理都适合于Web数据采集。下面是鲲鹏数据的技术人员给出的说明。

根据HTTP代理的匿名性可以将其分为以下几种：

 

**1. 透明代理（Transparent Proxies）**

目标服务器能够检测到真实的源IP。

 

目标服务器根据HTTP请求头进行检测，判断依据：

REMOTE_ADDR = 代理服务器 IP

HTTP_VIA = 通常为代理服务器 IP（或代理软件名称，也可能无此头）

HTTP_X_FORWARDED_FOR = 真实源IP（不用代理时，无此头或值为空）

PS：该类型代理不适合用于Web数据采集。

 

**2. （普通）匿名代理（Anonymous Proxies）**

目标服务器无法检测到真实的源IP，但能够检测到使用了代理。

 

检测依据：

REMOTE_ADDR = 代理服务器 IP

HTTP_VIA = 通常为代理服务器 IP（或代理软件名称，也可能无此头）

HTTP_X_FORWARDED_FOR = 代理服务器 IP（知道你使用了代理，但无法得知真实源IP）

PS：该类型代理可以用于Web数据采集，但有被检测到的风险。

 

**3. 高匿名代理（High Anonymity Proxies -Elite proxies**）

目标服务器无法检测到你在是使用代理。

 

检测依据：

REMOTE_ADDR = 代理服务器 IP

HTTP_VIA = 值为空或无此头

HTTP_X_FORWARDED_FOR = 没数值或无此头

PS：该类型的代理非常适合用户Web数据采集。鲲鹏数据的付费代理方案提供的全部为高匿名类型的代理。

 

另外，不使用代理时发出的头：

REMOTE_ADDR =真实源 IP

HTTP_VIA = 值为空或无此头

HTTP_X_FORWARDED_FOR = 没数值或无此头

 

不过，在检测严格的情况下，即使没有HTTP_VIA头和HTTP_X_FORWARDED_FOR头，如果存在HTTP_PROXY_CONNECTION头，会被认为在使用普通匿名代理。

 

我们提供了一个代理类型检测接口，在浏览器中访问该接口即可显示出你当前使用的代理类型（如下图）：

<http://proxies.site-digger.com/proxy-detect/>

 

![img](http://www.site-digger.com/uploads/allimg/130114/1_130114000818_1.gif)

 

西安鲲之鹏提供多种高匿稳定HTTP代理解决方案，详情请查看这里<http://www.site-digger.com/html/proxies.html>