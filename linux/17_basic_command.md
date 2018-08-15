#### Basic Command



## 用户

添加用户：

```
sudo adduser username
```

添加用户并设置目录：

```
sudo adduser username --home /home/username
```

将用户设置超级用户组（如添加到 sudo 用户组）：

```
sudo usermod -aG sudo username
```



根据名称强制杀死进程：

```
ps -ef | grep python | cut -c 9-15 | xargs kill -9
```

查看当前目录文件及文件夹大小：

```
du -sh *
```

查看各分区使用情况：

```
df -h
```

查看内存及用量（G为单位）：

```
free -g
```

