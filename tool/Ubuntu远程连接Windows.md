# Ubuntu 远程连接 Windows

使用工具 **rdesktop**

```
$ sudo apt install rdesktop

$ sudo rdesktop -f -u Administrator -p password 47.52.132.255 -g 1024*768 -r disk:mydisk=/home/bwhite/tmp -r clipboard:PRIMARYCLIPBOARD
```



