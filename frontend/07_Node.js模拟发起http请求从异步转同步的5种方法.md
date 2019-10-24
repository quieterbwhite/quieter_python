# Node.js模拟发起http请求从异步转同步的5种方法

> https://juejin.im/post/5b9b7e9a5188255c6140b9c0

使用`Node.js`模拟发起`http`请求很常用的,但是由于`Node`模块（原生和第三方库）提供里面的方法都是异步，对于很多场景下应用很麻烦，不如同步来的方便。下面总结了几个常见的库`API`从异步转同步的几种方法。模块有：`request`, `request-promise` , `request-promise-native` , `request-promise-any`

PS：`Node的版本>=8.0.0 为了使用 Async / Await` PS: 这里加入`auth` 字段是为了需要用户名和密码登录的应用的请求 ，比如`rabbitmq` ,不需要登录的页面可以去掉这个参数。

## 第一种

使用原生模块 `util` , 利用其 `promisify` `API` ， 代码示例如下：

```
const request = require('request');
const util = require('util');
var url = "https://www.baidu.com/";
const getPromise = util.promisify(request.get);
// PS: 这里加入auth 字段是为了需要用户名和密码登录的应用的请求 ，比如rabbitmq ,不需要登录的页面可以去掉这个参数。

//1：  原生写法  无auth 参数
getPromise(url).then((value)=>{
    console.log("value" , value );
}).catch((err)=>{
    console.log("err" , err );
});

//2：  原生写法  有auth 参数
getPromise(url , {'auth' : {
    'user' : 'xx',
    'pass' : 'xx',
    'sendImmediately' : 'false',
}}).then((value)=>{
    console.log("value" , value );
}).catch((err)=>{
    console.log("err" , err );
});

// 第二种写法   async/await

// 个人最建议使用这种 ， 只使用util 和 request 。

async function handle(){

    let result = await getPromise(url , {'auth' : {
        'user' : 'xx',
        'pass' : 'xx',
        'sendImmediately' : 'false',
    }});
    // 可以加入 try catch 捕获异常  也可以加 .catch()
    console.log("result" , result.);
}

handle();

PS: `auth` 参数的用法参考[链接][1]  , 在异步变同步中 不能使用  `request.get().auth()` 写法。
复制代码
```

## 第二种

使用模块 `request-promise-native` , `request-promise-native`是使用 `native Promise` 写的，查看源码可以看到继承自 `Request` 模块 ， 代码示例如下：

```
// 不再写 原生示例  then()链的那种，参考第一个示例即可
//get 请求示例   
const rpn = require('request-promise-native');  
var url = "https://www.baidu.com/";
async function useRequestPromiseNative(){
    // options 里面的参数可以去看request的源码  查看其index.d.ts 文件里面的 interface CoreOptions 里面有所有的参数。
    let options = {
        method: 'GET',
        uri: url,
        auth : {
            'user' : 'xx',
            'pass' : 'xx',
            'sendImmediately' : 'false',
        }
      };
    let  rpnbody = await rpn(options);       
    
    console.log("rpnbody" , rpnbody );
}

useRequestPromiseNative();

// post 示例 
const rpn = require('request-promise-native');
var url = "https://www.baidu.com/";
async function useRequestPromiseNative(){
    let options = {
        method: 'POST',
        uri: url,
        body: {    // 这里定义你的body参数
        }
        json: true, // 这个看你的参数而定
      };
    let  rpnbody = await rpn(options);       
    
    console.log("rpnbody" , rpnbody );
}
useRequestPromiseNative();
复制代码
```

## 第三种

使用模块 `request-promise` , `request-promise`是基于 `bluebird` 写的， 查看源码可以看到继承自 `Request` 模块 ， 代码示例如下：

```
// 不再写post 示例

const rp  = require('request-promise');
var url = "https://www.baidu.com/";
async function useRequestPromise(){
    let options = {
        method: 'GET',
        uri: url,
        auth : {      //可以拿掉
            'user' : 'xx',
            'pass' : 'xx',
            'sendImmediately' : 'false',
        }
      };
    let  rpbody = await rp(options);       
    console.log("rpnbody" , rpbody );
}

useRequestPromise();
复制代码
```

## 第四种

使用模块 `request-promise-any` , `request-promise-any`也是基于 `request` 写的， 代码示例如下：

```
// 不再写post 示例

const rpa = require('request-promise-any');
var url = "https://www.baidu.com/";
async function useRequestPromiseAny(){
    let options = {
        method: 'GET',
        uri: url,
        auth : {
            'user' : 'xx',
            'pass' : 'xx',
            'sendImmediately' : 'false',
        }
      };
    let  rpabody = await rpa(options);       
    console.log("rpabody" , rpabody );
}

useRequestPromiseAny();
复制代码
```

## 第五种

使用模块 `bluebird` , 利用其 `promisifyAll` `API` 转成`Promise` ， 代码示例如下：

```
const Promise = require('bluebird');
const request = require('request');
var url = "https://www.baidu.com/";
Promise.promisifyAll(request, { suffix: 'SC' });  //suffix 自定义 get --> getSC

async function usebluebird(){

    let result = await request.getSC(url , {'auth' : {
        'user' : 'xx',
        'pass' : 'xxx',
        'sendImmediately' : 'false',
    }});
    console.log("result" , result);
}

usebluebird()
复制代码
```

上面总结了5种使用方法，其实要说也不止5种了，大家根据自己需要来选择。