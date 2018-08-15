# [使用Python+selenium+Phantom.js爬取js加载数据的网页](https://blog.yasking.org/a/python-selenium-phantomjs.html)

Published: 2015-07-09

By [solideogloria](https://blog.yasking.org/author/solideogloria.html)

tags: [Python](https://blog.yasking.org/tag/python.html) [selenium](https://blog.yasking.org/tag/selenium.html) [Phantomjs](https://blog.yasking.org/tag/phantomjs.html)

1. [selenium与phantomjs](https://blog.yasking.org/a/python-selenium-phantomjs.html#1)
2. [判断网页是否为js加载数据](https://blog.yasking.org/a/python-selenium-phantomjs.html#2)
3. [编译phantomjs](https://blog.yasking.org/a/python-selenium-phantomjs.html#3)
4. [一个例子](https://blog.yasking.org/a/python-selenium-phantomjs.html#4)
5. [多进程改进](https://blog.yasking.org/a/python-selenium-phantomjs.html#5)
6. [在Centos下使用phantomjs](https://blog.yasking.org/a/python-selenium-phantomjs.html#6)
7. [编译好的phantom下载](https://blog.yasking.org/a/python-selenium-phantomjs.html#7)

------

#### 1. selenium与phantomjs

Selenium是一个用于Web应用程序测试的工具，Selenium测试直接运行在浏览器中，就像真正的用户在操作一样

Selenium支持众多浏览器，如IE、Firefox、Chrome等等，他可以模拟用户的访问，这样，就可以访问js加载的数据，但是常规浏览器每次访问网站都会调用浏览器，打开界面，致使脚本不能运行在后台，无法集成到脚本自动运行，不过，好在有一个强大的无界面浏览器phantom.js，配合selenium使用，就可以抓取网站通过js加载的数据，“所见即所得”

------

#### 2. 判断网页是否为js加载数据

举个例子 <http://data.eastmoney.com/report/>

打开如上网站，通过两种方式查看网站源代码会有不同

第一种是“右键”- “查看源代码”，通过这种方式，我们是无法看到“最新研报”的数据的

第二种是在“研报”上点击“右键” - “审查元素”，通过这种方式，我们可以看到数据

这就说明网站数据是js加载的，如果不是js加载的，我们使用urllib2下载网页直接就可以解析数据了，但是下载的数据是第一种情况看到的代码，如果是js加载的，我们需要模拟浏览器的行为，等js加载完成再获取源代码，这样就获取到了第二种情况看到的数据

------

#### 3. 编译phantomjs

windows用户可以直接在[官网下载](http://phantomjs.org/download.html)phantom.js，Linux下暂时没有编译完成的，需要自己进行编译，如果你是Fedora系统，可以[下载](http://dd-pan.b0.upaiyun.com/ishell/phantomjs-2.0.1-development-for-fedora)我编译完成的可执行程序 ——`20150709`

------

如下是在Fedora22下的编译过程记录：

编译是需要一些基础环境的

```
sudo dnf groupinstall "Development Tools"
sudo dnf -y install gcc gcc-c++ make flex bison gperf ruby \
  openssl-devel freetype-devel fontconfig-devel libicu-devel sqlite-devel \
  libpng-devel libjpeg-devel
```

下载phantomjs

```
git clone git://github.com/ariya/phantomjs.git
cd phantomjs
git checkout 2.0
```

编译之前，我们还需要修改一点源码来绝解决如下的报错信息：

> g++ -fdebug-types-section -Wl,-O1 -fuse-ld=gold -Wl,-rpath,/home/sincerefly/Downloads/phantomjs/src/qt/qtwebkit/lib -o ../../bin/jsc .obj/jsc.o -Wl,-whole-archive -lJavaScriptCore -Wl,-no-whole-archive -L/home/sincerefly/Downloads/phantomjs/src/qt/qtwebkit/Source/JavaScriptCore/release -Wl,-whole-archive -lWTF -Wl,-no-whole-archive -L/home/sincerefly/Downloads/phantomjs/src/qt/qtwebkit/Source/WTF/release -licui18n -licuuc -licudata -L/home/sincerefly/Downloads/phantomjs/src/qt/qtbase/lib -lQt5Core -lpthread -lz -licui18n -licuuc -licudata -lm -ldl -lrt -lpthread /home/sincerefly/Downloads/phantomjs/src/qt/qtwebkit/Source/JavaScriptCore/release/libJavaScriptCore.a(JSArray.o):JSArray.cpp:function JSC::JSArray::push(JSC::ExecState*, JSC::JSValue): error: undefined reference to 'void JSC::JSObject::putByIndexBeyondVectorLengthWithoutAttributes<(unsigned char)20>(JSC::ExecState*, unsigned int, JSC::JSValue)' collect2: 错误：ld 返回 1 Makefile.jsc:98: recipe for target '../../bin/jsc' failed make[2]:**[../../bin/jsc] Error 1 make[2]: Leaving directory '/home/sincerefly/Downloads/phantomjs/src/qt/qtwebkit/Source/JavaScriptCore' Makefile.JavaScriptCore:126: recipe for target 'sub-jsc-pro-make_first-ordered' failed make[1]:** [sub-jsc-pro-make_first-ordered] Error 2 make[1]: Leaving directory '/home/sincerefly/Downloads/phantomjs/src/qt/qtwebkit/Source/JavaScriptCore' Makefile:91: recipe for target 'sub-Source-JavaScriptCore-JavaScriptCore-pro-make_first-ordered' failed make: *** [sub-Source-JavaScriptCore-JavaScriptCore-pro-make_first-ordered] Error 2

这个问题不是phantom.js自身的issue，是GCC5.1与qt之间的问题。问题讨论在：<https://github.com/ariya/phantomjs/issues/13265>

代码已经有补丁，根据<https://codereview.qt-project.org/#/c/107921/3/Source/JavaScriptCore/runtime/JSObject.cpp>修改即可。修改的文件就是/phantomjs/src/qt/qtwebkit/Source/JavaScriptCore/runtime/JSObject.cpp

其实就是把如下内容加到JSObject.cpp中的1912行

```
// Used in JSArray.cpp so we must instantiate explicit
template void JSObject::putByIndexBeyondVectorLengthWithoutAttributes<Int32Shape>(ExecState* exec, unsigned i, JSValue value);
template void JSObject::putByIndexBeyondVectorLengthWithoutAttributes<DoubleShape>(ExecState* exec, unsigned i, JSValue value);
template void JSObject::putByIndexBeyondVectorLengthWithoutAttributes<ContiguousShape>(ExecState* exec, unsigned i, JSValue value);
```

接下来，在终端下键入如下命令进行编译

```
./build.sh
```

大概需要半个小时，编译完成后，在源码的bin目录下会有phantomjs程序，在同级目录新建hello.js文件，内容如下，用来测试phantomjs是否能够正常使用

```
console.log('Hello, world!');
phantom.exit();
```

运行./phantomjs hello.js会输出

```
Hello, world!
```

------

#### 4. 一个例子

```
#!/bin/env python
#encoding:utf-8
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re
import json
import base64

# static
MAX_NUMBER = 10
startTime = int(time.time())

# 匹配网站的数据
pattern = re.compile(r'<tbody>([\s\S]+)</tbody>')

print "-"*6 + ' start ' + '-'*6
for page in range(1, MAX_NUMBER + 1):

    # 拼接网站的URL
    params = 'tp=1&cg=0&dt=2&page=' + str(page)
    base64encode = base64.b64encode(params)

    URL = 'http://data.eastmoney.com/report/#' + base64encode

    driver = webdriver.PhantomJS("./phantomjs")
    driver.set_window_size(1366, 768) 
    driver.get(URL)

    bodyStr= driver.find_element_by_tag_name("body").get_attribute("innerHTML")
    #print bodyStr

    driver.quit() # 每一次抓取URL都需要关闭driver，重新建立，否则无法循环使用

    match = pattern.search(bodyStr)

    if match:
        string = match.group(1)
    else:
        print 'Error: ' + str(page) + '/' + str(MAX_NUMBER) + 'No data'

    # 将数据每页数据拼接
    l = []
    for row in BeautifulSoup(string, "html.parser")("tr"):

        data = {
            "date": row("td")[1]("span")[0]["title"],
            "code": row("td")[2].text,
            "name": row("td")[3].text,
            "title": row("td")[5].text,
            "suggest": row("td")[6].text,
            "change": row("td")[7].text,
            "author": row("td")[8].text,
            "a1": row("td")[9].text,
            "a2": row("td")[10].text,
            "b1": row("td")[11].text,
            "b2": row("td")[12].text,
        }
        l.append(data)

    #print l
    useSeconds = str(int(time.time()) - startTime)
    print 'Success: ' + str(page) + '/' + str(MAX_NUMBER) + '\t' + base64encode +  '\tTotalUseTime: ' + useSeconds + 's'

print "-"*6 + ' end ' + '-'*6
```

**输出**：

```
------ start ------
Success: 1/10   dHA9MSZjZz0wJmR0PTImcGFnZT0x    TotalUseTime: 11s
Success: 2/10   dHA9MSZjZz0wJmR0PTImcGFnZT0y    TotalUseTime: 14s
Success: 3/10   dHA9MSZjZz0wJmR0PTImcGFnZT0z    TotalUseTime: 21s
Success: 4/10   dHA9MSZjZz0wJmR0PTImcGFnZT00    TotalUseTime: 25s
Success: 5/10   dHA9MSZjZz0wJmR0PTImcGFnZT01    TotalUseTime: 28s
Success: 6/10   dHA9MSZjZz0wJmR0PTImcGFnZT02    TotalUseTime: 31s
Success: 7/10   dHA9MSZjZz0wJmR0PTImcGFnZT03    TotalUseTime: 38s
Success: 8/10   dHA9MSZjZz0wJmR0PTImcGFnZT04    TotalUseTime: 45s
Success: 9/10   dHA9MSZjZz0wJmR0PTImcGFnZT05    TotalUseTime: 50s
Success: 10/10  dHA9MSZjZz0wJmR0PTImcGFnZT0xMA==    TotalUseTime: 54s
------ end ------
```

如上代码可以获取到通过js加载的数据，同理，很多网站的数据都可以通过如上方法抓取，而且selenium+phantom.js模拟浏览器发挥想象，可以做更多的事情，值得去探索

------

#### 5. 多进程改进

在上面的例子中，虽然我们能爬取数据，但是效率很低，而且phantom.js本就不高效，几千条数据基本上就等的很烦了

所以现在我们需要用多进程来加快速度，如下是两个演示程序，展示单进程和多进程的爬取速度

`test_singleprocessing.py`

```
#!/bin/env python
#encoding:utf-8
from multiprocessing import Pool
from bs4 import BeautifulSoup
import time
import requests

def get_Data(url):
    start = time.time()
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    title = soup.find_all('div', class_='report-title')[0]("h1")[0].text
    end = time.time()
    print '%s runs %0.2f seconds.' % (title, (end - start))

if __name__=='__main__':

    # 50 url
    url_list = [
        'http://data.eastmoney.com/report/20150430/APPGMH5GQzzLASearchReport.html',
        'http://data.eastmoney.com/report/20150430/APPGMH5GQzpUASearchReport.html',
        'http://data.eastmoney.com/report/20150430/APPGMH5GQzzHASearchReport.html',
        'http://data.eastmoney.com/report/20150430/APPGMH5GQzzRASearchReport.html',
        'http://data.eastmoney.com/report/20150430/APPGMH5GQzzIASearchReport.html',
        'http://data.eastmoney.com/report/20150430/APPGMH5GR2ILASearchReport.html',
        'http://data.eastmoney.com/report/20150430/APPGMH5GR2bKASearchReport.html',
        'http://data.eastmoney.com/report/20150430/APPGMH5GR2beASearchReport.html',
        'http://data.eastmoney.com/report/20150430/APPGMH5GR33EASearchReport.html',
        'http://data.eastmoney.com/report/20150430/APPGMH5GR35UASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8SulMpASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8SulMBASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8SulU5ASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8SulYxASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8SulVEASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8SulbKASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8SuleSASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8SulhqASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8SulndASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8SultcASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8Sum4AASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8SulzuASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8Sum9nASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8SumHqASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8SumIsASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8SumIgASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8SumIhASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8SumJwASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8SumLNASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8SumNdASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8SumPCASearchReport.html',
        'http://data.eastmoney.com/report/20150616/APPGN2AwEpcGASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8SumQeASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8SumS1ASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8SumTrASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8SumUZASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8SumbJASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8SumjDASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8SumjGASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8SumwVASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8SunBJASearchReport.html',
        'http://data.eastmoney.com/report/20150616/APPGN2AwEnnUASearchReport.html',
        'http://data.eastmoney.com/report/20150616/APPGN2AwEnqMASearchReport.html',
        'http://data.eastmoney.com/report/20150616/APPGN2AwEnmZASearchReport.html',
        'http://data.eastmoney.com/report/20150616/APPGN2AwEnrgASearchReport.html',
        'http://data.eastmoney.com/report/20150616/APPGN2AwEp7YASearchReport.html',
        'http://data.eastmoney.com/report/20150616/APPGN2AwEp7TASearchReport.html',
        'http://data.eastmoney.com/report/20150616/APPGN2AwEpI1ASearchReport.html',
        'http://data.eastmoney.com/report/20150615/APPGN1vwyGuYASearchReport.html',
        'http://data.eastmoney.com/report/20150615/APPGN1vwyGwaASearchReport.html'
    ]

    print 'Waiting for ...'
    t1 = time.time()
    for url in url_list:
        get_Data(url)    

    t2 = time.time()
    print 'Done. use %0.2f seconds' % (t2-t1)
```

**结果**:

```
Waiting for ...
线上线下齐发力，国企改革即将落地 runs 0.33 seconds.
中小盘公司信息更新报告：战投中植入驻，转型商业保理可期 runs 0.35 seconds.
去库存和新老产品过渡的阵痛期，新品发力在望 runs 0.36 seconds.
单季度营收环比改善，国企改革触发基本面腾飞 runs 0.36 seconds.
行业发展带动业绩高增长，能源互联网进行时 runs 0.38 seconds.
营收净利高成长，柔性供应好管理，持股计划安军心 runs 0.35 seconds.
新产品收获期到来，业绩拐点将现 runs 0.42 seconds.
公司点评：业绩符合预期，云猴O2O战略坚定执行 runs 0.65 seconds.
员工持股计划完成，战略继续推进势不可挡 runs 1.06 seconds.
2015年一季报点评：盈利提升，U+生态圈构建日趋完善 runs 0.84 seconds.
西南铁路建设龙头，泛亚铁路最大受益者 runs 0.39 seconds.
医院资源&医疗数据是核心竞争力 runs 0.60 seconds.
业绩企稳向好，转型打开空间 runs 0.59 seconds.
中亚建线带来较大业绩弹性 runs 0.47 seconds.
肿瘤医疗服务全产业链布局完成 runs 0.35 seconds.
预计公司上市10个交易日内股价核心波动区间为70元-85元 runs 1.06 seconds.
搭建金融平台，医疗O2O闭环模式加速全国布局 runs 0.69 seconds.
全球高铁大机遇，定增降负债促转型 runs 0.74 seconds.
定增百亿投资国内四大项目，主业经营更稳健 runs 0.48 seconds.
全球民爆整合者和龙头锂盐供应商 runs 1.78 seconds.
拟收购武汉南瑞，内生外延齐发力 runs 2.23 seconds.
大股东变更催生机遇，重点产品成长空间大 runs 0.52 seconds.
清洁煤气应用领域拓宽，高环保压力下的最优选择 runs 0.56 seconds.
SUV产品密集投放，15年业绩高增长可期 runs 1.76 seconds.
发布股权激励方案，进军互联网金融 runs 0.50 seconds.
国企改革将助推化工业务发展进入快车道 runs 0.41 seconds.
能源结构优化，资产注入可期 runs 1.18 seconds.
商业广场陆续开业 公司价值将提升 runs 1.65 seconds.
静待“文化平台型公司”的华丽蜕变 runs 1.93 seconds.
集运旺季迭加油价下跌，双重利好促公司业绩改善 runs 0.77 seconds.
国内领先的通风系统装备供应商，积极布局核电领域 runs 0.93 seconds.
增资入股桎影数码，涉足虚拟现实 runs 1.11 seconds.
收购武汉南瑞100%股权，增强协同效应，构建新增长点 runs 0.88 seconds.
基本面良好 资本限制打开后发展空间巨大 runs 0.67 seconds.
原有业务处于快速增长期，CF光刻胶和丙肝新药中间体打开长期成长空间 runs 0.39 seconds.
综合海岛开发将成公司下一个看点 runs 0.44 seconds.
进军跨境电商，服务全国人民 runs 0.55 seconds.
收购相关资产，涉足机器人领域 runs 0.64 seconds.
打造更专业化的电网“天猫”平台 runs 0.51 seconds.
妇儿类中成药品牌企业 runs 0.35 seconds.
海外并购进一步提升公司综合竞争力 runs 0.56 seconds.
“互联网+”战略迈出第一步 runs 0.52 seconds.
激活用户突破千万，关注资本运作计划 runs 0.34 seconds.
工具行业空间巨大，公司具备高速成长预期 runs 0.34 seconds.
皮革全产业链互联网+，2.0转型扩张再发力 runs 0.34 seconds.
公司研究报告：加速布局环保装备业，天保重装整装待发 runs 1.06 seconds.
公司跟踪报告：看好公司对产业链布局的进一步完善 runs 0.52 seconds.
互联网金融生态喷薄欲出 runs 1.02 seconds.
首家服装设计上市公司 runs 0.34 seconds.
股权变更提供想象空间 超薄电子玻璃与多晶硅弹性可期 runs 0.32 seconds.
Done. use 35.61 seconds
```

下面是多进程的：

```
#!/bin/env python
#encoding:utf-8
from multiprocessing import Pool
from bs4 import BeautifulSoup
import os, time
import requests

def get_Data(url):
    start = time.time()
    page = requests.get(url).text
    soup = BeautifulSoup(page, "html.parser")
    title = soup.find_all('div', class_='report-title')[0]("h1")[0].text
    end = time.time()
    print '%s runs %0.2f seconds.' % (title, (end - start))

if __name__=='__main__':

    t1 = time.time()
    print 'Parent process %s.' % os.getpid()
    p = Pool()

    # 50 url
    url_list = [
        'http://data.eastmoney.com/report/20150430/APPGMH5GQzzLASearchReport.html',
        'http://data.eastmoney.com/report/20150430/APPGMH5GQzpUASearchReport.html',
        'http://data.eastmoney.com/report/20150430/APPGMH5GQzzHASearchReport.html',
        'http://data.eastmoney.com/report/20150430/APPGMH5GQzzRASearchReport.html',
        'http://data.eastmoney.com/report/20150430/APPGMH5GQzzIASearchReport.html',
        'http://data.eastmoney.com/report/20150430/APPGMH5GR2ILASearchReport.html',
        'http://data.eastmoney.com/report/20150430/APPGMH5GR2bKASearchReport.html',
        'http://data.eastmoney.com/report/20150430/APPGMH5GR2beASearchReport.html',
        'http://data.eastmoney.com/report/20150430/APPGMH5GR33EASearchReport.html',
        'http://data.eastmoney.com/report/20150430/APPGMH5GR35UASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8SulMpASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8SulMBASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8SulU5ASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8SulYxASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8SulVEASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8SulbKASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8SuleSASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8SulhqASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8SulndASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8SultcASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8Sum4AASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8SulzuASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8Sum9nASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8SumHqASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8SumIsASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8SumIgASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8SumIhASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8SumJwASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8SumLNASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8SumNdASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8SumPCASearchReport.html',
        'http://data.eastmoney.com/report/20150616/APPGN2AwEpcGASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8SumQeASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8SumS1ASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8SumTrASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8SumUZASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8SumbJASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8SumjDASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8SumjGASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8SumwVASearchReport.html',
        'http://data.eastmoney.com/report/20141218/APPFjG8SunBJASearchReport.html',
        'http://data.eastmoney.com/report/20150616/APPGN2AwEnnUASearchReport.html',
        'http://data.eastmoney.com/report/20150616/APPGN2AwEnqMASearchReport.html',
        'http://data.eastmoney.com/report/20150616/APPGN2AwEnmZASearchReport.html',
        'http://data.eastmoney.com/report/20150616/APPGN2AwEnrgASearchReport.html',
        'http://data.eastmoney.com/report/20150616/APPGN2AwEp7YASearchReport.html',
        'http://data.eastmoney.com/report/20150616/APPGN2AwEp7TASearchReport.html',
        'http://data.eastmoney.com/report/20150616/APPGN2AwEpI1ASearchReport.html',
        'http://data.eastmoney.com/report/20150615/APPGN1vwyGuYASearchReport.html',
        'http://data.eastmoney.com/report/20150615/APPGN1vwyGwaASearchReport.html'
    ]

    for url in url_list:
        p.apply_async(get_Data, args=(url,))

    print 'Waiting for all subprocesses done...'
    p.close()
    p.join()
    t2 = time.time()

    print 'All subprocesses done. use %0.2f seconds' % (t2-t1)
```

**结果**：

```
Parent process 19757.
Waiting for all subprocesses done...
单季度营收环比改善，国企改革触发基本面腾飞 runs 0.34 seconds.
线上线下齐发力，国企改革即将落地 runs 0.38 seconds.
去库存和新老产品过渡的阵痛期，新品发力在望 runs 0.41 seconds.
中小盘公司信息更新报告：战投中植入驻，转型商业保理可期 runs 0.42 seconds.
公司点评：业绩符合预期，云猴O2O战略坚定执行 runs 0.42 seconds.
新产品收获期到来，业绩拐点将现 runs 0.43 seconds.
营收净利高成长，柔性供应好管理，持股计划安军心 runs 0.46 seconds.
员工持股计划完成，战略继续推进势不可挡 runs 0.37 seconds.
西南铁路建设龙头，泛亚铁路最大受益者 runs 0.37 seconds.
2015年一季报点评：盈利提升，U+生态圈构建日趋完善 runs 0.39 seconds.
中亚建线带来较大业绩弹性 runs 0.38 seconds.
业绩企稳向好，转型打开空间 runs 0.46 seconds.
医院资源&医疗数据是核心竞争力 runs 0.48 seconds.
行业发展带动业绩高增长，能源互联网进行时 runs 1.39 seconds.
搭建金融平台，医疗O2O闭环模式加速全国布局 runs 0.32 seconds.
预计公司上市10个交易日内股价核心波动区间为70元-85元 runs 0.36 seconds.
全球高铁大机遇，定增降负债促转型 runs 0.41 seconds.
全球民爆整合者和龙头锂盐供应商 runs 0.33 seconds.
定增百亿投资国内四大项目，主业经营更稳健 runs 0.40 seconds.
拟收购武汉南瑞，内生外延齐发力 runs 0.37 seconds.
肿瘤医疗服务全产业链布局完成 runs 1.04 seconds.
大股东变更催生机遇，重点产品成长空间大 runs 0.38 seconds.
清洁煤气应用领域拓宽，高环保压力下的最优选择 runs 0.42 seconds.
SUV产品密集投放，15年业绩高增长可期 runs 0.45 seconds.
发布股权激励方案，进军互联网金融 runs 0.34 seconds.
国企改革将助推化工业务发展进入快车道 runs 0.36 seconds.
能源结构优化，资产注入可期 runs 0.34 seconds.
商业广场陆续开业 公司价值将提升 runs 0.32 seconds.
静待“文化平台型公司”的华丽蜕变 runs 0.50 seconds.
国内领先的通风系统装备供应商，积极布局核电领域 runs 0.34 seconds.
集运旺季迭加油价下跌，双重利好促公司业绩改善 runs 0.56 seconds.
增资入股桎影数码，涉足虚拟现实 runs 0.40 seconds.
基本面良好 资本限制打开后发展空间巨大 runs 0.36 seconds.
收购武汉南瑞100%股权，增强协同效应，构建新增长点 runs 0.43 seconds.
综合海岛开发将成公司下一个看点 runs 0.46 seconds.
进军跨境电商，服务全国人民 runs 0.35 seconds.
原有业务处于快速增长期，CF光刻胶和丙肝新药中间体打开长期成长空间 runs 0.59 seconds.
收购相关资产，涉足机器人领域 runs 0.55 seconds.
海外并购进一步提升公司综合竞争力 runs 0.31 seconds.
妇儿类中成药品牌企业 runs 0.36 seconds.
打造更专业化的电网“天猫”平台 runs 0.48 seconds.
“互联网+”战略迈出第一步 runs 0.57 seconds.
工具行业空间巨大，公司具备高速成长预期 runs 0.44 seconds.
皮革全产业链互联网+，2.0转型扩张再发力 runs 0.46 seconds.
激活用户突破千万，关注资本运作计划 runs 0.67 seconds.
公司研究报告：加速布局环保装备业，天保重装整装待发 runs 0.48 seconds.
互联网金融生态喷薄欲出 runs 0.46 seconds.
公司跟踪报告：看好公司对产业链布局的进一步完善 runs 0.51 seconds.
首家服装设计上市公司 runs 0.33 seconds.
股权变更提供想象空间 超薄电子玻璃与多晶硅弹性可期 runs 0.92 seconds.
All subprocesses done. use 6.52 seconds
```

相比于单进程的35.61s，6.52s已经有不少的提高，更高效的方法还有待摸索。

------

#### 6. 在Centos下使用phantomjs

`2015-08-20` 如下“引用”中的内容不准确，请跳过，看之后的更新内容

> 在阿里云的Centos服务器环境下，尝试编译phantomjs，问题颇多，放弃编译的想法，而且生产环境尽量避免编译软件
>
> 相比于Fedora，Centos用户还是多不少的，难以编译这可怎么搞，还好，有可以下载的编译好的版本，操作如下:
>
> 1. 安装必要的软件包 `bash yum install fontconfig freetype freetype-devel fontconfig-devel libstdc++`
> 2. 下载phantomjs
>
> `bash wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-1.9.8-linux-x86_64.tar.bz2` 3. 安装
>
> `bash mkdir -p /opt/phantomjs tar -xjvf ~/downloads/phantomjs-1.9.8-linux-x86_64.tar.bz2 --strip-components 1 /opt/phantomjs/ ln -s /opt/phantomjs/bin/phantomjs /usr/bin/phantomjs`
>
> 1. 测试 `bash phantomjs /opt/phantomjs/examples/hello.js`
>
> 参考: <http://www.bonusbits.com/wiki/HowTo:Install_PhantomJS_on_CentOS>

如上的内容也有一定的参考价值，但是现在看来用处不大，之前提到的无法在阿里云centos上编译经过试验，是因为源码包的问题，所以一定要按照上面的教程从github上git clone，然后编译，我使用官方网站提供的源码包无法编译！！！

------

#### 7. 编译好的phantom下载

[Fedora22下编译2.0.1-development版本下载](http://dd-pan.b0.upaiyun.com/ishell/phantomjs-2.0.1-development-for-fedora)

[Centos6.5下编译2.0.1-development版本下载](http://dd-pan.b0.upaiyun.com/ishell/phantomjs-2.0.1-development-for-centos6.5)

[Centos下1.9.8版本下载](http://dd-pan.b0.upaiyun.com/ishell/phantomjs-1.9.8-for-centos)

说明：使用之前先对照前面的编译教程安装好所需的库，然后直接在程序中调用Phantomjs程序即可，Fedora下建议使用第一个，没在不同版本下测试，想必21，20也没有问题，Centos下建议使用第二个，第三个是我在网上找的外国友人编译的，也就是“6”中提到的。