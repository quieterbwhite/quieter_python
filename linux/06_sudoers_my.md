# 指定用户执行指定sudo命令不需要输入密码
> 在理想境界的时候用到这个东西  

编辑 /etc/sudoers 文件  
```
sudo visudo
```

如添加下面一行到最后:  
```
# 切记: 用户名 isee 后面跟着的是 tab
isee    ALL=(ALL) NOPASSWD: ALL          # 表示 isee 执行所有 sudo 命令不需要密码

isee    ALL=(ALL) NOPASSWD: /bin/mv,/bin/kill   # 表示 isee 执行指定的 sudo 命令不需要密码
```

如果改错了 visodoers 文件   

报错:  
```
i56@i56-B85N-PHOENIX-WIFI:/etc$ sudo more sudoers
>>> /etc/sudoers: syntax error near line 32 <<<
>>> /etc/sudoers: syntax error near line 32 <<<
sudo: parse error in /etc/sudoers near line 32
sudo: no valid sudoers sources found, quitting
sudo: unable to initialize policy plugin
```

这时候需要使用　pkexec visudo 命令来重新修改  
```
i56@i56-B85N-PHOENIX-WIFI:/etc$ pkexec visudo
```
