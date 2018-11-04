#!/bin/bash
cur_dir=`pwd`
docker stop micro-mysql
docker rm micro-mysql
docker run --name micro-mysql -v ${cur_dir}/conf:/etc/mysql/conf.d -v ${cur_dir}/data:/var/lib/mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=olivia -d mysql:latest
