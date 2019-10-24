# node.js获取时间

> https://www.jianshu.com/p/12e44dcc6c0f

2017.06.26 18:12:39字数 215阅读 7190

# 一、命令行下安装module:

```
npm install silly-datetime
```

可以在node_modules文件里查看是否已经安装好

# 二、在js文件里

```
var sd = require('silly-datetime');
var time=sd.format(new Date(), 'YYYY-MM-DD HH:mm:ss');
console.log(time);
```

时间格式化输出:
`YYYY-MM-DD HH:mm:ss`
关于时间的具体方法

> var myDate = new Date();
> myDate.getYear(); //获取当前年份(2位)
> myDate.getFullYear(); //获取完整的年份(4位,1970-????)
> myDate.getMonth(); //获取当前月份(0-11,0代表1月)
> myDate.getDate(); //获取当前日(1-31)
> myDate.getDay(); //获取当前星期X(0-6,0代表星期天)
> myDate.getTime(); //获取当前时间(从1970.1.1开始的毫秒数)
> myDate.getHours(); //获取当前小时数(0-23)
> myDate.getMinutes(); //获取当前分钟数(0-59)
> myDate.getSeconds(); //获取当前秒数(0-59)
> myDate.getMilliseconds(); //获取当前毫秒数(0-999)
> myDate.toLocaleDateString(); //获取当前日期
> var mytime=myDate.toLocaleTimeString(); //获取当前时间
> myDate.toLocaleString( ); //获取日期与时间