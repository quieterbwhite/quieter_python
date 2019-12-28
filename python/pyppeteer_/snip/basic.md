#### pyppeteer 代码片段

> https://www.anquanke.com/post/id/103350
> https://www.ctolib.com/article/comments/61657
> https://csbun.github.io/blog/2017/09/puppeteer/
> https://www.jianshu.com/p/611ed6b75d47

```python
# https://blog.csdn.net/u012731379/article/details/78671082

import asyncio
from pyppeteer.launcher import launch
# 这里还可以添加别的参数. Macbook 位于: /usr/local/lib/python3.6/site-packages/pyppeteer/launcher.py Launcher.options
browser = launch({"executablePath":"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"})

async def main(browser):
    page = await browser.newPage()
    await page.goto('https://www.baidu.com/')
    print("fun: " + str(dir(page)))
    title = await page.title()
    print("title: " + title)
    element = await page.querySelector('#ftConw')
    text = await element.evaluate('(element) => element.textContent')
    print("text: " + text)

asyncio.get_event_loop().run_until_complete(main(browser))
browser.close()


# fun: ['Events', 'J', 'JJ', 'Jeval', 'PaperFormats', '__annotations__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_add_event_handler', '_client', '_emulationManager', '_events', '_frameManager', '_go', '_handleException', '_ignoreHTTPSErrors', '_keyboard', '_loop', '_mouse', '_networkManager', '_onCertificateError', '_onConsoleAPI', '_onDialog', '_onTargetCrashed', '_pageBindings', '_schedule', '_screenshotTask', '_screenshotTaskQueue', '_touchscreen', '_tracing', '_viewport', 'addScriptTag', 'click', 'close', 'content', 'cookies', 'deleteCookie', 'emit', 'emulate', 'emulateMedia', 'evaluate', 'evaluateOnNewDocument', 'exposeFunction', 'focus', 'frames', 'goBack', 'goForward', 'goto', 'hover', 'injectFile', 'keyboard', 'listeners', 'mainFrame', 'mouse', 'on', 'once', 'pdf', 'plainText', 'press', 'querySelector', 'querySelectorAll', 'querySelectorEval', 'reload', 'remove_all_listeners', 'remove_listener', 'screenshot', 'setContent', 'setCookie', 'setExtraHTTPHeaders', 'setJavaScriptEnabled', 'setRequestInterceptionEnabled', 'setUserAgent', 'setViewport', 'tap', 'title', 'touchscreen', 'tracing', 'type', 'url', 'viewport', 'waitFor', 'waitForFunction', 'waitForNavigation', 'waitForSelector']
# title: 百度一下，你就知道
# text: 把百度设为主页关于百度About  Baidu百度推广©2017 Baidu 使用百度前必读 意见反馈 京ICP证030173号  京公网安备11000002000001号 
```

```python
# https://github.com/GoogleChrome/puppeteer/issues/336
# What about proxy usage? 

let instance = puppeteer.launch({
  args: [
   '--proxy-server=127.0.0.1:9876', // Or whatever the address is 
  ]
});

  const browser = await puppeteer.launch({
    ignoreHTTPSErrors: true,
    args: [
      "--proxy-server=proxy.example.com:8010",
      "--no-sandbox",
      "--disable-setuid-sandbox"
    ]
  });
```

```python
# puppeteer使用记录
# https://juejin.im/post/5b207a226fb9a01e480e9b3e

```
