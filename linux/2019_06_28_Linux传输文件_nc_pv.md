# Linux 传输文件-nc+pv

 发表于 2018-05-13 |  更新于 2019-06-17 |  分类于 [Linux使用](https://sjq597.github.io/categories/Linux%E4%BD%BF%E7%94%A8/)

做数据的写代码多了,会经常碰到传输文件的需求,之前还好，一般是下载文件,直接用python内置的server起个服务就搞定了.但是对于跨机房有防火墙存在的情况，一般数据是单向的，就是假设(A–>B)A作为HTTPServer,B可以下载文件.但是反过来就不好使了，因为防火墙策略没有开,(B–>A)用B作为HTTPServer,A无法访问到服务.所以这个时候,A仍然得作为服务端,主要有两种不同的方式.

- nc传输文件

1.Data Transfer模式:A(sender/client)->B(receiver/server)
数据Transfer模式简单来说就是在家等着收数据，可以理解为被动模式.所以`receiver`监听的是本机的端口,然后等着`sender`会把数据发送到这个地方.

```
A(sender): tar -zcvf - file/directory | nc -l {B_IP} 12345
B(receiver): nc -l 12345 | sudo tar -zxvf -
```

**PS:**`receiver`端先启动,然后启动`sender`发送数据.如果是想`B->A`传输,对调一下就行,注意服务的开启顺序

2.Data Take模式:A(sender/server)->B(receiver/client)
数据的Take模式和Transfer有一点不大一样,可以理解为主动模式.就是你得自己去指定机器上主动取数据.所以`sender`会把数据发送到本机指定端口,`receiver`从指定机器以及端口获取数据

```
A(sender): nc -l 12345 < file/directory
B(receiver): nc {A_IP} 12345 > file/directory
```

**PS:**`sender`端先启动,然后启动`receiver`接收数据.注意和第一种方式区分

上面两种传输方式虽然有一点不大一样,不过有一个共同点就是:`server`一定要先启动,然后才是`client`端才启动.但是不管是哪种方式，只要记住一点,就是`client`对`server`提供服务端`port`一定是通的,比如说本机可以访问服务器指定端口的服务,但是服务器就无法访问本机指定端口服务，所以不管是想从服务器拷贝数据还是发送数据到服务器,服务器只能是`server`.

- 配合pv使用

pv我就不介绍是啥了,这个小工具也非常的好用,因为一般传输大文件的时候，我们希望看到传输进度啊,速度啊之类的,还有一个很重要的功能就是限速,尤其是专线跨机房问题.
A:pv -p -r -L 10m heap.bin | nc -l 9099
B:nc {A_IP} 9099 > heap.bin
常用参数:

```
-p, --progress           show progress bar
-r, --rate               show data transfer rate counter
-L, --rate-limit RATE    limit transfer to RATE bytes per second
```