## Ubuntu18.04-L2TP-Client配置 原

[![副帅](https://oscimg.oschina.net/oscnet/up-df56a1f32b52c851a3a72de24ce2b66e.jpeg!/both/50x50?t=1502069458000)  副帅](https://my.oschina.net/podjonss) 发布于 2018/10/11 08:54

> https://my.oschina.net/podjonss/blog/2243307

[NetworkManager](https://my.oschina.net/podjonss?q=NetworkManager)[GNOME](https://my.oschina.net/podjonss?q=GNOME)[OpenSSL](https://my.oschina.net/podjonss?q=OpenSSL)[Linux](https://my.oschina.net/podjonss?q=Linux)[Ubuntu](https://my.oschina.net/podjonss?q=Ubuntu)

安装：
sudo apt update

sudo apt install network-manager-l2tp-gnome

1.将新VPN连接命名为something 
将主机名或地址放在Gateway字段中。
将用户名放在用户名字段中。
单击“密码”字段中的图标，然后选择有关如何提供密码的首选项。
Name the new VPN connection something
Put the hostname or address in the Gateway field.
Put username in the Username field.
Click the icon in the Password field and select your preference for how to supply the password.

2.单击IPSec设置... 
单击“启用到L2TP主机的IPsec隧道”框，
在预共享密钥字段中输入共享密钥。
将Gateway ID字段留空。
展开“高级选项”区域
在“阶段1算法”框中输入“3des-sha1-modp1024”。
在Phase 2 Algorithms框中输入“3des-sha1”。
选中“强制UDP封装”复选框。
单击确定。
单击保存。
Click IPSec Settings…
Click the box for “Enable IPsec tunnel to L2TP host”
Enter the shared secret into the Pre-shared key field.
Leave the Gateway ID field empty.
Expand the Advanced options area
Enter “3des-sha1-modp1024” into the Phase 1 Algorithms box.
Enter “3des-sha1” into the Phase 2 Algorithms box.
Leave the box checked for “Enforce UDP encapsulation”.
Click OK.
Click Save.

3.禁用xl2tpd
打开终端并输入以下命令以永久禁用xl2tpd服务：

sudo service xl2tpd stop
sudo systemctl disable xl2tpd
打开网络设置并尝试打开VPN