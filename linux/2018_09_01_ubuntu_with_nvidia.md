#### Ubuntu下安装nvidia显卡驱动（安装方式简单）

2018年03月05日 14:48:04 阅读数：4770

版权声明：本文为博主原创文章，未经博主允许不得转载。	

https://blog.csdn.net/linhai1028/article/details/79445722

Ubuntu下安装nvidia显卡驱动，用同方法安装过GTX1050，安装成功。不会出现循环登录

------

## 第一步 获取显卡型号

想办法获取自己nvidia显卡的型号（一般买电脑的时候都会有显卡型号，我的显卡型号是在电脑上的一个贴纸上），本人的显卡是GTX970M。

## 第二步 去[NVDIA driver search page](http://www.nvidia.com/Download/index.aspx)查看支持 GTX970M 显卡的驱动的最新版本的版本号

![这里写图片描述](https://img-blog.csdn.net/20180201204241599?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbGluaGFpMTAyOA==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast) 
After a successful search take a note of the resulting driver version number: 
![这里写图片描述](https://img-blog.csdn.net/20180201204317023?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbGluaGFpMTAyOA==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

## 第三步 查询支持GTX970M显卡的显卡驱动的其他驱动版本

从上面得到了最新的安装版本390，但为了防止新版本不稳定。我们可从 [geforce drivers](https://www.geforce.cn/drivers) 处查询支持970M显卡的所有驱动版本，如下图 
![这里写图片描述](https://img-blog.csdn.net/20180228142307328?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbGluaGFpMTAyOA==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
查询结果，如下图 
![这里写图片描述](https://img-blog.csdn.net/20180228142341619?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbGluaGFpMTAyOA==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
图中有390、384、375等版本

## 第四步 安装

下面我们使用ppa方式安装384版本驱动，而不是最新的390版本驱动 
在terminal run， `sudo apt-get install nvidia-384`

if 上述命令报错，那么执行下面命令，否则不执行

>   1.  更新源，运行 
>       `sudo apt-get upgrade` 
>       `sudo apt-get update`
>   2.  查询nvidia驱动可用版本，运行`sudo apt-cache search nvidia-*` 查询ppa安装支持的版本驱动，如果有384
>   3.  安装nvidia驱动，`sudo apt-get install nvidia-384`

## 第五步 测试nvidia driver是否安装成功

首先需要重新启动操作系统，然后通过以下方式测试nvidia driver安装成功与否 
\1. ubuntu下seach invidia并打开，如果结果如下则表示安装成功 
![这里写图片描述](https://img-blog.csdn.net/20180206154917901?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbGluaGFpMTAyOA==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast) 
\2. 或者terminal下执行`nvidia-smi`

------

## 环境

1.  ubuntu 16.04
2.  ubuntu 17.10
3.  显卡型号 GTX970M

## 参考资料

1.  [How to install the latest Nvidia drivers on Ubuntu 16.04](https://linuxconfig.org/how-to-install-the-latest-nvidia-drivers-on-ubuntu-16-04-xenial-xerus)