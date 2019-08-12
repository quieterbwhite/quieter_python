# New Job New Env

## Created Time: 2017年12月06日 星期三 13时51分40秒

## 系统:

```
0. 系统镜像地址

    http://mirrors.aliyun.com/ubuntu-releases/

    https://opsx.alibaba.com/?lang=zh-CN

1. 换系统源

    https://wiki.ubuntu.com.cn/%E6%BA%90%E5%88%97%E8%A1%A8

    https://www.jianshu.com/p/126d51514097

    apt edit-sources

    Ubuntu 18.04 TLS版本阿里云镜像源：
    # https://opsx.alibaba.com/mirror
    deb https://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse 
    deb https://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse 
    deb https://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse 
    deb https://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse 
    deb https://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse 

    # 仿照清华镜像源，注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
    # deb-src https://mirrors.aliyun.com/ubuntu/ xenial main restricted universe multiverse 
    # deb-src https://mirrors.aliyun.com/ubuntu/ xenial-security main restricted universe multiverse 
    # deb-src https://mirrors.aliyun.com/ubuntu/ xenial-updates main restricted universe multiverse 
    # deb-src https://mirrors.aliyun.com/ubuntu/ xenial-proposed main restricted universe multiverse 
    # deb-src https://mirrors.aliyun.com/ubuntu/ xenial-backports main restricted universe multiverse

2. 更新系统

    sudo apt update

    sudo apt upgrade

3. 安装系统软件

    sudo apt install build-essential dpkg-dev openssh-server openssh-client python-dev python3-dev python-pip python3-pip nginx supervisor terminator vim git redis-server mysql-server mysql-client libmysqlclient-dev openssl libssl-dev zookeeperd docker.io
```

#### 技术软件
```
MyExcel

    MyExcel，是一个集导入、导出、加密Excel等多项功能的工具包

    https://gitee.com/mirrors/MyExcel

ecar_team/apimonitor

    - https://gitee.com/ecar_team/apimonitor

    - api监控系统，有api探测、api监控、http请求模拟、系统接口监控等功能，可以模拟http页面操作过程，并根据请求耗时和响应结果监控系统接口可用性和正确性

qidianliusong/redis-shared-lock

    - https://gitee.com/lsongiu/redis-shared-lock

    - 基于redis的分布式共享锁，使用注解的方式对方法加锁

IJPay

    - https://gitee.com/javen205/IJPay

    - IJPay 让支付触手可及，封装了微信支付、支付宝支付、银联支付常用的支付方式以及各种常用的接口。


imgcook

    - imgcook 是专注以各种图像（Sketch/PSD/静态图片）为原材料一键生成可维护的 UI 视图代码

    - 可以生成react代码,正是我熟悉的

ranger

    - 命令行浏览文件系统

    - sudo apt install ranger

EasyScheduler

    易调度
    https://github.com/analysys/EasyScheduler
    Easy Scheduler是一个分布式工作流任务调度系统，主要解决"错综复杂的任务依赖关系，而不能直观监控任务健康状态等问题"。

HanLP
 
    - https://github.com/hankcs/HanLP

    - 自然语言处理 中文分词 词性标注 命名实体识别 依存句法分析 新词发现 关键词短语提取 自动摘要 文本分类聚类 拼音简繁 http://hanlp.com/

funNLP

    - https://github.com/fighting41love/funNLP

    - 中英文敏感词、语言检测、中外手机/电话归属地/运营商查询、名字推断性别、手机号抽取、身份证抽取等

buaazp/zimg

    https://github.com/buaazp/zimg

    A lightweight and high performance image storage and processing system. http://zimg.buaa.us

    Zimg—轻量级图片服务器搭建利器 - https://mp.weixin.qq.com/s/O4qNmeIEYIryIzSEPxspaQ

Apache Tika

    - a content analysis toolkit

    - 内容抽取

Geet/central-platform

    - https://gitee.com/GeekPerson/central-platform

    - 为企业级打造最全面的微服务开发解决方案; http://47.94.252.160:8066
```

#### 其他软件
```
2018 年度新增开源软件排行榜之国产新秀榜
https://www.oschina.net/news/103781/2018-oschina-new-opensource-software-cn-top30

gnome-tweak-tool

    - https://itsfoss.com/gnome-tricks-ubuntu/

    - sudo apt install gnome-tweak-tool

ATX

    - ATX是一个安卓设备集群管理平台，可在线管理多台设备，实现远程操作，远程监控，获取手机元素信息等

    - https://gitee.com/hagyao520/ATX

chrome

lantern

pycharm

MusicTools

    - 免费下载各大平台无损音乐

AreaCity-JsSpider-StatsGov

    - https://github.com/xiangyuecn/AreaCity-JsSpider-StatsGov

    - 国家统计局中的省市区镇行政区划数据带拼音标注，高德地图的坐标和行政区域边界范围

ip2region

    - https://github.com/lionsoul2014/ip2region

Flameshot

    - Flameshot 在去年发布到 GitHub，并成为一个引人注目的工具。

    - https://github.com/lupoDharkael/flameshot

    - sudo apt install flameshot

    - 全局搜索启动 flameshot 后, 双击托盘图标即可截图

    - https://linux.cn/article-10070-1.html

mysql

    - https://blog.csdn.net/qq_38737992/article/details/81090373

roncoo-education

    - https://gitee.com/roncoocom/roncoo-education

    - 领课教育 - 领课网络在线教育系统

RemixIcon
 
    - https://gitee.com/mirrors/RemixIcon

    - Remix Icon 是一套面向设计师和开发者的开源图标库

pixi.js

    - https://gitee.com/mirrors/pixijs

    - Pixi.js 使用 WebGL ，是一个超快的 HTML5 2D 渲染引擎

xuanxuan

    - https://gitee.com/wwccss/xuanxuan

    - 喧喧是一个轻量级的企业聊天软件。由然之协同办公团队开发。http://xuan.im

DataGrip

    - 数据库图形界面软件

jenkins

    - 持续集成

nexus

    - 搭建maven私服

leaf

    - leaf 美团分布式ID生成服务

    - https://github.com/Meituan-Dianping/Leaf

    - https://tech.meituan.com/2017/04/21/mt-leaf.html

新浪微博图床

    - 感谢新浪微博提供的免费图床（对外链无限制），以及吊炸天的 cdn 图片加速服务，从此妈妈再也不用担心我的图床不能用了，另外还支持在网页图片右键菜单中一键上传。

    - chrome 扩展
    - https://4ark.me/post/549a6198.html

UML图

    - http://haha98k.com/

    - http://plantuml.com/zh/

分布式事务

    - FESCAR（Fast & Easy Commit And Rollback）

        - https://gitee.com/mirrors/FESCAR
        - FESCAR（Fast & Easy Commit And Rollback） 是一个用于微服务架构的分布式事务解决方案，它的特点是高性能且易于使用，旨在实现简单并快速的事务提交与

    - EasyTransaction

        - https://gitee.com/mirrors/EasyTransaction

frp

    - 内网穿透

    - 外部通过 ssh, http 访问内部服务

rancher

    - docker 图形化管理界面

PDMan

    - PDMan是一款开源免费的数据库模型建模工具，支持Windows,Mac,Linux等操作系统，是PowerDesigner之外，更好的免费的替代方案。

    - https://gitee.com/robergroup/pdman

Redisson

    - Redisson是架设在Redis基础上的一个Java驻内存数据网格（In-Memory Data Grid）。【Redis官方推荐】

    - https://github.com/redisson/redisson

    - lock-spring-boot-starter 轻松实现分布式锁

    - https://gitee.com/yizhigui/lock-spring-boot-starter

fish

    - fish shell 3.0.0 发布了，fish 是一个智能且用户友好的命令行 shell，适用于 macOS、Linux 等平台。fish 在无需配置的情况下支持语法高亮与智能联想等功能。

    - https://github.com/fish-shell/fish-shell/

giojs

    - Gio.js 是一个基于Three.js的web 3D地球数据可视化的开源组件库。

    - https://github.com/syt123450/giojs/blob/master/README_zh.md

TeaWeb

    - TeaWeb-可视化的Web代理服务。 DEMO: http://meloy.cn:7777

    - https://gitee.com/liuxiangchao/build

神箭云市场

    - https://www.shenjian.io/index.php?r=home/index

    - 爬虫软件, 数据市场

Portainer

    - Portainer是一个开源、轻量级Docker管理用户界面

Icework

    - 飞冰是一套基于 React 的中后台应用解决方案

    - https://alibaba.github.io/ice/docs/about

FrontJS

    - 它是一个前端错误的监控平台，可以监控 Web 和小程序页面的性能，以及收集异常信息。

    - https://www.frontjs.com/

tamguo

    - 探果网（简称tamguo）是基于java开发的在线题库系统

    - https://gitee.com/smiletocandy/tamguo

Doctor

    - 基于知识图谱的分布式智能医疗诊断系统

    - https://gitee.com/zyzpp/Doctor

CodeMirror

    - CodeMirror 是一款“Online Source Editor”，基于 Javascript，短小精悍，实时在线代码高亮显示

    - https://gitee.com/mirrors/CodeMirror

wired-elements

    - Collection of elements that appear hand drawn. Great for wireframes. 

    - https://wiredjs.com

    - https://github.com/wiredjs/wired-elements

deck.gl

    - http://deck.gl/#/

    - Uber 开源的基于地图的数据可视化框架。

    - https://github.com/uber/deck.gl

ip2region

    - ip2region - 最自由的ip地址查询库，ip到地区的映射库，提供Binary,B树和纯内存三种查询算法，妈妈再也不用担心我的ip地址定位。

    - https://gitee.com/lionsoul/ip2region

ExcelUtil

    - ExcelUtil借助反射和POI对Excel读取,省略了以往读取Excel的繁琐步骤

    - https://gitee.com/likaixuan0/ExcelUtil

Lottie

    - Airbnb 推出的动画效果库，可以把 Adobe After Effects 制作的动画用于 Web、安卓和 iOS。

    - http://airbnb.io/lottie/

python-eureka-client

    - 一个 Python 编写的 eureka 客户端，可以使得你的代码非常方便地接入 spring cloud 中。

    - https://gitee.com/keijack/python-eureka-client

Plotly

    - 这是一个开源的 JavaScript 图表库

    - Plotly.js 是一个高层次的、描述性的图表库，自带超过30种图表类型，包括 3D 图表、统计图表、SVG 地图等。

    - https://github.com/plotly/plotly.js

    - https://plot.ly/javascript/

    - https://github.com/Plotly  有不少python原生的内容

ICEC

    - springboot应用生态圈

    - https://gitee.com/weiweicode/icec

    - 可以参考 java 对某些功能的实现, 比如: 文件管理

O2OA

    - Java 全功能开源办公软件

    - http://www.o2oa.net/indexpc.html

MAME

    - 重温童年的街机模拟器

    - https://github.com/mamedev/mame

wav2letter++

    - Facebook 开源首个全卷积语音识别工具包 wav2letter++

    - https://github.com/facebookresearch/wav2letter/

Gource

    - Gource 是一个很好玩的可视化工具，可以将代码仓库的历史变成视频，支持 Git 和 SVN 等多种格式。只要在仓库目录执行 gource 命令，就能看到提交历史的视频。

    - https://gource.io/

Puppeteer

    - Puppeteer 是谷歌推出的 Chrome 无头浏览器，是目前的浏览器自动化首选工具。本文介绍了作者的使用经验。

    - https://docs.browserless.io/blog/2018/06/04/puppeteer-best-practices.html

faceai

    - 一款入门级的人脸、视频、文字检测以及识别的项目。

    - https://github.com/vipstone/faceai

natapp

    - 开启您的内网穿透之旅

    - https://natapp.cn/

    - https://natapp.cn/article/nohup

jdk

node

TIKA

    - Tika 是一个内容抽取的工具集合, pdf, doc

    - https://www.yiibai.com/tika

    - http://tika.apache.org/

mitmproxy

    - 跨平台代理软件

    - 开发调试用, 命令行,界面都有

torproject

    - https://www.torproject.org/index.html.en

    - Tor is free software and an open network that helps you defend against traffic analysis

anyproxy

    - http://anyproxy.io/cn/#%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B

    - npm install -g anyproxy

    AnyProxy是一个开放式的HTTP代理服务器。

    Github主页：https://github.com/alibaba/anyproxy

    主要特性包括：

        基于Node.js，开放二次开发能力，允许自定义请求处理逻辑
        支持Https的解析
        提供GUI界面，用以观察请求

snail007/goproxy

    - Proxy是golang实现的高性能http,https,websocket,tcp,防污染DNS,socks5代理服务器,支持内网穿透,链式代理,通讯加密,智能HTTP,SOCKS5代理,域名黑白名单,跨平台,KCP协议支持,集成外部API。

    - https://github.com/snail007/goproxy

    - Why need these?
    当由于某某原因,我们不能访问我们在其它地方的服务,我们可以通过多个相连的proxy节点建立起一个安全的隧道访问我们的服务.
    微信接口本地开发,方便调试.
    远程访问内网机器.
    和小伙伴一起玩局域网游戏.
    以前只能在局域网玩的,现在可以在任何地方玩.
    替代圣剑内网通，显IP内网通，花生壳之类的工具.

RedisDesktopManager

    - https://github.com/uglide/RedisDesktopManager

    - sudo snap install redis-desktop-manager

RedisPlus

    - https://gitee.com/MaxBill/RedisPlus

    - RedisPlus是为Redis管理开发的桌面客户端软件

lazygit

    - https://github.com/jesseduffield/lazygit
    
VMware vSphere

	- VMware vSphere集成容器（VIC）建立了一个在轻量级虚拟机内部署并管理容器的环境。

postman

sublime

sogoupinyin

    - https://blog.csdn.net/lupengCSDN/article/details/80279177

netease cloud music

    # 修改网易云音乐的启动图标：
    sudo gedit /usr/share/applications/netease-cloud-music.desktop

    # 修改 Exec 这一行内容为：
    Exec=sh -c "unset SESSION_MANAGER && netease-cloud-music %U"

    # 附录：网易云音乐配置及缓存目录：
    ~/.config/netease-cloud-music
    ~/.cache/netease-cloud-music

    ref: https://www.zhihu.com/question/277330447/answer/478510195

    ref: https://my.oschina.net/editorial-story/blog/2938423

zookeeper

ActiveMQ

kafka

intellij idea

datagrip

EasyPDF

    - 我们想向你推荐 EasyPDF —— 一款可以胜任所有场合的在线 PDF 软件。

    - https://easypdf.com/

    - https://linux.cn/article-10102-1.html

速盘

    - https://www.speedpan.com/

    - 全速下载度盘资源，免受限速困扰！

vscode

mysql-workbench

mongodb

robomongo

typora

vlc

aria2

    - aria2 is a lightweight multi-protocol & multi-source, cross platform download utility operated in command-line.

    - https://github.com/aria2/aria2

doodooke/doodoo

    - 多多小程序开源版

    - https://gitee.com/doodooke/doodoo

Anbox 在Ubuntu上运行Android应用

    - Run Android applications on any GNU/Linux operating system.

    - https://anbox.io/

    - 亲测没啥用，安装两个apk就包缺少本地包。

Android Studio

    - Android 开发

upterm

    - A terminal emulator for the 21st century.

    - https://github.com/railsware/upterm

wps    处理文档

Zathura: 轻巧好用的 PDF 查看器

    - sudo apt install zathura

	操作总结:

	基本操作与vim一致,对于熟悉vim快捷键的十分方便:

	向下移动一页是J(Ctrl+f),向上移动一页是K(Ctrl+b).上下左右移动分别是k/j/h/l

	gg 跳到文章首页
	G 跳到文末

	a 放大页面到合适大小
	s 放大页面到窗口宽度

	Ctrl+R 反色,inverted color

krita  类似 photoshop

bookworm  - ebook reader

    https://babluboy.github.io/bookworm/

calibre - 电脑上看电子书

    - sudo -v && wget -nv -O- https://download.calibre-ebook.com/linux-installer.sh | sudo sh /dev/stdin

rdesktop  ubuntu 远程连接 windows

坚果云

网易云音乐

    - http://music.163.com/#/download

    - https://www.cnblogs.com/linga/p/9133415.html

爱壁纸

    - http://www.lovebizhi.com/linux.html

有道词典

    - http://cidian.youdao.com/index-linux.html

上面这些deb包安装的时候如果报错没有依赖，解决方法: sudo apt-get install -f
因为deb包安装不会自动解决依赖

梧桐那时雨
http://blog.csdn.net/fuchaosz/article/details/51882935

rundeck   -   后台任务

    - http://tech.oyster.com/rundeck-vs-crontab-why-rundeck-won/

crontab-ui

    - 后台进程管理工具Supervisor + superlance（Supervisor 的增强插件工具集）
```

##### idea 插件
```
JRebel for IntelliJ
热部署插件，Java WEB 开发必备，节省生命。

Grep Console
高亮log不同级别日志，看日志的时候一目了然。

GenerateSerialVersionUID
Alt + Insert 生成serialVersionUID

Rainbow Brackets
彩虹括号。自动给代码块内花括号和括号加色，让视野更加注意在代码上。

Maven Helper
Maven插件，安装后可查看依赖以及冲突，一目了然。
```

## 网站
```
招投标:

    火标网

    剑鱼招标

    千里马招标

查政策:

    白鹿 www.bailuzhiku.com
```

## pip install
```
arrow   时间处理

pipenv

mysqlclient

Pillow

PyJWT

apscheduler

python-hwinfo  python 获取硬件信息

pysnowflake  发号器

pytesser     简单验证码识别

fake-useragent　User-Agent池
```

## other
```
sudo apt-get install sox libsox-fmt-all

Deluge BitTorrent Client

aMule

transmission-gtk

uget-gtk

you-get
```
