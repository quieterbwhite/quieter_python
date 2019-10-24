# Nodejs try catch捕捉异常失效场景

> https://juejin.im/post/5a31d21cf265da432480744b

## 先看一个和异步无关的错误处理

```
var test = undefined;
try{
    var f1 = function(){
         console.log(test.toString());  
    }
}
catch(e){
    console.log('error..');
}

//TypeError: Cannot read property 'toString' of undefined
//assume somewhere f1() will be called as an call back function
f1();
复制代码
```

`try catch`中的代码仅仅是声明一个变量并且赋值，除非没有足够的内存，否则基本上不会抛出异常，不管f1中的函数有没有错误。`f1`函数的调用根本就没有包含在`try catch`中，所以抛弃出未捕获的异常那是100%的事情（至于赋给它的值所指向的函数有没有错误显然不在它的职责范围之内，毕竟函数在这里没有执行。），这个和异步毫无关系。

## 在看看跟异步相关的

node.js是异步IO执行,所以我们将`try/catch`放置异步回调函数中,当出现一个异常时,`try/catch`操作只能捕获当次事件循环内的异常，我们通过`try` 拿到这个错误时错过了当前程序运行堆栈。(或者理解成，异步错误发生时在`try catch`块结束时候，所以当然不会被catch)

之后 Node 会触发 `uncaughtException`事件,而在node.js原生的`uncaughtException` 处理事件是挂在 `process` 对象上,所以，如果一个异常出现时,当前运行的 `process` 会直接挂掉,导致错误永远不会走到 `catch`语句.

```
var test = undefined;

try{
    
    setTimeout(function(){
    	//TypeError: Cannot read property 'toString' of undefined
         console.log(test.toString());  
    }, 3000)
}
catch(e){
    console.log('error..');
}
复制代码
```

比如，在实际项目中，

```
var deserialize = require('deserialize'); 
// 假设 deserialize 是一个带有 bug 的第三方模块

// app 是一个 express 服务对象
app.get('/users', function (req, res) {
    mysql.query('SELECT * FROM user WHERE id=1', function (err, user) {
        var config = deserialize(user.config); 
        // 假如这里触发了 deserialize 的 bug
        res.send(config);
    });
});
复制代码
```

如果不幸触发了 `deserialize` 模块的 `bug`，这里就会抛出一个异常，最终结果是整个服务 crash。

当这种情况发生在 Web 服务上时结果是灾难性的。`uncaughtException` 错误会导致当前的所有的用户连接都被中断，甚至不能返回一个正常的 HTTP 错误码，用户只能等到浏览器超时才能看到一个`no data received`错误。

这是一种非常野蛮粗暴的异常处理机制，一个友好的错误处理机制应该满足三个条件:

- 对于引发异常的用户，返回 500 页面
- 其他用户不受影响，可以正常访问
- 不影响整个进程的正常运行