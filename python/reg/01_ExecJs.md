# Python执行Js语句之ExecJs

[未不明不知不觉](https://www.jianshu.com/u/6a2cdcdb3ba6)

##### execjs模块

在网页数据提取的日常中，经常有一些有用的信息以json的格式存放在网页的源代码中，这时候要规则的提取的这些数据，就需要一个能够解析js的包了，execjs提供了简单易用的api

##### 安装

使用pip安装：

```
  pip install PyExecJS
```

使用easy_install安装：

```
  easy_install PyExecJS
```

##### 使用

这里使用了一个网站的网页做示例,它的源代码中有这么一段

 

![img](https://upload-images.jianshu.io/upload_images/944794-824ea85f2dad76a6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/538)

 

我们的目标是提取图中的json数据，代码如下：

```
import requests
import re
import execjs
from lxml import etree

url = 'https://www.madewell.com/cn/madewell_category/SHIRTSTOPS/topsblouses/PRDOVR~F9375/F9375.jsp'
res = requests.get(url)
doc = etree.HTML(res.text)
#s_text = doc.xpath('//script/text()')
#def f(var,text):
#    if var in text:
#        return True
#    return False
#data = filter(partial(f,"var data"),s_text)[0]
data = ''.join(doc.xpath('//script[contains(text(),"var data")]/text()'))
json_raw = re.search('({[\S\s]*\})',data).group(1)
jsn = execjs.eval(json_raw)
print(jsn)
```

执行结果如下图：

 

![img](https://upload-images.jianshu.io/upload_images/944794-52b4909818a894fa.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/527)

#### 扩展

在一些数据的抽取中用到了模拟浏览器，通常我们会用selenium或者其他的webkit包，但是一般的模拟包只是返回了渲染后的页面，有的时候仅仅是返回动态渲染的页面是不够的，还需要能够执行js并控制js与dom交互，有兴趣的同学可以看一下PyV8和w3c包