# -*- coding=utf-8 -*-
# Created Time: 2016年01月28日 星期四 23时45分00秒
# File Name: 08_settings_tricks.py

'''
配置文件方面 技巧
'''

'''
不要将项目名称包含在引用代码里

不要硬编码MEDIA_ROOT和TEMPLATE_DIRS

不要将静态文件的路径硬编码在模板中

不要将业务逻辑代码写到视图里

部署时别忘记将DEBUG设置成False
 
'''

'''
** 不要将项目名称包含在引用代码里
 
比如你创建了一个名为"project"的项目，包含一个名为"app"的应用，那么如下代码是不好的：

    from project.app.models import Author

缺点在于：应用和项目变成了紧耦合，无法将应用轻易变得可重用。如果将来要换一个项目名称，那你可有得受了。
推荐的做法是：

    from app.models import Author  


** 不要硬编码MEDIA_ROOT和TEMPLATE_DIRS

项目配置文件settings.py中不要使用如下代码：

    TEMPLATE_DIRS = ( "/home/html/project/templates",)  
    MEDIA_ROOT = "/home/html/project/appmedia/"  

当你在部署到生产环境，或者迁移服务器的时候，就会发生问题。
推荐使用如下方式： 

    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))  
    MEDIA_ROOT = os.path.join(SITE_ROOT, 'appmedia')  
    TEMPLATE_DIRS = ( os.path.join(SITE_ROOT, 'templates'),)  

** 不要将静态文件的路径硬编码在模板中

模板中链接CSS，javascript或图片的时候，不建议使用如下方式：

    <link rel="stylesheet" type="text/css" href="/appmedia/amazing.css" />  
    <script type="text/javascript" src="/appmedia/jquery.min.js"></script>  

当你的项目需要将静态文件用其他服务器提供的时候，通常会是另外一个http地址，那么你就得把所有的/appmedia/替换成新的地址，做网站写代码已经够乏味的了。
没有后顾之忧的解决方法是使用{{ MEDIA_URL }}代替硬编码的路径：

    <link rel="stylesheet" type="text/css" href="{{ MEDIA_URL }}amazing.css" />  
    <script type="text/javascript" src="{{ MEDIA_URL }}jquery.min.js"></script>  

模板上下文变量怎么获取到呢？请使用RequestContext即可：

    return render_to_response("app/template.html", {'var': 'foo'},  
    context_instance=RequestContext(request))  


** 不要将业务逻辑代码写到视图里

不要迷惑，虽然你可能看过很多书和例子，它们把逻辑都写在了views.py里，但请你别这么做。因为这样不利于单元测试，不利于重用代码。
 
那我的业务逻辑应该放哪里呢？推荐放到模型里或者单独建立一个辅助（helper）模块。
 
当然，从模型得到一个Author，获取Author列表的代码是可以放到视图里面的。


** 部署时别忘记将DEBUG设置成False
 
我们常常忘记在部署时禁用DEBUG，有很多种方法自动来处理这个配置：

import socket  
hostname = socket.gethostname()
print 'hostname ', hostname
  
# SECURITY WARNING: don't run with debug turned on in production!
if socket.gethostname() == 'x':  
    DEBUG = True
    ALLOWED_HOSTS = []
else:  
    DEBUG = False
    ALLOWED_HOSTS = ['xiyi.api.wedor.cn', 'wedor.cn']
print 'DEBUG: ', DEBUG 


另一种途径是使用不同的配置文件：

#文件名：settings_debuy.py  
#包含调试模式的配置信息  
#使用python manage.py runserver settings=settings_debug.py来运行项目  
  
from settings import *  
  
DEBUG = True  
  
#还可以配置更多在调试时使用的变量：）  




'''
