## 我是如何培养新人的：关于如何制作一个python库？

From: shadow chi [无界社区mixlab](javascript:void(0);) *2019-12-06*

我喜欢提出问题给新人去解决，而不会直接把答案告诉他。最近在工作中完成了一些文本分类的算法，涉及到最后的工程化问题，于是我布置了个作业，要求是把代码整理成python，并发布，方便调用。



下面是新人完成的作业，他写了一个简短的指南，分享给大家。





Python包封装流程：



1.创建项目 项目名任意（例：pure）



2.在项目下新建python包，包名任意（例：pure）



3.在python包里须有__init__文件、实例.py文件

例：我的实例.py文件取名（demo.py）

文件内容如下：



def demo_test():

  print("My package was successful")



4.在项目目录下创建setup.py文件

文件内容如下：



from setuptools import setup, find_packages

setup(

  name='mypure',

  version='1.0',

  packages=find_packages(),

  author='Example Author',

 author_email='',

  keywords='',

  description='A small example package',

  license='',

  url='',

  include_package_data=True,

  install_requires=[],

)



5.在该项目路径下：执行 python setup.py sdist

此时项目中会出现两个新文件夹如下：

6.在pypi官网注册账号：官网：https://pypi.org/



7.执行 pip install twine



8.执行twine upload dist/*上传包



上传包过程中需输入用户名、密码



9.执行pip install 包名安装包



简短的指南，后续再有新人，可以直接传授，😄节省时间。



把复杂的工作拆解成一步步可以解决的问题，这样离目标就近了～