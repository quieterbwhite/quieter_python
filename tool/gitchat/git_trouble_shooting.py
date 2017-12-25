# -*- coding=utf-8 -*-
# Created Time: 2015年10月13日 星期二 14时13分56秒
# File Name: git_trouble_shooting.py

'''
git 相关问题解决
'''

1. git insufficient permission for adding an object to repository database ./objects
2. 撤销操作


1. git insufficient permission for adding an object to repository database ./objects
this is a shared group repository
so i had to enter the repository dir and make sure group can write into it

ssh to server
cd repository.git

sudo chmod -R g+ws *
sudo chgrp -R mygroup *

git repo-config core.sharedRepository true

and the try to push origin master again

2. 撤销操作
git reset --hard <commit_id>
git revert <commit_id>




