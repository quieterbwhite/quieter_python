# -*- coding=utf-8 -*-
# Created Time: Sun 26 Feb 2017 10:56:33 PM CST
# File Name: check_task.py


from app import app

import subprocess


def check_task():

    with app.app_context():

        print "running a task..."
