### fiddler抓取小程序和app的https数据包

2018年12月27日 09:17:47 [栁罗风尘](https://me.csdn.net/wujiangwei567) 阅读数：351

>   https://blog.csdn.net/wujiangwei567/article/details/85272283

### 文章目录

-   -   -   [1.下载并安装fiddler](https://blog.csdn.net/wujiangwei567/article/details/85272283#1fiddler_3)

        -   [2. 配置fiddler](https://blog.csdn.net/wujiangwei567/article/details/85272283#2_fiddler_7)

        -   [3.手机端设置](https://blog.csdn.net/wujiangwei567/article/details/85272283#3_24)

        -   -   [3.1 设置wifi网段](https://blog.csdn.net/wujiangwei567/article/details/85272283#31_wifi_25)
            -   [3.2 安装证书](https://blog.csdn.net/wujiangwei567/article/details/85272283#32___31)
            -   [3.3 设置证书为信任证书](https://blog.csdn.net/wujiangwei567/article/details/85272283#33__39)

        -   [4. 查看抓包](https://blog.csdn.net/wujiangwei567/article/details/85272283#4__45)

>   很多时候，我们的api接口不能经过浏览器查看网络请求，来获取数据包以及相关的接口返回，这时候就需要使用抓包工具，个人比较喜欢使用 `fiddler` ,当然也有其他的，这里说明一下怎么使用 `fiddler`，以及怎么抓取`https`数据包，本文的 `pc`环境是 `windows` 移动设备是`iphone`

### 1.下载并安装fiddler

>   下载地址 ： <https://www.telerik.com/download/fiddler>

### 2. 配置fiddler

>   依次选择菜单 `tools` —> `options`
>   并按照 如下图配置

![在这里插入图片描述](https://img-blog.csdnimg.cn/20181227090430647.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3d1amlhbmd3ZWk1Njc=,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20181227090448391.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3d1amlhbmd3ZWk1Njc=,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20181227090457204.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3d1amlhbmd3ZWk1Njc=,size_16,color_FFFFFF,t_70)

>   这里需要安装一下证书：
>   下载fiddler证书地址：<https://www.telerik.com/fiddler/add-ons>

![在这里插入图片描述](https://img-blog.csdnimg.cn/20190102150925465.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3d1amlhbmd3ZWk1Njc=,size_16,color_FFFFFF,t_70)

>   下载完成后，按照步骤一步步安装，然后重启fiddler即可，否则手机端访问可能会出现如下错误：
>   Have you enabled HTTPS traffic decryption in Fiddler yet?

### 3.手机端设置

#### 3.1 设置wifi网段

>   step1 `设置` — `无线局域网` — 与电脑fiddler同网段的wifi

>   step2 滑到最底部 `配置代理` — `手动` — 你的fiddler所在电脑 `ip` + 刚刚配置的`7888`端口号
>   不需要勾选鉴定 — 保存

#### 3.2 安装证书

>   step1 打开 safari浏览器 输入地址 : `192.168.0.97:7888` 访问
>   这里的 `192.168.0.97` 是你fiddler所在电脑的 `ip`

>   step2 点击底部的 `FiddlerRoot certificate` 下载并安装

![在这里插入图片描述](https://img-blog.csdnimg.cn/20181227090657762.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3d1amlhbmd3ZWk1Njc=,size_16,color_FFFFFF,t_70)

#### 3.3 设置证书为信任证书

>   选择信任证书 `通用`— `关于本机` — `证书信任设置`
>   开启刚刚下载的证书

![在这里插入图片描述](https://img-blog.csdnimg.cn/20181227090929721.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3d1amlhbmd3ZWk1Njc=,size_16,color_FFFFFF,t_70)

### 4. 查看抓包

>   重启`fiddler` ，依次选择 `Inspectors` ---- 选中访问的接口连接 ----- `WebView`

![在这里插入图片描述](https://img-blog.csdnimg.cn/201812270915002.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3d1amlhbmd3ZWk1Njc=,size_16,color_FFFFFF,t_70)

原文参考：[我的博客](http://blog.chaifei.pw/article/72)