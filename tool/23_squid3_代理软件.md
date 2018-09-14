#### Install squid

> https://www.digitalocean.com/community/tutorials/how-to-install-squid-proxy-on-ubuntu-12-10-x64
>
> https://www.linode.com/docs/web-servers/squid/squid-http-proxy-ubuntu-12-04/

```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install squid

sudo cp /etc/squid3/squid.conf /etc/squid3/squid.conf.default
```

##### 修改端口
```
cd /etc/squid3

http_port 3128
```

##### 配置允许所有连接:
```shell
You need to edit the squid config file to enable access. The default location for the squid file on ubuntu is : /etc/squid3/squid.conf

The following lines enable access to all requests:

# allow all requests    
acl all src 0.0.0.0/0
http_access allow all

# Make sure your custom config is before the "deny all" line
http_access deny all
Note: Make sure you insert this before the final deny block in the squid config file:

If you'd like to debug your requests , use the following line in your config file:

debug_options ALL,1 33,2 28,9
This enables extensive logging for every request. The logs can be found in /var/log/squid3/cache.log
```

