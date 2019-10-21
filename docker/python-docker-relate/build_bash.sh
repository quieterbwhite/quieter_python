#!/usr/bin/env bash
# 创建基础镜像

docker build -t python-base:latest -f Dockerfile.base .