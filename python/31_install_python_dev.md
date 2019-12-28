#### install python dev on different os
> https://stackoverflow.com/questions/21530577/fatal-error-python-h-no-such-file-or-directory
> https://www.jianshu.com/p/e6945ac9c4c8

For apt (Ubuntu, Debian...):

sudo apt-get install python-dev   # for python2.x installs
sudo apt-get install python3-dev  # for python3.x installs
For yum (CentOS, RHEL...):

sudo yum install python-devel   # for python2.x installs
sudo yum install python3-devel   # for python3.x installs

---

#### CentOS 7安装pip3
```
首先要确保在CentOS 7上已经安装了EPEL仓库。如果没有安装，执行以下命令安装：

yum install -y epel-release
安装后，安装pip3

$sudo yum install python34-pip
$pip3.4 install foo
```
