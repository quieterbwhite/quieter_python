#### jquery ajax 请求中多出现一次OPTIONS请求及其解决办法

> https://www.tangshuang.net/2271.html

在上一篇《[服务端php解决jquery ajax跨域请求restful api问题及实践](https://www.tangshuang.net/2254.html)》中，我简单介绍了如何通过服务端解决jquery ajax的跨域请求问题，但是，在这个过程中，我们会发现，在很多post,put,delete等请求之前，会有一次options请求。本文主要是来讨论一下这是什么原因引起的。

根本原因就是，W3C规范这样要求了！在跨域请求中，分为简单请求（get和部分post，post时content-type属于application/x-www-form-urlencoded，multipart/form-data，text/plain中的一种）和复杂请求。而复杂请求发出之前，就会出现一次options请求。

什么是options请求呢？它是一种探测性的请求，通过这个方法，客户端可以在采取具体资源请求之前，决定对该资源采取何种必要措施，或者了解服务器的性能。

在ajax中出现options请求，也是一种提前探测的情况，ajax跨域请求时，如果请求的是json，就属于复杂请求，因此需要提前发出一次options请求，用以检查请求是否是可靠安全的，如果options获得的回应是拒绝性质的，比如404\403\500等http状态，就会停止post、put等请求的发出。

虽然在下面的参考文献中有人提出可以取消options请求，但是实测后发现是不行的，jquery封装之后，更不能轻易取消。因此，靠javascript客户端取消options请求是不可能的，只能通过服务端对options请求做出正确的回应，这样才能保证options请求之后，post、put等请求可以被发出。但是，我们不能允许所有的options请求，而应该是有条件的，所以最好是通过一个特殊的机制，去验证客户端发出的options请求数据是否是符合服务端的条件的，如果不满足，返回403，则客户端会取消原有的post计划。

参考文献：

- [探讨跨域请求资源的几种方式](http://www.cnblogs.com/dojo-lzz/p/4265637.html)
- [CORS 中的POST and OPTIONS 请求](http://cnodejs.org/topic/519c234863e9f8a542aa7ebd)
- [POST请求失败，变成options请求](http://www.barretlee.com/blog/2014/08/19/post-method-change-to-options/#comments)
- [$.ajax post方式变成OPTIONS 跨域请求](http://www.oschina.net/question/1014827_115277)
- [Access control allow origin 简单请求和复杂请求](http://blog.csdn.net/wangjun5159/article/details/49096445)
- [HTTP的请求方法OPTIONS](http://blog.csdn.net/leikezhu1981/article/details/7402272)

 2016-03-14  9982

---

