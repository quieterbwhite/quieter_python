# DNS

## 浏览器正常访问 github, shell 里面不能访问

```
就是网页访问都是正常的，但是不能拉代码, ping也ping不通

解决方法:
https://askubuntu.com/questions/558141/ubuntu-12-04-cant-resolve-hostname

So by running the command

echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf

we are basically setting the Google's free DNS server (8.8.8.8) as the nameserver.
```
