# Gitlab

## Install gitlab:
```
    first of all, it's very easy...

    follow the lead

        https://about.gitlab.com/installation/#ubuntu

    no mail service yet :(
```

## 修改gitlab访问端口
> https://segmentfault.com/a/1190000011266124  
```
修改默认的gitlab 相关端口

修改/etc/gitlab/gitlab.rb

    vim /etc/gitlab/gitlab.rb

        #unicorn['port'] = 8080 修改 8070  默认是注释的去掉前面的#
        unicorn['port'] = 8070
        #nginx['listen_port'] = nil 修改 8090  默认是注释的去掉前面的#
        nginx['listen_port'] = 8090

修改/var/opt/gitlab/gitlab-rails/etc/unicorn.rb

    vim /var/opt/gitlab/gitlab-rails/etc/unicorn.rb

        #listen "127.0.0.1:8080", :tcp_nopush => true
        listen "127.0.0.1:8070", :tcp_nopush => true

修改默认的gitlab nginx的web服务80端 /var/opt/gitlab/nginx/conf/gitlab-http.conf

    vim /var/opt/gitlab/nginx/conf/gitlab-http.conf

        #listen *:80;
        listen *:8090;

重新配置gitlab

    gitlab-ctl reconfigure

重新启动gitlab

    gitlab-ctl restart
```

## 修改gitlab生成的项目的地址host
```

## 配置邮件发送
```
$ sudo vi /etc/gitlab/gitlab.rb                            
# Change the external_url to the address your users will type in their browser
external_url 'http://xxhost.com'

#Sending application email via SMTP
gitlab_rails['smtp_enable'] = true
gitlab_rails['smtp_address'] = "smtp.163.com"
gitlab_rails['smtp_port'] = 25 
gitlab_rails['smtp_user_name'] = "xxuser@163.com"
gitlab_rails['smtp_password'] = "xxpassword"
gitlab_rails['smtp_domain'] = "163.com"
gitlab_rails['smtp_authentication'] = :login
gitlab_rails['smtp_enable_starttls_auto'] = true

##修改gitlab配置的发信人
gitlab_rails['gitlab_email_from'] = "xxuser@163.com"
user["git_user_email"] = "xxuser@163.com"
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
