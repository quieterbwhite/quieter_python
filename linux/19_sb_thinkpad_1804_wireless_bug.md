先上一下原网站以表尊重： https://github.com/endlessm/linux 给你们网盘分享啊。
1.下载之后解压（右键提取到此处..）找到其中的（上面全下载下来的那些傻哥们这个文件在rtl8821ce里面的）

Makefile文件中把 "export TopDIR ?= ..." 改成 "export TopDIR ?= PATH TO EXTRACTED DIRECTORY" 就是填写当前路径地址（pwd查看当前文件夹所在的路径）【也有改成export TopDIR ?= $(shell pwd)】可以成功的，但我没成功。所以老实的按部就班吧。
代码： 全选

1. make
2. sudo make install
3. sudo modprobe -a 8821ce
第一个，以太网的r8168的驱动：链接：https://pan.baidu.com/s/1dGZC70d 密码：cwsx 
第二个 ，无线网rtl8821ce的压缩包：链接：https://pan.baidu.com/s/1sneDK8d 密码：8930

https://blog.csdn.net/fljhm/article/details/79281655

https://www.jianshu.com/p/90ff6c10f64e

参考这个

