#### docker 安装 rabbitmq



```shell
docker run -d --name rabbit -p 5672:5672 -p 15672:15672 -e RABBITMQ_DEFAULT_USER=bwhite -e RABBITMQ_DEFAULT_PASS=olivia rabbitmq:3.7.3-management
```

