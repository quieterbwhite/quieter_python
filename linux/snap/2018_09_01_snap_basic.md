#### Ubuntu 18.04及Snap体验——让Linux入门更简单

| [日期：2018-06-27] | 来源：[Linux公社](https://www.linuxidc.com/Linux/2018-06/152993.htm)  作者：xzymoe | [字体：[大](javascript:ContentSize(16)) [中](javascript:ContentSize(0)) [小](javascript:ContentSize(12))] |
| --------------- | ---------------------------------------- | ---------------------------------------- |
|                 |                                          |                                          |

初次听说过Linux的时候，是大一计算机课时候老师介绍说除了Windows还有Linux、Unix操作系统。但真正接触Linux是为管理虚拟专用服务器（VPS），都说[Ubuntu](https://www.linuxidc.com/topicnews.aspx?tid=2)适合新手于是接触了是Ubuntu 10.10（Maverick Meerkat）。从此爱上了Linux。虽然之后我使用[CentOS](https://www.linuxidc.com/topicnews.aspx?tid=14)的时间长于别的Linux Distribution，但Ubuntu从没有离开过我的电脑。如今都发行到了Ubuntu 18.04（Bionic Beaver）。

![Ubuntu 18.04及Snap体验——让Linux入门更简单](https://www.linuxidc.com/upload/2018_06/18062720505501.jpg)

### 0x00 Ubuntu 18.04的安装

1.Ubuntu每年都会在4月与10月份发布一个版本的更新，而每两年发布一个LTS长期支援版本，其支援期限长达5年，而非LTS版本的支援通常只有半年。而18.04是2016年之后发行的第一个LTS版本，作为一个喜欢尝鲜的Linuxer来说，肯定第一时间也安装了Ubuntu 18.04 LTS。

2.Ubuntu18.04的安装与之前的发行版并没有什么区别。由于我的生产环境Ubuntu16.10中程序较多，被DIY的较多，因而并没有在实体机中安装Ubuntu 18.04，而是在VirtualBox中安装的。

![Ubuntu 18.04及Snap体验——让Linux入门更简单](https://www.linuxidc.com/upload/2018_06/18062720504852.png)

3.在安装类型中，我选择了其他选项，因为这样可以自己创建、调整分区，或者为Ubuntu选择多个分区。

![Ubuntu 18.04及Snap体验——让Linux入门更简单](https://www.linuxidc.com/upload/2018_06/18062720507994.png)

4.对于分区来说，特别是在虚拟机中，建议/挂载点划分15G左右，/boot大概128MB左右，/swap分区大概2G左右，剩余空间划分为/home。

![Ubuntu 18.04及Snap体验——让Linux入门更简单](https://www.linuxidc.com/upload/2018_06/18062720507550.png)

由于我在虚拟机里分区的划分大小与设备都是很随意的配置了一下，不过还是应该按照个人的实际情况来安装配置。对于初次安装Linux的人来说，机子配置还可以的话，直接划分/与/home即可。

5.之后耐心等待就可以完成Ubuntu 18.04的安装了，总体安装还是非常的快的，当然如果你勾选了网络下载更新的话，那么会根据你的网速来决定你的安装过程。安装完毕后，提示重启，之后就可以进入Ubuntu 18.04的桌面了。

![Ubuntu 18.04及Snap体验——让Linux入门更简单](https://www.linuxidc.com/upload/2018_06/18062720544357.png)

6.进入系统后会发现又是那个熟悉的Gnome图形界面，这里不得不吐槽下从Ubuntu11.04到Ubuntu17.10的过程中图形界面为Unity，我觉得是一个非常不友好的图形界面，反正在Unity统治Ubuntu的6年半时间里，我基本都会在第一时间将其更换为Gnome。

### 0x01 Ubuntu 18.04新特性与体验

**新版Gnome**

刚才我还吐槽了Unity的同时赞美了Gnome。而随Ubuntu 18.04一起到来的还有Gnome3.28。

![Ubuntu 18.04及Snap体验——让Linux入门更简单](https://www.linuxidc.com/upload/2018_06/18062720549105.png)

由于在上一个LTS版本的Ubuntu中，Unity依旧为主流的桌面环境，Gnome3.28的到来标志着新统一风格定制的Gnome3.0桌面在长期支援版上的到了支持。

**Suru图片的纳入**

喜欢Linux的人一定还记得Ubuntu Touch吧！这个由Ubuntu衍生而来的移动操作系统，当初Suru作为一个开源图标项目，就是专门为Ubuntu Touch设计的，如今已经完全的融入到了Ubuntu 18.04LTS，那些当初设计的图标已经被重新用于Gnome主题图标相对应。当然出了之前设计的图标外，此次还在Sura项目中加入了很多文件夹与文件类型的图标。

具体样式可以参考Suru官网。

\# Project Suru

<https://snwh.org/suru>

**全新Emoji支援**

Firefox最近在about:config中终于可以启开了内置Emoji，而查阅一下关于FirefoxEmoji支援，你会发现其最早是在Mozilla Firefox 50就引入了内置Emoji，不过最先只是给Gnu/Linux与Win8这类原生不带Emoji的系统启用的，你就可以知道Linux对Emoji的支援应该不是那么满意（[Fedora](https://www.linuxidc.com/topicnews.aspx?tid=5)除外哈！）该版本的Ubuntu中为了保持平台间的一致性，其默认使用了Noto Color Emoji（AOSP中也使用了该字体）字体，其支援最新的Unicode版本中定义的所有Emoji符号，且在该版本的Ubuntu中GTK程序中添加Emoji非常的简单。

**Gnome To Do**

![Ubuntu 18.04及Snap体验——让Linux入门更简单](https://www.linuxidc.com/upload/2018_06/18062720542664.png)

作为一个重度健忘症患者，在使用Windows和[Android](https://www.linuxidc.com/topicnews.aspx?tid=11)的时候，我一直都是用Microsoft To-Do来最为待办事项管理，不过没有想到在这个版本的Gnome中竟然自带了这个功能。

**Minimize on Click**

该功能类似于Windows的任务栏，点击软件图标可以最小化窗口或者还原窗口。只不过点击的位置换成了Ubuntu Dock上了。不过略有遗憾的就是该功能默认情况下为关闭的，不过可以通过以下命令启用该功能。

**#启用Minimize on Click**

gsettings set org.gnome.shell.extensions.dash-to-dock click-action 'minimize'

**Gstreamer Multimedia Codecs解码器的加入**

在安装Ubuntu 18.04的时候就默认加入了第三方解码器Gstreamer Multimedia Codecs，这个让人挺意外的，其可以让我们实现在线视频观看和改进图形显卡的支援。当然不包括那些受限于Adobe Flash和专有驱动程序。

**夜间模式**

和Windows10 April更新一样，加入了夜间模式，对于在学校半夜断电后，还在玩电脑的同学来说，是一个非常贴心的功能。

![Ubuntu 18.04及Snap体验——让Linux入门更简单](https://www.linuxidc.com/upload/2018_06/18062720543344.png)

除此之外，Ubuntu 18.04还使用Linux Kernel 4.15，并且恢复了Xorg为默认显示服务等。这些新的特性都在预示着新的Ubuntu系统是一个很优秀的桌面Linux Distribution。

### 0x02 Ubuntu 18.04软件安装与体验

**更换更新源**

为了让软件下载与系统更新更快点，推荐将更新源改为国内的更新源。这里推荐使用阿里云的更新源。

**#阿里云更新源**

deb http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse

![Ubuntu 18.04及Snap体验——让Linux入门更简单](https://www.linuxidc.com/upload/2018_06/18062720583664.png)

**更换方法：**

sudo vim /etc/apt/sources.list

将文件的内容替换为阿里云的更新源,:wq保存

sudo apt update
sudo apt upgrade

**安装搜狗输入法**
其实我感觉Ubuntu现在默认的输入法还是不错的，当然没有搜狗输入法好用，好在搜狗输入法也提供了Linux版本。
\#Sogou for Linux

<https://pinyin.sogou.com/linux/?r=pinyin>
下载后进入下载目录,尝试安装软件，之后安装依赖后重新安装即可。

\#搜狗输入法安装

sudo dpkg -i sogoupinyin2.2.0.0108amd64.deb

sudoapt-get install -f

sudo dpkg-i sogoupinyin2.2.0.0108amd64.deb
安装好后，在系统设置中语言部分将键盘输入法系统改为fcitx。之后重启系统。在fcitx的配置中设置搜狗输入法为默认即可。

![Ubuntu 18.04及Snap体验——让Linux入门更简单](https://www.linuxidc.com/upload/2018_06/18062720582382.png)

**网易云安装**
网易云的安装和搜狗输入法的一样，不过不用配置非常的简单。
\#网易云下载

<http://music.163.com/#/download>
官网下载好后，进入下载目录。
sudo dpkg-i netease-cloud-music1.1.0amd64_ubuntu.deb

sudoapt-get install -f

sudo dpkg-i netease-cloud-music1.1.0amd64_ubuntu.deb
不出意外的话，安装完毕后你是无法打开的，貌似是这个版本的Bug。
不过可以通过修改权限来完成，不过修改后需要重启。
cd　～/.cache

chmod 777netease-cloud-music

reboot

![Ubuntu 18.04及Snap体验——让Linux入门更简单](https://www.linuxidc.com/upload/2018_06/18062720582508.png)

之后就可以在Ubuntu 18.04中欣赏音乐了。

**QQ安装**

由于QQ没有提供Linux版本的程序，所以一般情况下都用wine来安装，不过wine的配置略麻烦，所以推荐使用appimage的方式来安装。

**#QQ Appimage 下载**

https://yun.tzmm.com.cn/index.php/s/XRbfi6aOIjv5gwj/download

下载好程序后，右键属性——允许作为程序执行文件勾选即可。或者chmod +x download。

![Ubuntu 18.04及Snap体验——让Linux入门更简单](https://www.linuxidc.com/upload/2018_06/18062720585231.png)

剩下的程序就可以用过APP Store或者Snap Store安装即可。

### 0x03 关于Snap

Snap是Ubuntu母公司Canonical于2016年4月发布Ubuntu16.04时候引入的一种安全的、易于管理的、沙盒化的软件包格式，与传统的dpkg/apt有着很大的区别。

Snap可以让开发者将他们的软件更新包随时发布给用户，而不必等待发行版的更新周期；其次Snap应用可以同时安装多个版本的软件，比如安装Python2.7和Python3.3。

我初次接触Snap的时候是安装NextCloud，通过Snap的方式来安装NextCloud，很快就可以完成安装与部署。

0x04 使用Snap安装主题与美化

每天都要面对的操作系统，有一个漂亮的主题那么心情会愉悦很多，而我个人使用的是flatabulous-theme。非常的漂亮，不过其没有snap包，所以今天安装另一款也很好看的主题communitheme。

**主题安装**

**方案一：SnapStore**

在App Store中搜搜communitheme即可，之后点击安装即可。

![Ubuntu 18.04及Snap体验——让Linux入门更简单](https://www.linuxidc.com/upload/2018_06/18062721012977.png)

**方案二：Snap命令安装**

这里我通过edge通道进行安装，也可以通过GTK+3、Qt frameworks、stable等通道进行安装。

sudo snapinstall communitheme –edge

sudo snaprefresh

安装好后，重启后在登陆界面选择小齿轮设置为新的主题即可。

![Ubuntu 18.04及Snap体验——让Linux入门更简单](https://www.linuxidc.com/upload/2018_06/18062721016186.png)

![Ubuntu 18.04及Snap体验——让Linux入门更简单](https://www.linuxidc.com/upload/2018_06/18062721011820.png)

是不是发现Theme的风格已经发生了改变，特别是左下角的的Ubuntu Logo特别的帅。

**图标安装与设置**

图标包我非常喜欢的是Numix这个系列的图标，特别是其中的numix-icon-theme-circle。那么就安装numix-icon-theme-circle这套图标包了。

\#Numix-icon-theme-circle

sudoadd-apt-repository ppa:numix/ppa

sudoapt-get update

sudoapt-get install numix-icon-theme-circle

图标包安装好了设置使用上该套图标包还需要使用Gnome Tweak，安装方法也是通过到AppStore中搜索Gnome Tweak即可，也可以通过sudo apt-get install gnome-tweak-tool来完成安装。由于系统是中文系统，该软件中文名叫做“优化”。

![Ubuntu 18.04及Snap体验——让Linux入门更简单](https://www.linuxidc.com/upload/2018_06/18062721013341.png)

在图标部分选择Numix-Circle即可。

![Ubuntu 18.04及Snap体验——让Linux入门更简单](https://www.linuxidc.com/upload/2018_06/18062721038479.png)

总体来说这套图标还是颜值很高的。

### **0x05 使用Snap安装软件及基础教程**

Snap安装软件也是非常的方便仅仅需要一个命令即可完成安装，当然如果这样做你就不能完全理解Snap的设计的完美。

**Snap安装软件**

**VLC安装**

一般怎么用Snap安装软件呢？这里以VLC为例。

1.首先查看你是否通过Ubuntu One登陆Snap。

snap whoami

2.如果显示空邮箱的话，那么说明你没有登陆，你可以通过一下命令通过Ubuntu One登陆Snap。

snap login

3.此处分割线，其实以上过程可以省略，只是为了更加标准一点啦！

4.首先在SnapStore中寻找VLC。

snap find vlc

![Ubuntu 18.04及Snap体验——让Linux入门更简单](https://www.linuxidc.com/upload/2018_06/18062721041103.png)

可以通过结果看出，VLC的Snap包的确就叫vlc，这个就很尴尬了，感觉多弄了一步，不顾没关系这里主要是告诉你如何使用Snap搜索软件。

5.为了在次确认VLC的软件包，我可以查询更多的信息。

snap info vlc

![Ubuntu 18.04及Snap体验——让Linux入门更简单](https://www.linuxidc.com/upload/2018_06/18062721043378.png)

在确定了vlc的信息后，还可以看到各个通道中的Snap包的情况。

6.安装VLC，如果你已经通过Ubuntu One登陆了Snap，一下命令可以省略了sudo。其默认是通过stable通道进行下载安装的。

snap install vlc

![Ubuntu 18.04及Snap体验——让Linux入门更简单](https://www.linuxidc.com/upload/2018_06/18062721041596.png)

安装好后也可以通过vlc –version来查看VLC的版本。

7.默认情况下，是通过stable的通道进行安装的（还记得之前安装communitheme时候我用的edge通道吗？）。当然即使你安装好了stable通道的VLC，当然也还可以切换到别的通道。

snap switch–channel=candidate vlc

snap refresh

之后就切换到了candidate（候选发行版）的vlc了，你可以通过刚才的vlc –-version来查看你你的vlc版本。

8.看似很简单的Snap是不是就完了呢？基本可以这么说吧！不过还有一个snap run -shell的命令呢。通过snap run -shel vlc可以给你一个shell让你拥有更多的snap权利。

你可以在/snap中找到snap的文件。再其二级目录中有一个和snap软件包一样的目录，如/snap/vlc/。由于之前我也说了，Snap的一个优点就是可以安装不同版本的同一个软件，至于你现在使用的版本的文件其在/snap/vlc/current/中。在meta/snap.yaml中，我可以可以获取到snapcraft的配置文件。

Telegram

Telegram是近年来比较流行的即使聊天软件，也是非常完美的融入了我的生活，至于这个软件怎么使用呢？自己Google吧！！！安装的方法和VLC一样，不过我觉得你都会来安装Telegram，那么Snap你估计也很熟悉了吧！这里直接安装Telegram。

\#Telegram Snap App

sudo snap install telegram-sergiusens

![Ubuntu 18.04及Snap体验——让Linux入门更简单](https://www.linuxidc.com/upload/2018_06/18062721058586.png)

Snap安装软件时候，终端会有白色进度条显示下载百分比，非常的人性。

**Snap基础教程**

其实基础教程应该在实战之前，不过我觉得实战才是最好的学习方法，所以先写了Snap安装软件的方法。相比你现在都已经学会了几个Snap的基本用法了。

\#查询已经安装了的软件

sudo snap list

\#搜索要安装的Snap软件包

sudo snap find xxxx

\#查看Snap软件的更多信息

sudo snap info xxxx

\#安装Snap软件包

sudo snap install xxxx

\#更换软件安装通道

sudo snap switch –channel=xxxx xxxx

\#更新Snap软件包

sudo snap refresh xxxx

\#还原到之前版本

sudo snap revert xxxx

\#卸载Snap软件

sudo snap remove xxxx

当然光靠命令你想搜索什么snap软件包也是一头雾水吧！可以去uappexplorer里查询下，有什么snap软件包呢！喜欢的就都安装上。

\#Uappexplorer

<https://uappexplorer.com/snaps>

0x06 将软件打包为Snap软件

![Ubuntu 18.04及Snap体验——让Linux入门更简单](https://www.linuxidc.com/upload/2018_06/18062721064397.png)

Snapcraft是用来构建snaps的软件，他使用也非常的简单，我们仅仅需要写一个snapcraft.yaml的配置文件即可。接下来就用Snapcraft打包一下GNU项目里的hello和bash。先从hello开始。

由于Ubuntu 18.04LTS中已经安装有Snapcraft了，我们就不需要在去apt安装了。可以直接开始打包我们的snap软件。

**初始打包**

1.创建一个打包snap的目录hello。

mkdir hello

cd hello

2.初始化snapcraft。

snapcraft init

3.使用vim编辑配置文件snapcraft.yaml。

vim snap/snapcraft.yaml

将其修改为以下内容。

![Ubuntu 18.04及Snap体验——让Linux入门更简单](https://www.linuxidc.com/upload/2018_06/18062721073178.png)

name:描述这个snap软件的名称

version:描述这个软件的版本，可以用ascii码。

summary:对软件的一个总结。

Description:对软件进行一个描述。

grade:软件的发行通道。

confinement:对软件做一个限制，如devmode或者strict。

之后按照格式定义以下parts。

其中source表示打包软件的来源，plugin表示此软件安装时候需要的一些依赖关系，使用autotools即可。

4.编译snap打包软件。

snapcraft

![Ubuntu 18.04及Snap体验——让Linux入门更简单](https://www.linuxidc.com/upload/2018_06/18062721079389.png)

由于我们的source需要从GNU的ftp服务器上下载程序，待下载好后，其会自动打包编译。

5.之后进行测试安装。

sudo snap install --devmode hello2.10amd64.snap

![Ubuntu 18.04及Snap体验——让Linux入门更简单](https://www.linuxidc.com/upload/2018_06/18062721085769.png)

可以通过snap list查看是否安装成功，注意看Notes部分，其为devmode。

![Ubuntu 18.04及Snap体验——让Linux入门更简单](https://www.linuxidc.com/upload/2018_06/18062721098998.png)

6.进行测试，输入hello命令。

神马？？竟然抱错了。当然你肯定会想用which hello进行检查。不过我可以告诉你答案，hello的二进制文件在/snap/bin里，是不是明白哪里出问题了？

**Snap全局命令**

我们已经知道了为什么hello不能成为全局命令了，当然也还是只能通过修改snapcraft.yaml配置文件来使之成为全局命令。

1.修改snapcraft.yaml，添加一个apps部分，使命令hello指向bin/hello即可。

![Ubuntu 18.04及Snap体验——让Linux入门更简单](https://www.linuxidc.com/upload/2018_06/18062721083266.png)

2.迭代你的snap打包软件。

snapcraft prime

![Ubuntu 18.04及Snap体验——让Linux入门更简单](https://www.linuxidc.com/upload/2018_06/18062721107110.png)

3.之后再次尝试hello命令，终于生效了。

**Snap打包进阶**

1.为了让我们的snap更有意思一点，我们添加一个新的parts和apps。

![Ubuntu 18.04及Snap体验——让Linux入门更简单](https://www.linuxidc.com/upload/2018_06/18062721109078.png)

2.之后我们重新执行。

Snapcraft prime

毫无疑问你肯定会报错失败。为什么呢？？因为gnu-hello和gnu-bash两个不同的parts都将定向到了一个share/info/dir里，这里就发生了冲突。

3.其实在执行snapcraft的时候，类似于执行./configure，这里只用给./configure一个参数即可。那么snapcraft.yaml配置文件可以这么修改。

![Ubuntu 18.04及Snap体验——让Linux入门更简单](https://www.linuxidc.com/upload/2018_06/18062721108617.png)

这相当于将—infodir=/var/bash/info作为一个参数传递给了./configure。

3.之后重新编译。

snapcraft clean gnu-bash -s build

这里的clean只是相当于重新构架了一下gnu-bash，并不需要重新下载gnu-bash，当然可以snapcraft成功了。

![Ubuntu 18.04及Snap体验——让Linux入门更简单](https://www.linuxidc.com/upload/2018_06/18062721118460.png)

4.之后重新测试。

sudo snap try --devmode prime

5.之后再次测试hello和hello.bash命令，看看是否能进入这个子shell。

![Ubuntu 18.04及Snap体验——让Linux入门更简单](https://www.linuxidc.com/upload/2018_06/18062721119683.png)

之后通过env查询当前的环境，确认进入子shell，要退出的话，按q哦！

删除devmode

之前通过snap list可以看出Notes部分标记hello为devmode，既然我们都测试完毕了，那么是时候改为strict了。

![Ubuntu 18.04及Snap体验——让Linux入门更简单](https://www.linuxidc.com/upload/2018_06/18062721118907.png)

1.修改配置文件snapcraft.yaml。

将devmode修改为strict；其实也可以将grade后面的devel修改为stable了。

2.再次snapscraft一下。

3.你可以尝试安装它。

sudo snap install hello2.10amd64.snap

不出意外会报错：error: cannot find signatures with metadata for snap "hello2.10amd64.snap"。

![Ubuntu 18.04及Snap体验——让Linux入门更简单](https://www.linuxidc.com/upload/2018_06/18062721126700.png)

4.为什么会报错呢？是由于我们的软件没有经过Snap Store签名，而之前的安装是因为是devmode所以可以被安装，因而要在本地安装非devmode的snap时候，需要加入—dangerous选项。

之后snap打包后的hello即可被安装，在通过snap list看一下，Notes部分已经没有devmode的字样了。而程序也可以正常的运行。

### 0x07 总结

Ubuntu 18.04 LTS经过开源社区及个人开发者的努力已经越来越完善了，软件数量丰富，美化资源也不少。虽然具有革命意义的Snap软件格式包的出现，让我们对Linux的上手更加的容易。

更多Ubuntu相关信息见[Ubuntu](https://www.linuxidc.com/topicnews.aspx?tid=2) 专题页面 <https://www.linuxidc.com/topicnews.aspx?tid=2>

Linux公社的RSS地址：<https://www.linuxidc.com/rssFeed.aspx>

**本文永久更新链接地址**：<https://www.linuxidc.com/Linux/2018-06/152993.htm>