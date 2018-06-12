## Vysor 破解
> https://blog.csdn.net/qq_21793463/article/details/61919151  

```
分析源代码可知软件在uglify-list.js文件内通过_il变量判断是否注册成功, 

pwd: /home/bwhite/.config/google-chrome/Default/Extensions/gidgenkbbabolejbgbpnhbimgjbffefm/1.9.3_0/uglify.js

于是配置该变量为true，打开 uglify.js文件, 搜索 _il变量, 将 _il:Te.a() 替换为 _il:true, 然后重启chrome和vysor. 发现Vysory已经变为专业版了。

将上文中提到的 _il:() 处都替换为 _il:true, 就可以完成破解了。

uglify.js文件在chrome的Extensions文件夹下，可以用开发者模式先找到扩展的id。
```  
