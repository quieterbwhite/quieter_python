#### README

##### link
```
ubuntu中安装apache ab命令进行简单压力测试
https://blog.csdn.net/Shyllin/article/details/80944974

Apache压力（并发）测试工具ab的使用教程收集
https://www.cnblogs.com/EasonJim/p/8085363.html

用ab进行POST,GET压力测试，且定义header及json的内容
https://blog.csdn.net/weixin_34346099/article/details/90336107

```

##### example
```
ab -n 5 -c 5  -p "post.txt" -T "application/json" -H "Content-Type: application/json" -H "Cache-Control: no-cache" -H "authorization: Bearer cW5kl2GubQBr5N1Xf5LZf3BefXuwMc" -H "client-logo: djnpUwcfXsZB7Xg4ay3k4+LKCL5mtgZ9ggUaEIMgu76Nmhf20VXh8/kGA6JTRGNmiXZuaWge1KupwKswDAsYm84DMEXvgozk4z7ZsfSftr+XXgKRWz8Ll92WlScoLiYg" https://api.fachans.com/apiweb/case/prolist

ab -n 5 -c 5  -p "post.txt" -T "application/json" -H "Content-Type: application/json" -H "Cache-Control: no-cache" -H "authorization: Bearer nbfIKZ7WlnJjwTMBc9oqW6GryekB5n" https://pressureapi.fachans.com/apiweb/case/prolist
```
