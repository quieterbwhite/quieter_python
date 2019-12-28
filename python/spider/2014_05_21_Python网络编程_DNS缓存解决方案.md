#### [Python网络编程] DNS缓存解决方案

>   https://blog.csdn.net/yueguanghaidao/article/details/26449911
>
>   https://blog.csdn.net/Bone_ACE/article/details/55000101

2014年05月21日 11:36:14

阅读数：4843

一般一个域名的DNS解析时间在10~60毫秒之间，这看起来是微不足道，但是对于大型一点的爬虫而言这就不容忽视了。例如我们要爬新浪微博，同个域名下的请求有1千万（这已经不算多的了），那么耗时在10~60万秒之间，一天才86400秒。也就是说单DNS解析这一项就用了好几天时间，此时加上DNS解析缓存，效果就明显了。

记得以前写爬虫的时候为了防止dns多次查询，是直接修改/etc/hosts文件的，最近看到一个优美的解决方案，修改后记录如下：

```python
import socket
# from gevent import socket

_dnscache={}

def _setDNSCache():
    """
    Makes a cached version of socket._getaddrinfo to avoid subsequent DNS requests.
    """
    def _getaddrinfo(*args, **kwargs):
        global _dnscache
        if args in _dnscache:
            print str(args)+" in cache"
            return _dnscache[args]

        else:
            print str(args)+" not in cache"  
            _dnscache[args] = socket._getaddrinfo(*args, **kwargs)
            return _dnscache[args]

    if not hasattr(socket, '_getaddrinfo'):
        socket._getaddrinfo = socket.getaddrinfo
        socket.getaddrinfo = _getaddrinfo
    
def test():
    _setDNSCache()
    import urllib
    urllib.urlopen('http://www.baidu.com')
    urllib.urlopen('http://www.baidu.com')
```

结果如下：

```python
('www.baidu.com', 80, 0, 1) not in cache
('www.baidu.com', 80, 0, 1) in cache
```

1.相当于只对socket.getaddrinfo打了一个patch，但socket.gethostbyname,socket.gethostbyname_ex还是走之前的策略

2.只对本程序有效，而修改/etc/hosts将对所有程序有效，包括ping

其实也没什么难度，就是将socket里面的缓存保存下来，避免重复获取。 
可以将上面的代码放在一个dns_cache.py文件里，爬虫框架里调用一下这个`_setDNSCache()`方法就行了。

需要说明一下的是，如果你使用了gevent协程，并且用上了monkey.patch_all()，要注意此时爬虫已经改用gevent里面的socket了，DNS解析缓存模块也应该要用gevent的socket才行。