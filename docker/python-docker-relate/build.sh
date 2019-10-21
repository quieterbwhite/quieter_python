#!/usr/bin/env bash
# 创建项目镜像

docker build -t message-service:latest -f Dockerfile .