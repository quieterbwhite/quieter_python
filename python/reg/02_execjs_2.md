# python中执行js

> https://xingzx.org/blog/eval-js-in-python



最近有个需求是要在python中执行js代码，原因是业务某些接口直接返回了 js 代码给Web前端执行，我要用 python 脚本去测试这段响应的正确性。幸运的是 python 有现成的模块`execjs`，不必自己去解析了。

到[这里](https://pypi.python.org/pypi/PyExecJS)安装，最好先安装 nodejs，因为它要依赖其他的js解析引擎。

```
pip install PyExecJS
```

使用也是比较简单的，假设有段js代码：

```
code = '''var ver="4.7.1版本";var upgrade=0;function add(x, y) {    return x + y;}'''
```

通过下面的方式去获得 js 变量、js函数执行结果：

```
import execjscontext = execjs.compile(code.decode('utf8'))js_ver = context.eval('ver')func_ret = context.call('add', 1, 2)print "%s%s" % (js_ver, func_ret)
```

这里注意一点，传递给 `execjs` 编译的代码要用 unicode 编码。