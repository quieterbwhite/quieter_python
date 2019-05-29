# Linux：tar命令批量解压方法总结

2016年12月28日 16:14:27 [silentwolfyh](https://me.csdn.net/silentwolfyh) 阅读数：16497

版权声明：本文为博主原创文章，出处为 http://blog.csdn.net/silentwolfyh https://blog.csdn.net/silentwolfyh/article/details/53909518

由于linux的tar命令不支持批量解压，所以很多网友编写了好多支持批量解压的shell命令，收集了一下，供大家分享： 
**第一：**

```
for tar in *.tar.gz;  do tar xvf $tar; done
for tar in *.tar.bz2; do tar xvf $tar; done12
```

**第二：** 
用tar命令批量解压某个文件夹下所有的tar.gz文件

```
ls *.tar.gz | xargs -n1 tar xzvf1
```

**第三：**

```
find -maxdepth 1 -name "*.bz2"|xargs -i tar xvjf {}1
```

这条命令可解压当前目录下的所有bz2文件

批量解压是比较郁闷的事，以前尝试各种方法，甚至用脚本循环语句解压都不行

现在发现这条命令可以搞定，maxdepth表示搜索深度，1代表只搜索当前目录 
**第四：**

```
for i in $(ls *.tar);do tar xvf $i;done1
```

问题： 
我想进行批量解压tar文件，使用tar -xvf *.tar会出错，提示“Not found in archive”。解决方法有很多，比如写一个脚本之类的。 请问为什么tar不支持这种通配符语法呢？是否有特殊的原因？ 我试过gzip就支gzip -d* .tar.gz。 
回答： 
通配符是shell解决的问题 
如 
tar -xvf *.tar 
实际上执行tar时，tar接收到的是 
tar -xvf a.tar b.tar c.tar … 
如果当前目录跟本没有tar的东西，那么tar就收到’*.tar’这个参数 
与win不同，linux所有字符都可以作文件名，也即目录中不存在着 *.tar这个文件 
为了防止 *.tar被shell解释为a.tar b.tar c.tar… 
可以给它加个单引号

用tar解开一个Archive时，语法是 
tar -xvf ＜tarfile.tar> 
＜tarfile.tar> 是选项f所要求的，只能是一个文件，比如myfiles.tar。 
是myfiles.tar所包含的归了档的文件中的一个或者多个成员文件。如果是多个，可以用通配符。 
先别跟我急，我知道，这些你是清楚的。但是，你的问题是，用了 
tar -xvf *.tar 
如楼上所说，tar接收到的是 
tar -xvf a.tar b.tar c.tar … 
tar把你的意图理解为，在a.tar里解出b.tar c.tar …