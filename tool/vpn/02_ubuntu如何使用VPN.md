# ubuntu如何使用VPN

- [![ubuntu如何使用VPN](https://imgsa.baidu.com/exp/whcrop=92,69/sign=c6caffb08713632715b89471feff9dd5/42166d224f4a20a491365fab9d529822720ed0b6.jpg)](http://jingyan.baidu.com/album/e73e26c06597a124adb6a7a6.html?picindex=1)1
- [![ubuntu如何使用VPN](https://imgsa.baidu.com/exp/whcrop=92,69/sign=4b69fb17dc1373f0f56a39ddcb7f76c2/0b55b319ebc4b745d983d47ac2fc1e178a821542.jpg)](http://jingyan.baidu.com/album/e73e26c06597a124adb6a7a6.html?picindex=2)2
- [![ubuntu如何使用VPN](https://imgsa.baidu.com/exp/whcrop=92,69/sign=596c8b085b4e9258a661d0acf3f2ec61/838ba61ea8d3fd1f117bc1563d4e251f95ca5f6f.jpg)](http://jingyan.baidu.com/album/e73e26c06597a124adb6a7a6.html?picindex=3)3
- [![ubuntu如何使用VPN](https://imgsa.baidu.com/exp/whcrop=92,69/sign=f4ad782f86d4b31cf069c2f9e8a61a46/4d086e061d950a7bbc482da807d162d9f2d3c959.jpg)](http://jingyan.baidu.com/album/e73e26c06597a124adb6a7a6.html?picindex=4)4
- [![ubuntu如何使用VPN](https://imgsa.baidu.com/exp/whcrop=92,69/sign=3ba8ef5d4790f60304e5ca0556628e22/8ad4b31c8701a18b36fc7123932f07082838fe43.jpg)](http://jingyan.baidu.com/album/e73e26c06597a124adb6a7a6.html?picindex=5)5
- [![ubuntu如何使用VPN](https://imgsa.baidu.com/exp/whcrop=92,69/sign=ae3ddcdeb4014a90816b10ffc607042b/2f738bd4b31c870111a1d18a2a7f9e2f0708ff43.jpg)](http://jingyan.baidu.com/album/e73e26c06597a124adb6a7a6.html?picindex=6)6
- [![ubuntu如何使用VPN](https://imgsa.baidu.com/exp/whcrop=92,69/sign=a35829626a09c93d07a758b5f04dc5e5/c2cec3fdfc039245bcc782638a94a4c27d1e256f.jpg)](http://jingyan.baidu.com/album/e73e26c06597a124adb6a7a6.html?picindex=7)7

> https://jingyan.baidu.com/article/e73e26c06597a124adb6a7a6.html

ubuntu是常用的一款桌面系统，今天我们来看看，在ubuntu上怎么使用VPN。

## 工具/原料

- Ubuntu18.04

## 方法/步骤

1. 1

   本经验以Ubuntu18.04平台为例，连接的VPN类型是L2TP。

   不管你是自己搭建的VPN平台，还是购买的VPN账号，都会给你下面图中所示的信息，主要有：服务器IP、用户名、密码、PSK密码。把这4个信息记录下来。

   [![ubuntu如何使用VPN](https://imgsa.baidu.com/exp/w=500/sign=9df8782f86d4b31cf03c94bbb7d6276f/42166d224f4a20a491365fab9d529822720ed0b6.jpg)](http://jingyan.baidu.com/album/e73e26c06597a124adb6a7a6.html?picindex=1)

2. 2

   然后登录到Ubuntu上开始配置，打开terminal终端，首先执行下面图中的add-apt命令，将这个源添加到ubuntu中。然后执行命令：

   sudo apt-get update

   来更新源信息。

   [![ubuntu如何使用VPN](https://imgsa.baidu.com/exp/w=500/sign=e734844703f41bd5da53e8f461da81a0/0b55b319ebc4b745d983d47ac2fc1e178a821542.jpg)](http://jingyan.baidu.com/album/e73e26c06597a124adb6a7a6.html?picindex=2)

   [![ubuntu如何使用VPN](https://imgsa.baidu.com/exp/w=500/sign=b592b14d9def76c6d0d2fb2bad17fdf6/838ba61ea8d3fd1f117bc1563d4e251f95ca5f6f.jpg)](http://jingyan.baidu.com/album/e73e26c06597a124adb6a7a6.html?picindex=3)

3. 3

   更新完毕后，就可以安装l2tp客户端了，命令是：

   sudo apt-get install network-manager-l2tp-gnome

   [![ubuntu如何使用VPN](https://imgsa.baidu.com/exp/w=500/sign=c6b0a16aa2c379317d688629dbc5b784/4d086e061d950a7bbc482da807d162d9f2d3c959.jpg)](http://jingyan.baidu.com/album/e73e26c06597a124adb6a7a6.html?picindex=4)

4. 4

   安装完成后，把xl2tpd的服务端程序停止掉，因为我们只需要客户端。停止命令是：

   sudo service xl2tpd stop

   sudo update-rd.d xl2tpd disable

   等它执行完成，到这里，客户端程序就安装好了。

   [![ubuntu如何使用VPN](https://imgsa.baidu.com/exp/w=500/sign=68199ec9dc43ad4ba62e46c0b2025a89/8ad4b31c8701a18b36fc7123932f07082838fe43.jpg)](http://jingyan.baidu.com/album/e73e26c06597a124adb6a7a6.html?picindex=5)

5. 5

   然后点击桌面右上角的网络图标，两个上下的箭头。然后点击下拉菜单中的edit connections开始创建vpn连接。

   [![ubuntu如何使用VPN](https://imgsa.baidu.com/exp/w=500/sign=f28d8f6fc595d143da76e42343f08296/2f738bd4b31c870111a1d18a2a7f9e2f0708ff43.jpg)](http://jingyan.baidu.com/album/e73e26c06597a124adb6a7a6.html?picindex=6)

6. 6

   会弹出一个网络连接窗口，点击右上角的add，添加链接。默认的连接是ethernet。

   [![ubuntu如何使用VPN](https://imgsa.baidu.com/exp/w=500/sign=b71b00129f58d109c4e3a9b2e159ccd0/c2cec3fdfc039245bcc782638a94a4c27d1e256f.jpg)](http://jingyan.baidu.com/album/e73e26c06597a124adb6a7a6.html?picindex=7)

   [![ubuntu如何使用VPN](https://imgsa.baidu.com/exp/w=500/sign=e952e547bd51f819f125034aeab54a76/09fa513d269759eeed2d03a7bffb43166d22df59.jpg)](http://jingyan.baidu.com/album/e73e26c06597a124adb6a7a6.html?picindex=8)

7. 7

   点击ethernet选项，就会出来多种连接方式，这里我们就可以看到L2TP这个选项。选择它，然后点击右下角的create按钮开始创建L2TP连接。

   [![ubuntu如何使用VPN](https://imgsa.baidu.com/exp/w=500/sign=606c8b085b4e9258a63486eeac83d1d1/c9fcc3cec3fdfc03fb0a80d4d93f8794a4c2266f.jpg)](http://jingyan.baidu.com/album/e73e26c06597a124adb6a7a6.html?picindex=9)

   [![ubuntu如何使用VPN](https://imgsa.baidu.com/exp/w=500/sign=a8eee4a74e166d223877159476230945/3b87e950352ac65ced2d051ff6f2b21193138ab6.jpg)](http://jingyan.baidu.com/album/e73e26c06597a124adb6a7a6.html?picindex=10)

8. 8

   这个时候会弹出连接窗口，在这个窗口中，gateway位置输入第一步中记录下来的服务器IP，下面的用户名填写记录的vpn用户名，密码这里无法输入不填。然后点击下面的IPsec settings。

   [![ubuntu如何使用VPN](https://imgsa.baidu.com/exp/w=500/sign=07d6484b8782b9013dadc333438da97e/10dfa9ec8a136327aafaa15f9c8fa0ec08fac743.jpg)](http://jingyan.baidu.com/album/e73e26c06597a124adb6a7a6.html?picindex=11)

9. 9

   在打开的IPsec Settings窗口里，在Pre-shared key一栏里填写第一步中记录的PSK密码。然后点击ok保存配置。再点ok保存连接信息，然后在编辑网络的页面就能看到我们创建好的VPN连接，如下面第二张图中所示：

   [![ubuntu如何使用VPN](https://imgsa.baidu.com/exp/w=500/sign=d73ddcdeb4014a90813e46bd99773971/a8ec8a13632762d03e29c7d3adec08fa513dc643.jpg)](http://jingyan.baidu.com/album/e73e26c06597a124adb6a7a6.html?picindex=12)

   [![ubuntu如何使用VPN](https://imgsa.baidu.com/exp/w=500/sign=f633dd88be1c8701d6b6b2e6177e9e6e/6c224f4a20a44623d1b7c60e9522720e0cf3d759.jpg)](http://jingyan.baidu.com/album/e73e26c06597a124adb6a7a6.html?picindex=13)

10. 10

    确认无误后，点击close关闭编辑网络连接的窗口，然后再点击右上角的网络图标，选择下拉菜单里的VPN connections，然后就能看到我们刚才创建的VPN连接，点击它。会弹出窗口让你输入密码，在这个窗口中输入第一步记录下来的用户密码。然后点击ok开始认证。

    [![ubuntu如何使用VPN](https://imgsa.baidu.com/exp/w=500/sign=5c41f7d78ad6277fe912323818391f63/472309f790529822a94e5aafdaca7bcb0a46d459.jpg)](http://jingyan.baidu.com/album/e73e26c06597a124adb6a7a6.html?picindex=14)

    [![ubuntu如何使用VPN](https://imgsa.baidu.com/exp/w=500/sign=3b2925d1a4773912c4268561c8198675/f603918fa0ec08fa9c1770cb54ee3d6d55fbda43.jpg)](http://jingyan.baidu.com/album/e73e26c06597a124adb6a7a6.html?picindex=15)

11. 11

    稍等片刻认证成功后，会弹出窗口提示VPN连接成功，如下面图中所示。然后就可以通过VPN连接到你想连接的内网中去了。

    [![ubuntu如何使用VPN](https://imgsa.baidu.com/exp/w=500/sign=7da1d18a2a7f9e2f70351d082f30e962/08f790529822720ed0d9819676cb0a46f21fab43.jpg)](http://jingyan.baidu.com/album/e73e26c06597a124adb6a7a6.html?picindex=16)

 