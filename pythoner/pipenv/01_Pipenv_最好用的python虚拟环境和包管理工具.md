# [Pipenv——最好用的python虚拟环境和包管理工具](https://www.cnblogs.com/zingp/p/8525138.html)

> https://www.cnblogs.com/zingp/p/8525138.html

**阅读目录**

- [1 安装pipenv](https://www.cnblogs.com/zingp/p/8525138.html#_label0)
- [2 创建虚拟环境](https://www.cnblogs.com/zingp/p/8525138.html#_label1)
- [3 安装python包（module）](https://www.cnblogs.com/zingp/p/8525138.html#_label2)
- [4 查看安装包及依赖关系](https://www.cnblogs.com/zingp/p/8525138.html#_label3)
- [5 兼容requirements.txt 文件](https://www.cnblogs.com/zingp/p/8525138.html#_label4)
- [6 运行python代码（py文件）](https://www.cnblogs.com/zingp/p/8525138.html#_label5)
- [7 删除python包（module）](https://www.cnblogs.com/zingp/p/8525138.html#_label6)
- [8 删除虚拟环境](https://www.cnblogs.com/zingp/p/8525138.html#_label7)
- [9 常用命令一览](https://www.cnblogs.com/zingp/p/8525138.html#_label8)

pipenv 是[**Kenneth Reitz**](https://www.kennethreitz.org/)大神的作品，能够有效管理Python多个环境，各种包。过去我们一般用virtualenv搭建虚拟环境，管理python版本，但是跨平台的使用不太一致，且有时候处理包之间的依赖总存在问题；过去也常常用 pip进行包的管理，pip已经足够好，但是仍然推荐pipenv，相当于virtualenv和pip的合体，且更加强大。pipenv开源之后，在GitHub上有很高人气（截止于现在有9600多星）。

**pipenv主要有以下特性：**

　　（1）pipenv集成了pip，virtualenv两者的功能，且完善了两者的一些缺陷。

　　（2）过去用virtualenv管理requirements.txt文件可能会有问题，Pipenv使用Pipfile和Pipfile.lock，后者存放将包的依赖关系，查看依赖关系是十分方便。

　　（3）各个地方使用了哈希校验，无论安装还是卸载包都十分安全，且会自动公开安全漏洞。。

　　（4）通过加载.env文件简化开发工作流程。

　　（5）支持Python2 和 Python3，在各个平台的命令都是一样的。

下面快速介绍pipenv的基本使用，文章末尾有其github链接。本文的测试环境是windows下的Python3.6，对于其他平台同样适用。



## 1 安装pipenv

首先请确保安装了python3和对应的pip3，如果你的python和pip对应的是python3.x,忽略数字3。

```
1 pip3 install pipenv
```

如下：

![img](https://images2018.cnblogs.com/blog/986023/201803/986023-20180307194834845-1842057243.png)



## 2 创建虚拟环境

```
1 mkdir project
2 cd project
3 pipenv install
```

如下：

![img](https://images2018.cnblogs.com/blog/986023/201803/986023-20180307194947220-1506286222.png)

初始化好虚拟环境后，会在项目目录下生成2个文件`Pipfile`和`Pipfile.lock`。为pipenv包的配置文件，代替原来的 requirement.txt。

项目提交时，可将`Pipfile` 文件和`Pipfile.lock`文件一并提交，待其他开发克隆下载，根据此Pipfile 运行命令`pipenv install --dev`生成自己的虚拟环境。

`Pipfile.lock` 文件是通过hash算法将包的名称和版本，及依赖关系生成哈希值，可以保证包的完整性。



## 3 安装python包（module）

用pycharm先打开咱们刚刚创建的project，然后创建APP目录，在app目录下创建如下spider.py文件，导入requests库，并没有安装这个包。

![img](https://images2018.cnblogs.com/blog/986023/201803/986023-20180307195400840-133682225.png)

安装requests包，命令如下：

```
1 pipenv install requests
```

详情参见下图：

![img](https://images2018.cnblogs.com/blog/986023/201803/986023-20180307195456749-1053646299.png)

这样，在pycharm里就能看到requests已经可用，并且能抓取到网页了。

![img](https://images2018.cnblogs.com/blog/986023/201803/986023-20180307195530532-1590317241.png)



## 4 查看安装包及依赖关系

命令如下：

```
1 pipenv graph
```

详情参见下图：

![img](https://images2018.cnblogs.com/blog/986023/201803/986023-20180307195620080-521697996.png)

4.1 通过--dev指明只安装在开发环境中

```
1 pipenv install --dev requests --three
```

详情如下图：

![img](https://images2018.cnblogs.com/blog/986023/201803/986023-20180307195741595-1234780798.png)

反应在Pipfile如下：

```
[[source]]

url = "https://pypi.python.org/simple"
verify_ssl = true
name = "pypi"


[packages]

requests = "*"


[dev-packages]

requests = "*"


[requires]

python_version = "3.6"
```

安装包记录是在`[dev-packages]` 部分，或是`[packages]` 部分。

在安装时，指定`--dev`参数，则只安装`[dev-packages]`下的包；若安装时不定指定`--dev`参数，只会安装`[packages]` 包下面的模块。

在构建新的python虚拟环境时，会自动下载安装`[requires]` 下的包。



## 5 兼容requirements.txt 文件

**5.1 pipenv可以像virtualenv一样用命令生成requirements.txt 文件**，命令如下：

```
1 pipenv lock -r --dev > requirements.txt
```

详情如下图：

![img](https://images2018.cnblogs.com/blog/986023/201803/986023-20180307200027248-1095832128.png)

**5.2 pipenv也可以通过requirements.txt安装包**

命令参见：

```
1 pipenv install -r requirements.txt
```

![img](https://images2018.cnblogs.com/blog/986023/201803/986023-20180307200204047-2082092811.png)

这样我们可以重用之前的requirement.txt 文件来构建我们新的开发环境，把我们的项目顺利的迁到pipenv。



## 6 运行python代码（py文件）

**6.1 方法一： pipenv run python xxx.py**

```
1 pipenv run python xxx.py
```

详情如下：

![img](https://images2018.cnblogs.com/blog/986023/201803/986023-20180307200346699-591006324.png)

**6.2 方法二：启动虚拟环境的shell环境**

```
1 pipenv shell
```

详情如下：

![img](https://images2018.cnblogs.com/blog/986023/201803/986023-20180307200522611-1308404339.png)

加上参数也可：

![img](https://images2018.cnblogs.com/blog/986023/201803/986023-20180307200555686-235624378.png)



## 7 删除python包（module）

删除包的命令：

```
pipenv uninstall [module_name]
```

例如卸载之前安装的requests包：

![img](https://images2018.cnblogs.com/blog/986023/201803/986023-20180307200637607-866216967.png)



## 8 删除虚拟环境

```
1 pipenv --rm
```

如下：

![img](https://images2018.cnblogs.com/blog/986023/201803/986023-20180307200738436-186882846.png)

删除虚拟环境之后，再次运行pip shell 会发现先为这个project创建虚拟环境，然后再打开shell。如下：

![img](https://images2018.cnblogs.com/blog/986023/201803/986023-20180307200832440-759998131.png)



## 9 常用命令一览

```
pipenv --where                 列出本地工程路径
pipenv --venv                  列出虚拟环境路径
pipenv --py                    列出虚拟环境的Python可执行文件
pipenv install                 创建虚拟环境
pipenv isntall [moduel]        安装包
pipenv install [moduel] --dev  安装包到开发环境
pipenv uninstall[module]       卸载包
pipenv uninstall --all         卸载所有包
pipenv graph                   查看包依赖
pipenv lock                    生成lockfile
pipenv run python [pyfile]     运行py文件
pipenv --rm                    删除虚拟环境
```


### pipenv 都包含什么？

> https://www.jianshu.com/p/00af447f0005

pipenv 是 Pipfile 主要倡导者、requests 作者 Kenneth Reitz 写的一个命令行工具，主要包含了Pipfile、pip、click、requests和virtualenv。Pipfile和pipenv本来都是Kenneth Reitz的个人项目，后来贡献给了pypa组织。Pipfile是社区拟定的依赖管理文件，用于替代过于简陋的 requirements.txt 文件。

Pipfile的基本理念是：

Pipfile 文件是 TOML 格式而不是 requirements.txt 这样的纯文本。
 一个项目对应一个 Pipfile，支持开发环境与正式环境区分。默认提供 default 和 development 区分。
 提供版本锁支持，存为 Pipfile.lock。
 click是Flask作者 Armin Ronacher 写的命令行库，现在Flask已经集成了它。

接下来，我们看看怎么使用它吧

### 安装

```
$ pip install pipenv
```

### 用法

在使用`pipenv`之前，必须彻底的忘记`pip`这个东西

新建一个准备当环境的文件夹pipenvtest，并cd进入该文件夹：
 `pipenv --three`   会使用当前系统的Python3创建环境

`pipenv --python 3.6` 指定某一Python版本创建环境

`pipenv shell` 激活虚拟环境

`pipenv --where`  显示目录信息
 `/home/jiahuan/pipenvtest`

`pipenv --venv`  显示虚拟环境信息
 `/home/jiahuan/.local/share/virtualenvs/pipenvtest-9KKRH3OW`

`pipenv --py`  显示Python解释器信息
 `/home/jiahuan/.local/share/virtualenvs/pipenvtest-9KKRH3OW/bin/python`

`pipenv install requests` 安装相关模块并加入到Pipfile

`pipenv install django==1.11` 安装固定版本模块并加入到Pipfile

`pipenv graph` 查看目前安装的库及其依赖

```
requests==2.18.4
  - certifi [required: >=2017.4.17, installed: 2017.11.5]
  - chardet [required: <3.1.0,>=3.0.2, installed: 3.0.4]
  - idna [required: >=2.5,<2.7, installed: 2.6]
  - urllib3 [required: >=1.21.1,<1.23, installed: 1.22]
```

`pipenv check`检查安全漏洞

```
Checking PEP 508 requirements…
Passed!
Checking installed package safety…
All good! 
```

`pipenv uninstall --all`  卸载全部包并从Pipfile中移除

```
Found 5 installed package(s), purging…
Uninstalling certifi-2017.11.5:
  Successfully uninstalled certifi-2017.11.5
Uninstalling chardet-3.0.4:
  Successfully uninstalled chardet-3.0.4
Uninstalling idna-2.6:
  Successfully uninstalled idna-2.6
Uninstalling requests-2.18.4:
  Successfully uninstalled requests-2.18.4
Uninstalling urllib3-1.22:
  Successfully uninstalled urllib3-1.22
```

跟上面graph命令显示的内容对应