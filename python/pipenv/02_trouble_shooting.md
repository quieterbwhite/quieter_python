#### 各种问题解决

##### 1. pipenv & python3 版本冲突问题
```
https://github.com/pypa/pipenv/issues/2924
```

##### 2. piepnv install 报错
```
TypeError: 'module' object is not callable

$ pipenv run pip install pip==18.0
```

##### Error after upgrading pip: cannot import name 'main'
```shell

https://stackoverflow.com/questions/49836676/error-after-upgrading-pip-cannot-import-name-main

https://blog.csdn.net/xxlovesht/article/details/89385194

You can resolve this issue by reinstalling pip.

Use one of the following command line commands to reinstall pip:

Python2:

    python -m pip uninstall pip && sudo apt install python-pip --reinstall

Python3:

    python3 -m pip uninstall pip && sudo apt install python3-pip --reinstall
```
