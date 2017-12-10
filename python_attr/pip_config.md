# Python Pip

## 1. 安装 pip

```
sudo apt-get install build-essential python-dev python3-dev python-pip python3-pip
```

## 2. 修改 pip 源

```
根目录新建或修改 pip 配置文件

$ touch ~/.pip/pip.conf

输入如下内容即可:

 [global]
 trusted-host = mirrors.aliyun.com
 index-url = http://mirrors.aliyun.com/pypi/simple/
 format = columns
```

## 2. 固化依赖包

```
1. 将项目用到的包都下载到指定目录

    pip install --download /tmp/pip -r requirements_online

2. 修改 requirements_local 指向包所在的目录, 如:

    /tmp/pip/Django-1.11-py2.py3-none-any.whl
    /tmp/pip/pytz-2017.3-py2.py3-none-any.whl

3. 通过本地包安装

    pip install -r requirements_local
```
