### 参考链接


#### 验证码限制
> https://www.cnblogs.com/zeze/p/6408649.html 

在访问频率较高的情况下会出现访问页面需要输入验证码，如下图：

此验证码的生成方式为动态验证码，即每次访问一次验证码生成链接，生成的验证码都不一样，验证码动态生成链接为：http://wenshu.court.gov.cn/User/ValidateCode

在采集器中如果要进行验证码的识别，需要先下载该验证码的图片，下载需要访问一次该验证码链接，此时的验证码与实际的验证码图片已经不是同一张了，即便识别成功，也会报验证码填入错误。

#### 封IP限制

我们人工模拟采集器采集页面，同一个IP，当访问频率达到一定程度时，该网站会直接拒绝访问

> https://www.jianshu.com/p/da54d322ba31 中国裁判文书网全网最新爬虫分析  