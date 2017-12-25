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

遇到的问题是:
    一开始已经安装好了，可以正常使用
    后来公司搬家了，gitlab对应的ip地址变了，但是新建的项目使用的地址还是旧的
    就需要修改

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

## Command line instructions

Git global setup
```
    git config --global user.name "libo"
    git config --global user.email "b__white@163.com"
```

Create a new repository
```
    git clone git@192.168.8.197:libo/debt.git
    cd debt
    touch README.md
    git add README.md
    git commit -m "add README"
    git push -u origin master
```

Existing folder
```
    cd existing_folder
    git init
    git remote add origin git@192.168.8.197:libo/debt.git
    git add .
    git commit -m "Initial commit"
    git push -u origin master
```

Existing Git repository
```
    cd existing_repo
    git remote rename origin old-origin
    git remote add origin git@192.168.8.197:libo/debt.git
    git push -u origin --all
    git push -u origin --tags
```
