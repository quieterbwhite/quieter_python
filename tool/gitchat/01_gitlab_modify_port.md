# [centos 6.8下部署gitlab服务器并修改默认端口](https://segmentfault.com/a/1190000011266124)

## 前言（场景）

github虽好，不过因为访问速度偶尔抽风
如果用来学习git和测试一些git命令可能有点浪费了，这里我们自己架设一个gitlab来学习一些不常规的git命令等
github私有仓库需要费用，gitlab自己架设不仅适合内部开发，还可以有很多好处

## 安装gitlab

### 安装依赖环境

```
yum install -y curl openssh-server openssh-clients cronie lokkit

lokkit -s http -s ssh
或
iptables -A INPUT -p tcp --dport 8090 -j ACCEPT
iptables -A INPUT -p tcp --dport 22 -j ACCEPT
service iptables save
```

### 安装postfix

```
yum install postfix
service postfix start
chkconfig postfix on
```

### 添加Gitlab包仓库

```
curl -sS https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.rpm.sh | sudo bash
```

### 安装Gitlab

```
yum install -y gitlab-ce
```

### 配置Gitlab和启动

```
gitlab-ctl reconfigure
gitlab-ctl start
```

### 访问gitlab

```
http://ip/
#默认是root和root密码即可登录
```

## 修改默认的gitlab 相关端口

### 修改/etc/gitlab/gitlab.rb

```
vim /etc/gitlab/gitlab.rb

#unicorn['port'] = 8080 修改 8070  默认是注释的去掉前面的#
unicorn['port'] = 8070
#nginx['listen_port'] = nil 修改 8090  默认是注释的去掉前面的#
nginx['listen_port'] = 8090
```

### 修改/var/opt/gitlab/gitlab-rails/etc/unicorn.rb

```
vim /var/opt/gitlab/gitlab-rails/etc/unicorn.rb

#listen "127.0.0.1:8080", :tcp_nopush => true
listen "127.0.0.1:8070", :tcp_nopush => true
```

### 修改默认的gitlab nginx的web服务80端 /var/opt/gitlab/nginx/conf/gitlab-http.conf

```
vim /var/opt/gitlab/nginx/conf/gitlab-http.conf

#listen *:80;
listen *:8090;
```

### 重新配置gitlab

```
gitlab-ctl reconfigure
```

### 重新启动gitlab

```
gitlab-ctl restart
```

### 配置smtp邮件发送

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