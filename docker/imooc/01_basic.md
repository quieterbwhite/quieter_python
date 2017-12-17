# docker @ imooc

## install docker
```
sudo wget -qO- https://get.docker.com/ | sh

    命令解释:
        -q, 减少输出
        O-, 将wget的output redirect to std output, rather file
        
        we download a shell script, and send it to sh to execute

sudo usermod -aG docker imooc

test:
    $docker info
```

## command
```
docker pull, get image
docker build, create image
docker images, list image
docker run, run container
docker ps, list container
docker rm
docker rmi
docker cp
docker commit
```

## run
```
* check container status

    docker ps -a

* copy local file to docker container

    docker cp index.html container_id://usr/share/nginx/html

* stop container

    docker stop container_id

* save container

    docker commit -m 'fun' container_id new_name

    will create a new image, that's the point

* delete a image

    docker rmi image_id

    docker rm container_id
```

## Dockerfile
```
* first Dockerfile

    FROM alpine:latest
    MAINTAINER libo
    CMD echo 'hello docker'

    then:

    docker build -t hello_docker .

        -t, like a tag name

        . , path, send file in ./ to docker to build a image

    check:

    docker images
```

```
* second Dockerfile

    FROM ubuntu
    MAINTAINER libo
    RUN sed -i 's/archive.ubuntu.com/mirrors.ustc.edu.cn/g' /etc/apt/sources.list
    RUN apt-get update
    RUN apt-get install -y nginx
    COPY index.html /var/www/html
    ENTRYPOINT ["/usr/sbin/nginx", "-g", "daemon off;"] # run nginx frontend
    EXPOSE 80

    docker build -t libo/hello-nginx .

    docker run -d -p 80:80 libo/hello-nginx
```






