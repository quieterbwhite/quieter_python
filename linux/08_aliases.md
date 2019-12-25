### alias 命令补充说明：

> [https://commandnotfound.cn/linux/1/97/alias-%2525E5%252591%2525BD%2525E4%2525BB%2525A4](https://commandnotfound.cn/linux/1/97/alias-%25E5%2591%25BD%25E4%25BB%25A4)

------

alias 命令用来设置指令的别名。我们可以使用该命令可以将一些较长的命令进行简化。使用alias时，用户必须使用单引号 '' 将原来的命令引起来，防止特殊字符导致错误。

alias 命令的作用只局限于该次登入的操作。若要每次登入都能够使用这些命令别名，则可将相应的 alias 命令存放到bash的初始化文件 `/etc/bashrc` 中。

### alias 命令语法：

------

```
alias(选项)(参数)
```

### alias 命令选项：

------

```
-p：打印已经设置的命令别名。
```

### alias 命令参数：

------

**命令别名设置**：定义命令别名，格式为“命令别名=‘实际命令’”。

### alias 命令实例：

------

alias 的基本使用方法为：

```
alias 新的命令='原命令 -选项/参数' #将重新定义ls命令，现在只需输入l就可以列目录了。#直接输入 alias 命令会列出当前系统中所有已经定义的命令别名。alias l='ls -lsh' #要删除一个别名，可以使用 unalias 命令： unalias l
```

查看系统已经设置的别名：

```
[root@Dev_Test ~]$aliasalias cp='cp -i'alias l.='ls -d .* --color=auto'alias ll='ls -l --color=auto'alias ls='ls --color=auto'alias mv='mv -i'alias rm='rm -i'alias vi='vim'alias which='alias | /usr/bin/which --tty-only --read-alias --show-dot --show-tilde'
```

### alias 命令总结：

------

alias 这个命令是 shell 的内建命令，可以根据自己的使用习惯设置一些别名，需要注意的就是和其他命令冲突的情况。

**一、 范例演示**

在使用和维护 Linux 系统过程中，我们常常希望根据自己的需要来定义一些命令，那么这样的操作是不是很难呢？其实不是，系统已经为我们设置好了相关的命令，下面小编就以 CentOS6.4 系统为例，为大家演示如何创建自己的命令。

**二、 自定义命令简介**

CentOS 系统下的创建自定义命令其实比较简单，使用的命令就是 `alias`，具体使用的方法就是 alias 自定义命令名='命令'。但是需要注意的是，在自定义之前需要查看自定义的命令名是否是系统已经使用的命令名，否则会冲突，另外一个就是定期清理不需要的自定义命令名。

**三、 演示举例**

假定系统操作员希望进行如下操作：

1. 进入目录/root
2. 查看目录下文件
3. 切换回根目录 通常这需要3条命令 `cd /root;ls;cd /`

如果需要经常使用那么我们可以通过自定义命令的方式用一条命令完成全部操作。



**四、 操作过程**

```
#首先使用命令 type 自定义命令名 ，查看自定义命令名是否被系统占用。[root@Dev_Test ~]$type testtest is a shell builtin #从图中可以看出test命令名已被系统占用，所以不能使用，而 loo 这个命令名经查询可以使用。[root@Dev_Test ~]$type loo-bash: type: loo: not found
#使用命令 alias 创建自定义命令：alias loo='cd /root;ls;cd /' #需要注意的是命令的使用格式，分号与分号之间是没有空格的。#测试一下自定义命令，当输入命令 loo 时，#发现系统依次完成了 cd /root、ls、cd / 三条命令，说明设置成功。#同时也可直接使用命令 alias  查询系统中是否添加了loo这个自定义命令。
#如果希望删除这个自定义命令，可以使用命令 unalias 自定义命令名 来完成。#执行之后发现，loo 命令已不存在，同时自定义命令库中也没有loo命令。
```

### alias 命令的坑：

------

直接在 shell 里设定的命令别名，在终端关闭或者系统重新启动后都会失效，如何才能永久有效呢？

命令别名永久生效

办法就是将别名的设置加入 `~/.bashrc` 文件，然后重新载入下文件就可以了。

```
$ vim ~/.bashrc #在文件最后面加入别名设置，如： alias rm='rm -i' #保存后重新载入：$ source ~/.bashrc
```

这样就可以永久保存命令的别名了。因为修改的是当前用户目录下的 `.bashrc` 文件，所以这样的方式只对当前用户有用。**如果要对所有用户都有效**，修改 `/etc` 目录下的 `bashrc` 文件就可以了。在 **CentOS 7** 下，这个文件是 `/etc/bash.bashrc`。此外在 **CentOS 7** 下，细看 `~/.bashrc` 文件，会发有这样一段代码：

```
if [ -f ~/.bash_aliases ]; then    . ~/.bash_aliasesfi
```

这个代码的意思就是加载 `.bash_aliases` 文件，**CentOS 7** 已经帮我们考虑好了，所以也可以在用户根目录下新建一个文件 `.bash_aliases` 存放命令别名设置。