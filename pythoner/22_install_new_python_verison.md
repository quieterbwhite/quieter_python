### 安装其他版本的 Python 到系统



#### 从源代码编译安装python

```shell
1. $ wget -c https://www.python.org/ftp/python/2.7.9/Python-2.7.9.tgz  
2. $ tar -xzvf Python-2.7.9.tgz  
3. $ cd Python-2.7.9/  
4. $ LDFLAGS="-L/usr/lib/x86_64-linux-gnu" ./configure  
5. $ make  
6. $ sudo make install   
```

```
其中，　上面的wget -c (url)是下载命令，参数-c表示支持断点下载, url是目标文件下载的绝对路径　
“-L/usr/lib/x86_64-linux-gnu”中的x86_64-linux-gnu在/usr/lib/下可以找到，　这是x86_64可以看出我的系统是64的, 这里根据自己的系统进行键入。

成功执行上述命令过后，新的Python的可执行程序就在　/usr/local/bin 下面，可以直接使用了。
```



#### 从PPA(Personal Package Archives) 安装apt工具包

```shell
1. $ sudo apt-get install python-software-properties  
2. $ sudo add-apt-repository ppa:fkrull/deadsnakes  
3. $ sudo apt-get update  
4. $ sudo apt-get install python2.7  

```

```
类似使用apt工具包安装python的工具虽然简单，　但有时不一定能够安装到最新版本。因此，　在python出现重要更新时，　我们最好学会以从源代码直接编译安装python2.7.
```



