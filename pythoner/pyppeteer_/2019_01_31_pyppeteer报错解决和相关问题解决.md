# pyppeteer报错解决和相关问题解决

2019年01月31日 18:01:01 [Nick_Spider](https://me.csdn.net/weixin_39198406) 阅读数：2951

版权声明：本文为博主原创文章，未经博主允许不得转载。	https://blog.csdn.net/weixin_39198406/article/details/86719814

# 1. 报错1：Most likely the page has been closed

```
pyppeteer.errors.NetworkError: Protocol Error (Runtime.callFunctionOn): Session closed. Most likely the page has been closed.
```

使用pyppeteer采集京东的时候,总数到7~8页的时候就报错.
谷歌发现了这样的解决方案:

```
https://github.com/miyakogi/pyppeteer/issues/178
https://github.com/miyakogi/pyppeteer/pull/160/files
```

照着修改了一下源码,就解决了这个问题,在此记录一下.

# 2. 报错2：error while loading shared libraries: libX11-xcb.so.1

在`ubuntu16.04`上，使用`python3.6`运行`pyppeteer`的`demo`：

```
import asyncio
from pyppeteer import launch

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('http://example.com')
    await page.screenshot({'path': 'example.png'})
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
```

报错如下：

```
pyppeteer.errors.BrowserError: Browser closed unexpectedly:
/home/ubuntu/.local/share/pyppeteer/local-chromium/575458/chrome-linux/chrome: error while loading shared libraries: libX11-xcb.so.1: cannot open shared object file: No such file or directory
```

搜索后，找到这条答案[github issue](https://github.com/Googlechrome/puppeteer/issues/290#issuecomment-451471338)
发现安装以下依赖后，报错解决：

```
sudo apt-get install -y libx11-xcb1 libxrandr2 libasound2 libpangocairo-1.0-0 libatk1.0-0 libatk-bridge2.0-0 libgtk-3-0 libnss3 libxss1
```

# 3. 报错3：ModuleNotFoundError: No module named ‘apt_pkg’

如果出现了以下问题：

```
ModuleNotFoundError: No module named 'apt_pkg'
```

可以参考这个链接解决： <https://blog.csdn.net/u014221090/article/details/82657401>

# 4. 问题：在ubuntu16.04下安装python3.6

参考： <https://www.cnblogs.com/yjlch1016/p/8641910.html>