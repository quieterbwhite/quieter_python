Git
1. SSH 公钥认证
2. 在使用Git初始化版本库的时候，使用”git init”命令和使用”git init –bare”命令有什么区别呢？
3. .gitignore 文件详解

1. SSH 公钥认证
关于公钥认证的原理，维基百科上的这个条目是一个很好的起点： http://en.wikipedia.org/wiki/Public-key_cryptography 。
如果你的主目录下不存在 .ssh 目录，说明你的 SSH 公钥/私钥对尚未创建。可以用这个命令创建：
$ ssh-keygen
该命令会在用户主目录下创建 .ssh 目录，并在其中创建两个文件：
id_rsa
私钥文件。是基于 RSA 算法创建。该私钥文件要妥善保管，不要泄漏。
id_rsa.pub
公钥文件。和 id_rsa 文件是一对儿，该文件作为公钥文件，可以公开。
创建了自己的公钥/私钥对后，就可以使用下面的命令，实现无口令登录远程服务器，即用公钥认证取代口令认证。
$ ssh-copy-id -i .ssh/id_rsa.pub user@server
说明:
该命令会提示输入用户 user 在 server 上的SSH登录口令。当此命令执行成功后，再以 user 用户登录 server 远程主机时，不必输入口令直接登录。该命令实际上将 .ssh/id_rsa.pub 公钥文件追加到远程主机 server 的 user 主目录下的 .ssh/authorized_keys 文件中。
检查公钥认证是否生效，运行SSH到远程主机，正常的话应该直接登录成功。如果要求输入口令则表明公钥认证配置存在问题。如果SSH服务存在问题，可以通过查看服务器端的 /var/log/auth.log 进行诊断。

2. 在使用Git初始化版本库的时候，使用”git init”命令和使用”git init –bare”命令有什么区别呢？
>>>> 用”git init”初始化的版本库（暂且称之为working repository）将会生成2类文件：“.git“版本库目录(记录版本历史)和实际项目文件的拷贝。你可以把这类版本库叫做“工作目录”。工作目录是一个包含有版本历史目录“.git”和源文件的目录。你可以在工作目录修改你的源文件并使用”git add”和”git commit”命令进行版本管理。
>>>> 用“git init –bare”初始化的版本库（暂且称之为bare repository）仅包含”.git”目录（记录版本历史），不含项目源文件拷贝。如果你进入版本目录，你会发现仅有”.git”目录，没有其他文件。版本库仅包含记录着版本历史的文件。
>>>> 总结：“工作目录”是通过使用“git init“或“git clone”创建的本地项目拷贝。我们可以在工作目录下面修改和测试代码。通过测试后我们可以使用“git add“和”git commit“命令本地提交修改，然后使用“git push”命令向远程 bare repository库提交更新，通常bare repository指定其他服务器，其他开发者将可以及时看到你的更新。当我们想去更新本地工作目录的时候，我们可以使用“git pull”命令去接受其他开发者提交的更新。

3. .gitignore 文件详解
在代码目录下建立.gitignore文件：vim .gitignore ,内容如下：
#过滤数据库文件、sln解决方案文件、配置文件
*.mdb
*.ldb
*.sln
*.config
#过滤文件夹Debug,Release,obj
Debug/
Release/
obj/
*. Linux 用户可以使用 ‘cache’ 认证助手包来缓存认证信息，运行下面的命令来启用凭据缓存，启用后每次输入密码将保存一小时（3600秒）：
git config --global credential.helper 'cache --timeout 3600'
*.
git config --global user.name "bwhite"
git config --global user.email 707295770@qq.com



