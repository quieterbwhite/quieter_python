# -*- coding=utf-8 -*-
# Created Time: 2017年09月19日 星期二 16时23分41秒
# File Name: 01_basic.py

"""

创建项目

    安装django
    pip install django

    创建项目
    django-admin startproject dream
    cd dream

    创建应用
    python manage.py startapp tiger

    注册应用
    add app info to INSTALL_APPS

    添加模型信息
    add model info

    生成迁移命令
    python manage.py makemigrations

    迁移
    python manage.py migrate

    开发服务器运行项目
    python manage.py runserver 0.0.0.0:8000

使用django的管理

    创建一个管理员用户
    python manage.py createsuperuser，按提示输入用户名、邮箱、密码

    启动服务器，通过“127.0.0.1:8000/admin”访问，输入上面创建的用户名、密码完成登录
    进入管理站点，默认可以对groups、users进行管理

管理界面本地化

    编辑settings.py文件，设置编码、时区
    LANGUAGE_CODE = 'zh-Hans'
    TIME_ZONE = 'Asia/Shanghai'

向admin注册booktest的模型

    打开booktest/admin.py文件，注册模型
    from django.contrib import admin
    from models import BookInfo
    admin.site.register(BookInfo)

    刷新管理页面，可以对BookInfo的数据进行增删改查操作
    问题：如果在str方法中返回中文，在修改和添加时会报ascii的错误
    解决：在str()方法中，将字符串末尾添加“.encode('utf-8')”


"""
