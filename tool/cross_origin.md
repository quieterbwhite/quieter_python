# 跨域
> http://blog.720ui.com/2016/web_cross_domain/  跨域问题，解决之道  

## 1. 方案一，JSONP（废弃）
```
jsonp是带有回调函数callback的json，它是一个很棒的方案，可用于解决主流浏览器的跨域数据访问的问题。

但是，JSONP方案的局限性在于，JSONP只能实现GET请求。
```

## 2. 方案二，CORS（常用）
```
CORS 全称为 Cross Origin Resource Sharing（跨域资源共享）。

浏览器一旦发现AJAX请求跨源，就会自动添加一些附加的头信息，但用户不会有感觉。

因此，实现CORS通信的关键是服务端。

服务端只需添加相关响应头信息，即可实现客户端发出 AJAX 跨域请求。

值得注意的是，浏览器必须先以 OPTIONS 请求方式发送一个预请求，从而获知服务器端对跨源请求所支持 HTTP 方法。
在确认服务器允许该跨源请求的情况下，以实际的 HTTP 请求方法发送那个真正的请求。
```

## 3. 方案三，搭建中间转发层（常用）
```
跨域问题的核心是什么？不同源访问。是啊，如果我们转换成同源请求，就不存在这个问题啦。

因此，我们之前有个项目，通过搭建中间层，当然可以是java，也可以是node.js，通过将服务端的请求进行转发，
换句话说，就是dispatcher了一层，那么前端请求的地址，就被转发了，所以很好的解决跨域问题。

当然，如果对性能有考量的产品，就需要慎重选择这个方案咯，因为多了一层中间转发，不管是网络开销，还是性能负载都是有一定的影响。
```

## 4. 方案四，Nginx反向代理（常用）
```
首先，产品需要搭建一个中转nginx服务器，用于转发请求。当然，我们都是基于Nginx作为反向代理，所以当然是水到渠成。

那么，Nginx的思路，就是通过Nginx解析URL地址的时候进行判断，将请求转发的具体的服务器上。

当用户请求xx.720ui.com/server1的时候，Nginx会将请求转发给Server1这个服务器上的具体应用，从而达到跨域的目的。

但是，我用的是另外一种方法，添加跨域请求需要的头信息就可以了。
```