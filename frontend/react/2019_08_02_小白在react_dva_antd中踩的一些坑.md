[![养猪大户](https://avatar-static.segmentfault.com/187/753/1877532009-5bed73a17f3cd_big64)](https://segmentfault.com/u/erin20188)

[**养猪大户**](https://segmentfault.com/u/erin20188) ![img](https://static.segmentfault.com/v-5d2ffc9a/global/img/rp.svg)0 关注作者

2018-12-17 发布

[小白在react+dva+antd中踩的一些坑](https://segmentfault.com/a/1190000017404075)

-   [react.js](https://segmentfault.com/t/react.js/blogs)
-   [dva.js](https://segmentfault.com/t/dva.js/blogs)
-   [antd](https://segmentfault.com/t/antd/blogs)

记录下来，一来给自己提醒，二来帮助一些朋友们解决问题。
大部分都是很傻的坑，但就是踩了，orz

1.  样式方面

------

1）、使用antd的table 想要改变td的样式，比如想要显示不完时省略

```
下图中2是官方文档的写法，当我们想要改变td样式时可以自己写一个render，见1
```

![clipboard.png](https://segmentfault.com/img/bVblaML?w=765&h=645)

2.逻辑方面

------

```
用的是dva，先简要概括一些model里各个的用法：
    namespace：唯一
    state:初始化数据
    subscriptions:路由变化，拿页面最初始数据   监听
    effects:请求数据 处理异步action
    reducers: 更新数据
    
1）、想向后端发送一个请求，得到返回值后再提交另一个请求，像promise.then一样。
    错误思路：
    一开始很傻地直接前后写了两个dispatch，结果错误，虽然分前后顺序调用了接口（dispatch是同步执行的），可是并没有根据第一个dispatch的结果动态调用第二个接口。
    
    解决方法：
    在model里的effects中相关的函数里调用第二个接口

```

![clipboard.png](https://segmentfault.com/img/bVblbgb?w=894&h=728)

```
所以使用effects的put来触发action。

首先用dispatch向后端发起第一个请求，

```

![clipboard.png](https://segmentfault.com/img/bVblbqF?w=576&h=468)

```
接着在effects里addAddressable函数里调用第二个请求

model.js：

```

![clipboard.png](https://segmentfault.com/img/bVblbsL?w=1090&h=775)

2）、如何在effects里获取state里维护的值

如上图，payload里需要sate里的deviceName、description等
根据前面的图应该知道应该用select
可是网上大概有两种方法：
const todos = yield select(state => state.todos);
const {id} = yield select(_=>_.storeIf) storeIf 是model的namespace

我使用第一种获取不到，原因还不知道。所以如果法一获取不到，不妨用法二

const {deviceName,description,templateDetail} = yield select(_=>_.device);

3）、如何在render里动态渲染不同的div？在render中使用if else会报错

```
解决：使用三元运算符 a?b:c
a是一个触发不同div的条件，b是一个div,c是另一个div


```

4）、根据后端数据动态渲染input数量，并且把输入值存到state中
接受到的数据肯定是一个对象，类似：
{

```
{
    a:1
},
{
    b:2
}
```

}
用map遍历得到a,b。
但接下来一个问题是动态存入数据。
*解决： 
（！！！！！！
这是第一版写的解决，后来遇到问题，比如如果我要在点击完成按钮检测input输入框都不能为空，那去判断哪个字段呢？？？去问老师，发现这种的思路是错的）

```
把后端可能要显示的字段都先在model的state中设置初始值。
我这里是可能显示port或者address.
在state写:
{
    address:"",
    port:0
}
通过[] 可以动态存入port或者address
```

![clipboard.png](https://segmentfault.com/img/bVblbHN?w=1326&h=450)*

正确的解决思路（新）：

把后端传来的数据化简一下，把你需要的数据存在一个新的字段(比如叫linkinfo)里，这个字段根据数据结构我们这里是对象类型。然后每次input触发onChange时，去linkinfo查找到对应的key值，然后改变key值的value。

蓝色框框是相较第一版改变的地方
![clipboard.png](https://segmentfault.com/img/bVblKIp?w=967&h=582)

然后开始写changLinkInput这个函数：

4.1）这里我有踩到一个傻吊坑，给这个函数传了一个val值，那么在这个函数接受的时候val值应该写在前面，默认的e(也就是输入事件)应该写在最后。

假设A是这样的:
A:{

```
a:'小敏',
b:'女'
```

}
那么
A:{

```
...A,
a
```

}
这种写法相当于把A这个对象遍历，就可以直接在下面代码中写 a ,就可以获取到a的值了

```
 const changeLinkInput=(val,e)=>{
    dispatch({
      type:'device/updateStates',
      payload:{
        linkinfo:{
          ...linkinfo,
          //使用[val.name]可以找到当前input对应的key值
          [val.name]:e.target.value  
        }
      }
    })
  }
```

暂时遇到的就是这样了，其实准确来说也不是坑，是我在学习这个上的比较费时间的一些东西。发出来就是希望大家百度问题时看到，尽快解决，少花点时间。