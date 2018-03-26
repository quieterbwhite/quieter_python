# -*- coding=utf-8 -*-
# Created Time: 2015年10月14日 星期三 23时11分02秒
# File Name: 01_create_project.py

'''
记录创建一个项目的完整步骤
'''

'''
1. 创建项目环境

  * virtualenv .
  * source bin/activate
  * pip install django==1.8.3
  * pip install psycopg2

2. 创建项目

  * django-admin startproject mysite
  * 修改 settings.py 配置文件为想要的样子, 像，数据库，时区，日志，中间件等

3. 项目内容相关

  * 创建django需要的数据库环境 python manage.py migrate
  * 尝试第一次运行django       python manage.py runserver 0.0.0.0:8001

  * 创建app                    python manage.py startapp polls
  * 关于创建app, 有一个很重要的法则！-> 任何时候不能有相同的app 名，不同项目也不行
  * 解决方案就是加上项目前缀应该就能解决绝大部分问题了
  * 创建model                  ...
  * 将 polls 添加到　INSTALLED_APPS

  * 创建数据库语句到文件       python manage.py makemigrations polls
  * 查看文件中生成的将要执行的sql语句 python manage.py sqlmigrate polls 0001
  * 创建表到数据库             python manage.py migrate

  * 进入django 的 shell 环境   python manage.py shell

  * 收集静态文件，供admin使用  python manage.py collectstatic
'''
