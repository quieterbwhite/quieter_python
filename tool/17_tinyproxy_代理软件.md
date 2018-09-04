# Ubuntu下使用TinyProxy搭建HTTP代理服务器

[![img](https://s5.51cto.com//wyfs02/M00/8D/01/wKiom1iBh4uj9BSqAAAjAYBpOIQ343_middle.jpg)](http://blog.51cto.com/tong707)ngle



2017-12-16 17:23:33

一、安装

安装TinyProxy

```shell
sudo apt-get install tinyproxy -y
```

安装完成后自动以root限权开启代理服务，默认监听8888

二、配置TinyProxy

```shell
vim /etc/tinyproxy.conf
```

1） 修改TinyProxy默认监听端口：

![image.png](http://s1.51cto.com/images/20171216/1513414418634956.png?x-oss-process=image/watermark,size_16,text_QDUxQ1RP5Y2a5a6i,color_FFFFFF,t_100,g_se,x_10,y_10,shadow_90,type_ZmFuZ3poZW5naGVpdGk=)

2） 修改监听网卡：

如果有多个网卡，可以绑定到其中的一个网卡上。

如果此行被注释掉，TinyProxy将绑定到当前所有网卡。

![image.png](http://s1.51cto.com/images/20171216/1513414957761953.png?x-oss-process=image/watermark,size_16,text_QDUxQ1RP5Y2a5a6i,color_FFFFFF,t_100,g_se,x_10,y_10,shadow_90,type_ZmFuZ3poZW5naGVpdGk=)

3） 修改流量出口：

这允许您指定用于传出连接的网卡。

这对于多台家用机器来说是非常有用的，因为你希望所有的流量都能从一个特定的接口显示出来。

![image.png](http://s1.51cto.com/images/20171216/1513415393998959.png?x-oss-process=image/watermark,size_16,text_QDUxQ1RP5Y2a5a6i,color_FFFFFF,t_100,g_se,x_10,y_10,shadow_90,type_ZmFuZ3poZW5naGVpdGk=)

4） 修改允许连接的网络（默认只有127.0.0.1）：

![image.png](http://s1.51cto.com/images/20171216/1513415505851498.png?x-oss-process=image/watermark,size_16,text_QDUxQ1RP5Y2a5a6i,color_FFFFFF,t_100,g_se,x_10,y_10,shadow_90,type_ZmFuZ3poZW5naGVpdGk=)

三、重启TinyProxy服务，使配置生效

```shell
sudo service tinyproxy restart
```

四、修改客户端配置，配置Internet代理

![image.png](http://s1.51cto.com/images/20171216/1513415868460850.png?x-oss-process=image/watermark,size_16,text_QDUxQ1RP5Y2a5a6i,color_FFFFFF,t_100,g_se,x_10,y_10,shadow_90,type_ZmFuZ3poZW5naGVpdGk=)

![image.png](http://s1.51cto.com/images/20171216/1513415899860274.png?x-oss-process=image/watermark,size_16,text_QDUxQ1RP5Y2a5a6i,color_FFFFFF,t_100,g_se,x_10,y_10,shadow_90,type_ZmFuZ3poZW5naGVpdGk=)

![image.png](http://s1.51cto.com/images/20171216/1513416162345007.png?x-oss-process=image/watermark,size_16,text_QDUxQ1RP5Y2a5a6i,color_FFFFFF,t_100,g_se,x_10,y_10,shadow_90,type_ZmFuZ3poZW5naGVpdGk=)

 