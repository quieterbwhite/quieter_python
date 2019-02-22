#### 给已经存在的项目添加git

2017年04月21日 12:17:00 [苇渡lrm](https://me.csdn.net/u013325929) 阅读数：13484

 版权声明：本文为博主原创文章，未经博主允许不得转载。	https://blog.csdn.net/u013325929/article/details/70313414

前提：先去gitlab或github网站上创建一个新项目，完毕后记得添加.ignoe；

1、打开终端，cd到已存在项目的目录

2、输入以下命令行，初始化一个本地仓库：

```
 git init
```

3、输入以下命令，把工程所有文件都添加到该仓库中（千万别忘记后面的.号！！！）：

```
 git add .
```

4、输入以下命令，把文件提交到本地仓库：

```
 git commit -m "Initial commit"

 如果出现nothing to commit, working directory clean说明你已经提交好了。
```

5、输入以下命令，添加远程仓库地址：

```
 输入：git remote add origin + 你的仓库地址

 例如：git remote add origin https://git.oschina.net/hhh/GitDemo.git

 如果出现fatal: remote origin already exists.说明你已经添加过远程仓库了，输入以下命令删除远程仓库：git remote rm origin，然后再次执行第5步。
```

6、输入以下命令，把文件提交到远程仓库：

```
 git push -u origin master
```

然后你就等着它提交完成就完事了。

7、假如第6部失败的话再执行git pull –rebase origin master命令，然后再执行git push -u origin master即可上传成功。

8、完事后假如还是不能拉代码的话再重启项目执行git branch –set-upstream master origin/master即可。