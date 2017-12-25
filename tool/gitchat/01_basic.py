# -*- coding=utf-8 -*-
# Created Time: 2017年03月21日 星期二 09时13分47秒
# File Name: 01_basic.py

"""
** Git global setup

git config --global user.name "libo"
git config --global user.email "libo@idealsee.cn"


** Create a new repository

mkdir stitch
cd stitch
git init
touch README.md
git add README.md
git commit -m "first commit"
git remote add origin ssh://git@10.0.1.55:10022/360camera/stitch.git
git push -u origin master


** Push an existing Git repository

cd existing_git_repo
git remote add origin ssh://git@10.0.1.55:10022/360camera/stitch.git
git push -u origin master

"""
