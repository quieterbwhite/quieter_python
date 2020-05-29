#### SSH

##### 一个名字 
```
authorized_keys  
```

##### ubuntu server, root login
```
ref: https://www.cnblogs.com/zepc007/p/10765314.html

Ubuntu server版启用root用户登录
sudo su
vim /etc/ssh/sshd_config

# 在 sshd_config 文件里的 “Authentication” 部分加上以下内容
PermitRootLogin yes
# 完成以后退出 vim 并保存

service sshd restart # 重启 ssh 服务以应用更改
passwd root # 直接修改 Root 用户的密码
这样重新登陆 ssh 就可以用 Root 登陆了。
```

##### 避免SSH连接因超时闲置断开/How to fix ssh timeout problems
```
用SSH过程连接电脑时，经常遇到长时间不操作而被服务器踢出的情况，常见的提示如：
Write failed: Broken pipe
这是因为如果有一段时间在SSH连接上无数据传输，连接就会断开。解决此问题有两种方法。

方案一：在客户端设置
方法很简单，只需在客户端电脑上编辑（需要root权限）/etc/ssh/ssh_config，并添加如下一行
：
ServerAliveInterval 60
此后该系统里的用户连接SSH时，每60秒会发一个KeepAlive请求，避免被踢。

方案二：在服务器端设置
如果有相应的权限，也可以在服务器端设置，即编辑/etc/ssh/sshd_config，并添加：
ClientAliveInterval 60
重启SSH服务器后该项设置会生效。每一个连接到此服务器上的客户端都会受其影响。应注意启用
该功能后，安全性会有一定下降（比如忘记登出时……）
```

##### ssh 连接提示 The authenticity of host can't be established 解决方案
```
StrictHostKeyChecking no
UserKnownHostsFile /dev/null
```
