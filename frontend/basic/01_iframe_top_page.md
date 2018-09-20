#### 解决iframe重定向让父级页面跳转

>   https://blog.csdn.net/xm_csdn/article/details/78131596

有内嵌iframe的页面，当session过期时，点击连接重定向后的跳转会在iframe中跳转，在登录页面中加入下面的代码，就会在最外层页面跳转:

```javasc
<script language="JavaScript"> 

    if (window != top) {

        top.location.href = location.href; 
    }

</script>
```

window.location.href、location.href   是本页面跳转

parent.location.href    是上一层页面跳转

top.location.href     是最外层的页面跳转