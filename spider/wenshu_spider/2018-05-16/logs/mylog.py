# -*- coding=utf-8 -*-
# Created Time: 2016年01月16日 星期六 16时24分02秒
# File Name: mylog.py

import os
import logging.config

log_dir = os.path.abspath(os.path.dirname(__file__))

logging.config.fileConfig(log_dir + "/logger.conf")

flogger = logging.getLogger('flogger')