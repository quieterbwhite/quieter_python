#### docker love python

```shell
-- 拉取镜像
docker pull python:3.6.8

-- 创建容器并进入容器命令行
docker run -it --entrypoint bash python:3.6.8

-- 启动容器
docker start 1e8aa

-- 进入容器命令行
docker exec -it 1e8aa /bin/bash

    安装python依赖
    $ pip install thrift
```