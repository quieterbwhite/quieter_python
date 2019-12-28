# Pipenv & 虚拟环境¶
> https://pythonguidecn.readthedocs.io/zh/latest/dev/virtualenvs.html  
> https://pipenv.readthedocs.io/en/latest/  
> https://sikaixing.com/2017/06/03/pipenv_intro/  
> https://robots.thoughtbot.com/how-to-manage-your-python-projects-with-pipenv  
> https://python.freelycode.com/contribution/detail/682  
> http://crazygit.wiseturtles.com/2018/01/08/pipenv-tour/  

![pipenv](http://7sbqvw.com1.z0.glb.clouddn.com/github/python/pipenv.jpg)

## 安装 Pipenv
```
确保 python & pip

    $ python --version
    $ pip --version

安装 Pipenv¶

    $ pip install --user pipenv

    --user 选项将 pipenv 安装在系统的用户目录，避免使用 sudo 权限以及破坏系统原有的依赖，在 Linux 和 macOS 中可以使用 python -m site --user-base 查看 pip 用户目录在什么地方：
    
    $ python -m site --user-base
    /home/bwhite/.local
```

## 为您的项目安装包¶
```
    Pipenv 管理每个项目的依赖关系。要安装软件包时，请更改到您的项目目录（或只是本教程中的 一个空目录）并运行：

    $ cd myproject
    $ pipenv --three  # 其中--two表示用Python2建立虚拟环境, 另外还有个--three表示用Python3建立. 
    $ pipenv install requests

    Pipenv 将在您的项目目录中安装超赞的 Requests 库并为您创建一个 Pipfile。 Pipfile 用于跟踪您的项目中需要重新安装的依赖

    # 卸载包

    pipenv uninstall beautifulsoup4
```

## 使用安装好的包¶
```
    $ pipenv run python main.py

    使用 $ pipenv run 可确保您的安装包可用于您的脚本。我们还可以生成一个新的 shell， 确保所有命令都可以使用 $ pipenv shell 访问已安装的包。
```

## 管理你的开发环境
```
    通常有一些Python包只在你的开发环境中需要，而不是在你的生产环境中，例如单元测试包。 Pipenv将使用--dev标志保持两个环境分开。 例如，

    pipenv install --dev nose2

    将安装nose2，但也将其关联为只在你的开发环境中需要的软件包。 这很有用，因为现在，如果你要在你的生产环境中安装你的项目，

    pipenv install

    默认情况下不会安装nose2包。 但是，如果另一个开发人员将你的项目克隆到自己的开发环境中，他们可以使用--dev标志，

    pipenv install --dev

    并安装所有依赖项，包括开发包。
```

## 运行你的代码
```
    为了激活与你的Python项目相关联的虚拟环境，你可以简单使用shell命令，比如，

    pipenv run which python

    将在您的虚拟环境中运行which python命令，并显示与您的虚拟环境相关联的python可执行文件所在的路径。 这个功能是在虚拟环境中运行你自己的Python代码的一个整洁的方法，

    pipenv run python my_project.py

    如果你不想每次运行Python时都输入这么多，你可以在shell中设置一个别名，例如，

    alias prp="pipenv run python"
```



