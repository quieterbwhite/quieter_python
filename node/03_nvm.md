#### nvm

##### install nvm
```shell

https://github.com/nvm-sh/nvm

1. 执行页面上最新的curl脚本

    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.1/install.sh | bash

2. 第一步执行完成过后最后会有三行命令

    export NVM_DIR="$HOME/.nvm"
    [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
    [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

    拷贝下来执行

3. 检查是否安装成功

    nvm -v

4. 安装需要版本的node

    nvm install v6.0.0
```
