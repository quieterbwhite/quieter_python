### APP 抓包和微信小程序抓包-Charles 的精简使用教程

2018年10月11日 16:11:55 

标签： [抓包](https://so.csdn.net/so/search/s.do?q=%E6%8A%93%E5%8C%85&t=blog)[手机抓包](https://so.csdn.net/so/search/s.do?q=%E6%89%8B%E6%9C%BA%E6%8A%93%E5%8C%85&t=blog)[移动项目抓包](https://so.csdn.net/so/search/s.do?q=%E7%A7%BB%E5%8A%A8%E9%A1%B9%E7%9B%AE%E6%8A%93%E5%8C%85&t=blog)[Charles](https://so.csdn.net/so/search/s.do?q=Charles&t=blog) 更多

个人分类： [Charles](https://blog.csdn.net/liqing0013/article/category/8117456)[抓包](https://blog.csdn.net/liqing0013/article/category/8117457)

 版权声明：本文为博主原创文章，未经博主允许不得转载。	https://blog.csdn.net/liqing0013/article/details/83010531

### APP 抓包和微信小程序抓包-Charles 的精简使用教程

-   [2019-03-18 更新](https://blog.csdn.net/liqing0013/article/details/83010531#20190318__1)

-   [目标](https://blog.csdn.net/liqing0013/article/details/83010531#_4)

-   [教程](https://blog.csdn.net/liqing0013/article/details/83010531#_8)

-   -   [一、安装 Charles](https://blog.csdn.net/liqing0013/article/details/83010531#_Charles_9)

    -   [二、Charles 简介](https://blog.csdn.net/liqing0013/article/details/83010531#Charles__11)

    -   -   [（1）Charles 欢迎页面](https://blog.csdn.net/liqing0013/article/details/83010531#1Charles__12)
        -   [（2）基础功能按钮](https://blog.csdn.net/liqing0013/article/details/83010531#2_14)
        -   [（3）抓包内容显示方式](https://blog.csdn.net/liqing0013/article/details/83010531#3_16)
        -   [（4）过滤抓包内容](https://blog.csdn.net/liqing0013/article/details/83010531#4_19)

    -   [三、手机配置 Charles 代理](https://blog.csdn.net/liqing0013/article/details/83010531#_Charles__23)

    -   [四、解决配置 Charles 代理之后手机无法上网的问题](https://blog.csdn.net/liqing0013/article/details/83010531#_Charles__28)

    -   [五、手机 APP 抓包](https://blog.csdn.net/liqing0013/article/details/83010531#_APP__33)

    -   -   [（1）对 “花生地铁” APP 进行抓包。](https://blog.csdn.net/liqing0013/article/details/83010531#1___APP___34)

    -   [六、微信小程序抓包](https://blog.csdn.net/liqing0013/article/details/83010531#_39)

    -   -   [（1）安装 SSL 证书](https://blog.csdn.net/liqing0013/article/details/83010531#1_SSL__40)

        -   -   [1、Charles 上安装 SSL 证书](https://blog.csdn.net/liqing0013/article/details/83010531#1Charles__SSL__42)
            -   [2、手机安装 SSL 证书](https://blog.csdn.net/liqing0013/article/details/83010531#2_SSL__46)

        -   [（2）配置 Charles 的 SSL](https://blog.csdn.net/liqing0013/article/details/83010531#2_Charles__SSL_62)

        -   [（3）对微信小程序“猫眼电影”进行抓包](https://blog.csdn.net/liqing0013/article/details/83010531#3_68)

    -   [总结](https://blog.csdn.net/liqing0013/article/details/83010531#_71)

#### 2019-03-18 更新

-   亲测，（SSL）抓取微信小程序 猫眼电影 的数据仍然成功。请没有成功的小伙伴们耐心检查一下自己的配置。
-   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20190318150617301.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xpcWluZzAwMTM=,size_16,color_FFFFFF,t_70)![在这里插入图片描述](https://img-blog.csdnimg.cn/20190318150510519.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xpcWluZzAwMTM=,size_16,color_FFFFFF,t_70)

# 目标

-   抓取移动端项目的前端页面和后台的交互数据，对请求信息和响应内容进行分析。
    -   普通手机 APP 的前端页面和后台一般是通过 **HTTP** 请求进行交互。
    -   微信小程序的前端页面和后台一般是通过 **HTTPS** 请求进行交互。

# 教程

## 一、安装 Charles

在[官方网站](https://www.charlesproxy.com/)下载最新的安装包，然后点击运行，在弹出的安装向导中，根据提示进行操作即可顺利完成安装。过程很简单，所以这里进行不详细介绍。当前最新的版本是 charles-proxy-4.2.7-win64.msi 。

## 二、Charles 简介

### （1）Charles 欢迎页面

-   运行 Charles 之后，默认打开的欢迎页如下图所示：![在这里插入图片描述](https://img-blog.csdn.net/20181011115129803?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xpcWluZzAwMTM=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

### （2）基础功能按钮

需要关注两个按钮：清空抓包内容按钮和抓包开关按钮：![在这里插入图片描述](https://img-blog.csdn.net/20181011115828821?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xpcWluZzAwMTM=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

### （3）抓包内容显示方式

-   **Sequence** 形式。可以看到全部请求，默认以数据请求的顺序来显示，最新的请求显示在最下面。如下图所示：![在这里插入图片描述](https://img-blog.csdn.net/20181011142313305?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xpcWluZzAwMTM=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
-   **Structure** 形式。可以很清晰的看到请求的数据结构，请求信息根据域名划分。具体如下图所示：![在这里插入图片描述](https://img-blog.csdn.net/20181011142533559?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xpcWluZzAwMTM=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

### （4）过滤抓包内容

-   通过 filter 框 进行过滤（推荐使用）。不管是Sequence 还是 Structure 显示方式，都可以通过下方的 filter 框进行过滤：![在这里插入图片描述](https://img-blog.csdn.net/20181011143345748?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xpcWluZzAwMTM=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
    ![在这里插入图片描述](https://img-blog.csdn.net/20181011143406807?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xpcWluZzAwMTM=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
-   通过 Recording Settings 设置过滤条件。具体如下图：![在这里插入图片描述](https://img-blog.csdn.net/20181011143748634?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xpcWluZzAwMTM=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

## 三、手机配置 Charles 代理

-   需要手机和运行 Charles 的电脑在同一个局域网内。
-   启动 Charles，点击 Proxy-Proxy Settings，查看代理端口：![在这里插入图片描述](https://img-blog.csdn.net/20181011111452153?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xpcWluZzAwMTM=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
-   在命令提示符窗口，执行 ipconfig ，查看电脑的IP：![在这里插入图片描述](https://img-blog.csdn.net/20181011111710806?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xpcWluZzAwMTM=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
-   在手机连接的 WLAN 中，设置代理信息。从前两步中，可以看到Charles 的代理端口为 8888，电脑IP为 192.168.1.101。![在这里插入图片描述](https://img-blog.csdn.net/20181011112337758?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xpcWluZzAwMTM=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

## 四、解决配置 Charles 代理之后手机无法上网的问题

如果代理配置完成之后，出现手机无法上网的情况。![在这里插入图片描述](https://img-blog.csdn.net/20181011112804231?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xpcWluZzAwMTM=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
需要检查下面几个地方：

-   检查防火窗。我用的是 win 10 。![在这里插入图片描述](https://img-blog.csdn.net/20181011113332904?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xpcWluZzAwMTM=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
-   检查 Charles 黑白名单。如果没有特别需要可以关闭黑白名单功能。![在这里插入图片描述](https://img-blog.csdn.net/20181011114117851?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xpcWluZzAwMTM=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)![在这里插入图片描述](https://img-blog.csdn.net/20181011114248506?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xpcWluZzAwMTM=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

## 五、手机 APP 抓包

### （1）对 “花生地铁” APP 进行抓包。

-   打开 花生地铁 APP（广州的朋友应该都用过吧）：
    ![在这里插入图片描述](https://img-blog.csdn.net/20181011144848798?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xpcWluZzAwMTM=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
-   查看抓包内容：
    ![在这里插入图片描述](https://img-blog.csdn.net/20181011144916922?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xpcWluZzAwMTM=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

## 六、微信小程序抓包

### （1）安装 SSL 证书

由于微信小程序的前端页面和后台交互，基本上都是基于 HTTPS ，所以需要先安装 SSL 证书。![在这里插入图片描述](https://img-blog.csdn.net/20181011145547819?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xpcWluZzAwMTM=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

#### 1、Charles 上安装 SSL 证书

-   通过 Help->SSL Proxying->Install Charles Root Certificate 打开证书安装窗口：
-   ![在这里插入图片描述](https://img-blog.csdn.net/2018101115053964?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xpcWluZzAwMTM=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
-   根据安装向导的提示，全部采用默认的选项，最后完成安装：![在这里插入图片描述](https://img-blog.csdn.net/20181011150754128?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xpcWluZzAwMTM=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

#### 2、手机安装 SSL 证书

-   Charles 建议的安装方法。
    -   通过 Help->SSL Proxying->Install Charles Root Certificate On a mobile device ，可以看到以下提示：![在这里插入图片描述](https://img-blog.csdn.net/2018101115143928?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xpcWluZzAwMTM=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
    -   根据提示，应该进行如下操作：
        -   手机配置 Charles 代理。上面已经介绍，这里不再赘述。
        -   在手机浏览上访问：<http://chls.pro/ssl> ，下载并安装证书。
        -   大致流程如下：![在这里插入图片描述](https://img-blog.csdn.net/20181011151927999?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xpcWluZzAwMTM=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
            ![在这里插入图片描述](https://img-blog.csdn.net/20181011151945190?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xpcWluZzAwMTM=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
        -   遗憾的是，有些品牌的手机，比如小米手机，不支持通过 getssl.crt 安装证书。
        -   ![在这里插入图片描述](https://img-blog.csdn.net/20181011152252251?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xpcWluZzAwMTM=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
-   其他方法。
    -   如果上面的方法不能成功安装证书，可以在电脑浏览器上访问 [http://chls.pro/ssl，下载](http://chls.pro/ssl%EF%BC%8C%E4%B8%8B%E8%BD%BD) charles-proxy-ssl-proxying-certificate.pem，并传手机上进行安装。![在这里插入图片描述](https://img-blog.csdn.net/20181011152918943?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xpcWluZzAwMTM=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
    -   在手机中，把文件的后缀名改成 .crt:![在这里插入图片描述](https://img-blog.csdn.net/20181011154943406?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xpcWluZzAwMTM=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
    -   点击 .crt 文件，进行证书安装：![在这里插入图片描述](https://img-blog.csdn.net/20181011155034333?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xpcWluZzAwMTM=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
    -   安装完成之后，在系统安全-加密与凭据-信任的凭据中，可以看到刚刚安装的证书：
    -   ![在这里插入图片描述](https://img-blog.csdn.net/2018101115522239?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xpcWluZzAwMTM=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

### （2）配置 Charles 的 SSL

-   通过 Proxy-SSL Proxy Settings 打开窗口：![在这里插入图片描述](https://img-blog.csdn.net/20181011155700773?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xpcWluZzAwMTM=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

-   在弹出的窗口中，选择 Enable SSL Proxy，并设置要代理的域名。本示例是要对微信小程序“猫眼电影”抓包，所以配置了 [api.maoyan.com](http://api.maoyan.com/) 和 [ad.maoyan.com](http://ad.maoyan.com/)。

-   如果要匹配的域名比较多，配置麻烦，可以不填域名和端口内容，直接点击OK

    -   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20190322154716545.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xpcWluZzAwMTM=,size_16,color_FFFFFF,t_70)
    -   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20190322154735764.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xpcWluZzAwMTM=,size_16,color_FFFFFF,t_70)

-   ### （3）对微信小程序“猫眼电影”进行抓包

-   在微信钱包-第三方服务中，打开“猫眼电影”。![在这里插入图片描述](https://img-blog.csdn.net/20181011160611138?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xpcWluZzAwMTM=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

-   查看 Charles 中的抓包情况：![在这里插入图片描述](https://img-blog.csdn.net/20181011160643631?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xpcWluZzAwMTM=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

## 总结

一个精简的 Charles 教程到此结束。
如果有什么问题，希望可以给我留言。
最后祝大家工作顺利。