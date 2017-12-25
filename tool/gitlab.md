# Gitlab

## Install gitlab:
```
    first of all, it's very easy...

    follow the lead

        https://about.gitlab.com/installation/#ubuntu

    no mail service yet :(
```

## 修改gitlab生成的项目的地址host
```
https://blog.haohtml.com/archives/16940

这时我们只需要修改一个配置文件即可。

我安装的时候全部使用的默认配置，路径为 /var/opt/gitlab/gitlab-rails/etc/，配置文件为 gitlab.yml

相关配置

    host: localhost
    port: 80
    https: false

修改host值为你想使用的外网域名或服务器IP地址即可，保存退出。

重启服务:

    gitlab-ctl restart
```
