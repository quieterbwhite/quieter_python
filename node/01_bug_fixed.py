# -*- coding=utf-8 -*-
# Created Time: 2017年09月28日 星期四 01时14分06秒
# File Name: 01_bug_fixed.py

"""
On Ubuntu 16: /usr/bin/env: ‘node’: No such file or directory

第一行的!/usr/bin/env node这里到node是找不到的

Fixed by:

    ln -s /usr/bin/nodejs /usr/bin/node

    in my situation:

        sudo ln -s /home/bwhite/software/node-v8.1.3-linux-x64/bin/node /usr/bin/node


"""
