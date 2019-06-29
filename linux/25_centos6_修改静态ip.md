### Linux CentOS6.8配置静态IP详细图文教程

2018年01月10日 16:49:55 [Attend_](https://me.csdn.net/Attend_) 阅读数：14605

一：运行”vi /etc/sysconfig/network-scripts/ifcfg-eth0“命令打开配置文件

二：按"i"键进入编辑状态，然后将配置修改成如下图所示，红箭头标出项修改成自己网段内的IP即可

![img](https://img-blog.csdn.net/20180110161914931?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvQXR0ZW5kXw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

三：按"esc"键退出编辑模式，输入":wq"保存并退出，如下图所示

![img](https://img-blog.csdn.net/20180110162623746?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvQXR0ZW5kXw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

四：运行"service network restart"命令，重启网络服务，使刚才修改的配置信息生效，运行效果如下图

![img](https://img-blog.csdn.net/20180110163042073?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvQXR0ZW5kXw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

如果配置正确的话，效果会如上图所示一样，都是OK状态，如果有FAILED项所说明配置错误，重新打开配置文件仔细检查一下，直至正确

五：运行"ifconfig"命令，查看服务器当前网络状态，如下图，eth0为我们配置的网卡信息，自己检查一下是否跟自己配置的一致

![img](https://img-blog.csdn.net/20180110163349285?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvQXR0ZW5kXw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

六：至此服务器的IP信息已经配置完毕，即可通过远程工具连接服务器进行访问，主编自己使用的是xshell远程连接工具，使用xsehll远程连接服务器教程如下：

1：安装xshell(百度直接搜索下载 and  安装)

2：安装后运行，进入主界面，如下图：

![img](https://img-blog.csdn.net/20180110163744513?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvQXR0ZW5kXw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

3：执行：文件>新建 选项卡，打开新建连接窗口，如下图：

![img](https://img-blog.csdn.net/20180110164141321?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvQXR0ZW5kXw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

4：单击确定，然后在列表中选中刚刚配置好的连接信息，单击”连接“按钮，然后等待出现输入用户名窗口，如下图：

![img](https://img-blog.csdn.net/20180110164301133?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvQXR0ZW5kXw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

![img](https://img-blog.csdn.net/20180110164348385?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvQXR0ZW5kXw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)点击确定

![img](https://img-blog.csdn.net/20180110164525872?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvQXR0ZW5kXw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)点击确定

![img](https://img-blog.csdn.net/20180110164608031?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvQXR0ZW5kXw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)连接成功，已连接至服务器

5：如上所述，如果配置正确的话，此刻已可正常远程操作服务器。

6：以上内容为小编亲身操作并记录，希望能帮助到各位小伙伴，希望你们能在编程的道路上越走越远，谢谢你们的观看。