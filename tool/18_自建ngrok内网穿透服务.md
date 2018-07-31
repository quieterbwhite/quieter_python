## 自建 ngrok 内网穿透服务

> http://www.zhaojun.im/ngrok/
>
> http://linfuyan.com/ubuntu-ngrok/

 发表于 2018-04-14 |  更新于 2018-07-08 | 

`ngrok` 和 `内网穿透` 是什么，有啥用处，以及为什么自建服务，这里我就不再多说了，相信点进来的人也不需要我解释这些。

## 准备工作

- 有公网 IP 的 VPS 一台
- 可以配置域名解析的域名一个。
- 系统：CentOS （也可为其他，命令稍有不同）

## 配置域名解析

先把域名给配置了，比如我的域名是 `zhaojun.im`，那么建立 `ngrok.zhaojun.im` 和 `*.ngrok.zhaojun.im` 解析到 你的 VPS 的 IP 上 (A 记录)。

[![img](https://cdn.jun6.net/201804141548_627.png)](https://cdn.jun6.net/201804141548_627.png)

## 安装 go 语言环境

`ngrok` 是基于 `go` 语言开发的，所以需要先安装 `go` 语言开发环境，`CentOS` 可以使用 `yum` 安装：

```
yum install golang
```

如果没有权限，请使用 `sudo` 安装，安装完成之后，执行 `go version` 看到类似信息，证明安装成功：

```
go version go1.7.3 linux/amd64
```

## 安装 git 环境

有些 VPS 的系统中自带了 git 环境，有的没有带，如果你的 git 使用不正常，请卸载自带的 git，重装安装。

卸载原有 git （根据需要自选）：

```
yum remove git
```

更新 yum 源：

```
yum update
```

安装 git ：

```
yum install git
```

安装完后执行 `git --version`，返回类似的信息，证明安装成功：

```
git version 2.5.0
```

## 下载 ngrok 源码：

找一个存放 `ngrok` 的文件夹 ，clone 一份源码：

(为了方便演示，本文使用 `root` 用户，所以存放在 `/root/` 路径下)

```
cd /root
git clone https://github.com/inconshreveable/ngrok.git
export GOPATH=/root/ngrok
```

## 生成自签名证书

使用 `ngrok` 官方服务时，我们使用的是官方的 `SSL` 证书。自己建立 `ngrok` 服务，需要我们生成自己的证书，并提供携带该证书的 `ngrok` 客户端。

证书生成过程需要有自己的一个基础域名，官网随机生成的地址，如：`695a358d.ngrok.com`，基础域名就是 `ngrok.com`。而在上文中提到的二级域名 `ngrok.zhaojun.im` 就是用来作为这次要提供的基础域名。如果你的域名是 `abc.com`，那么域名基础域名可以设置为 `ngrok.abc.com`。

以我的基础域名为例（**注意替换成自己的域名**），生成证书过程如下：

```
cd /root/ngrok
openssl genrsa -out rootCA.key 2048
openssl req -x509 -new -nodes -key rootCA.key -subj "/CN=ngrok.zhaojun.im" -days 5000 -out rootCA.pem
openssl genrsa -out device.key 2048
openssl req -new -key device.key -subj "/CN=ngrok.zhaojun.im" -out device.csr
openssl x509 -req -in device.csr -CA rootCA.pem -CAkey rootCA.key -CAcreateserial -out device.crt -days 5000
```

执行完成以上命令后，在 `ngrok` 目录下，会新生成 6 个文件：

```
device.crt  device.csr  device.key  rootCA.key  rootCA.pem  rootCA.srl
```

我们在编译可执行文件之前，需要把生成的证书分别替换到 `assets/client/tls` 和 `assets/server/tls` 中，这两个目录分别存放着 `ngrok` 和 `ngrokd` 的默认证书。

```
cp rootCA.pem assets/client/tls/ngrokroot.crt
cp device.crt assets/server/tls/snakeoil.crt
cp device.key assets/server/tls/snakeoil.key
```

> 中间会提示是否覆盖，输入 y 确认即可。这里最好一行一行复制执行，别一起复制执行。

## 编译 ngrokd 和 ngrok

ngrokd 是服务端的执行文件，进入到 ngrok 目录下，执行如下命令编译：

```
make release-server
```

ngrok 是客户端的可执行文件，进入到 ngrok 目录下，执行如下命令编译：

```
GOOS=xxx GOARCH=xxx make release-client
```

不同平台使用不同的 `GOOS` 和 `GOARCH`，`GOOS` 为编译出来的操作系统 (`windows`,`linux`,`darwin`)，`GOARCH` 对应的构架 (`386`, `amd64`, `arm`)

```
Linux 平台 32 位系统：GOOS=linux GOARCH=386
Linux 平台 64 位系统：GOOS=linux GOARCH=amd64

Windows 平台 32 位系统：GOOS=windows GOARCH=386
Windows 平台 64 位系统：GOOS=windows GOARCH=amd64

MAC 平台 32 位系统：GOOS=darwin GOARCH=386
MAC 平台 64 位系统：GOOS=darwin GOARCH=amd64

ARM 平台：GOOS=linux GOARCH=arm
```

然后下载编译后的客户端，通过 ftp 或 scp 等都可以，生成的目录在 ngrok 的 bin 目录下，当前例子的路径为 `/root/ngrok/bin/windows_amd64/ngrok.exe`

## 启动 ngrokd 服务器

在 ngrok 的 bin 目录下执行：

```
./ngrokd -domain="ngrok.zhaojun.im" -httpAddr=":8088" -httpsAddr=":8089"
```

其中，`-domain` 为你的 ngrok 服务域名，`-httpAddr` 为 http 服务端口地址，访问形式为：`xxx.ngrok.zhaojun.im:8088`，也可设置为 80 默认端口，注意端口冲突即可，`-httpsAddr` 为 https 服务，同上。

`ngrokd` 启动后，退出命令行即关闭服务。如果想要在后台运行，则执行：

```
nohup ./ngrokd -domain="ngrok.zhaojun.im" -httpAddr=":8088" -httpsAddr=":8089" &
```

注意末尾需要有 `&` 号，详细搜索 `nohup` 了解。
关闭服务只需通过：

```
ps -A   # 找到PID，执行关闭
kill xxxid
```

## 启动 ngrok 客户端

上面我们编译好了客户端并下载到了本地，演示路径为 `d:/ngrok/ngrok.exe`

在 `d:/ngrok/` 目录下，建立 ngrok 配置文件：`ngrok.cfg`

```
server_addr: "ngrok.zhaojun.im:4443"
trust_host_root_certs: false
```

`server_addr` 端口默认 4443，还需要服务器开启 4443 端口，使用阿里云或腾讯云的需要去安全组放行 4443 外网端口，不然无法正常使用。

然后使用 cmd 到这个路径下(`d:/ngrok/`)，执行命令启动并转发本地的 4000 端口：

```
ngrok -subdomain demo -config=./config.cfg 4000
```

运行完了以后会有提示域名，根据提示域名访问，我这里这里为 : `http://demo.ngrok.zhaojun.im:8088`，访问这个就等于访问到你的 `http://127.0.0.1:4000` 下的内容了。

更详细的 ngrok 配置，请参考官方文档 : <https://ngrok.com/docs>