#### Leaf ID生成器

##### 本机部署
```
准备: java环境

1. 下载源码

    git clone git@github.com:Meituan-Dianping/Leaf.git

2. 测试打包运行

    $ cd Leaf
    $ mvn clean install -DskipTests
    $ cd leaf-server
    $ mvn spring-boot:run

    curl http://localhost:8080/api/snowflake/get/test

3. supervisor管理服务

supervisor配置文件:

[program:leaf]

user=bwhite                                        ; User to run as
directory=/home/bwhite/mygit/Leaf/leaf-server
command=/home/bwhite/software/apache-maven-3.5.2/bin/mvn spring-boot:run              ; Command to start app


stdout_logfile=/tmp/leaf_out.log            ; Where to write log messages
stdout_logfile_maxbytes=50MB
stdout_logfile_backups=5

stderr_logfile=/tmp/leaf_err.log
stderr_logfile_maxbytes=50MB
stderr_logfile_backups=5

autostart=true
autorestart=true
#redirect_stderr = true                            ; Save stderr in the same log

#stdout_events_enabled=false

loglevel=info

environment=LANG=en_US.UTF-8,LC_ALL=en_US.UTF-8    ; Set UTF-8 as default encoding    

4. 测试服务

    $ sudo supervisorctl update
    $ sudo supervisorctl status
```

##### Docker部署
```
pass
```
