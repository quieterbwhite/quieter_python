# [js replace 全局替换](https://www.cnblogs.com/stubborn-donkey/p/9173089.html)

js 的replace 默认替换只替换第一个匹配的字符，如果字符串有超过两个以上的对应字符就无法进行替换，这时候就要进行一点操作，进行全部替换。

```
<script language="javascript">
var strM = "这是要被替换的字符串啊啊！";
//在此我想将字母a替换成字母A
alert(strM.replace("啊","额"));
</script>
```

上面这段代码，只能替换第一个字符“啊”，第二个“啊”就无法替换，这样就没办法满足大多数使用js(replace)的需求

```
<script type="text/javascript" language="javascript">
var s = "这是要被替换的字符换啊啊！";
alert(s);
alert(s.replace(/啊/g, "额"));
```

这样，就可以实现整个字符串的替换。

我们这里用到了正则函数的/g全部的使用。这样就可以实现整个字符串的替换效果。

下面，我们大家可能还有个需求无法满足，那就是，我们替换定值可以使用这个，但是替换变量怎么使用？

接下来，就说一下替换变量的使用方式。

简单介绍一下eval() 函数可计算某个字符串，并执行其中的的 JavaScript 代码。接下来主要靠这个函数。

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
<script>
var ch = "变量";
var reg = "/"+ch+"/g";
var str = "这是一个变量，这是一个变量";
var val = str.replace(eval(reg),"替换");
alert(val);
</script>
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

但是如果要替换的字符串中含有/符号时，上面的就不能用了，需要采取以下方法

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
<script>
var ch = "/";
var str = "这是一/个变量，这是一个变量";
var val = str .replace(new RegExp(ch,'g'),"b");
alert(val);
</script>
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)