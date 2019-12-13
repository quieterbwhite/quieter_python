# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from logs.mylog import flogger

from watcher.mapper.mapper_me import MeMapper


class MeService(object):

    @classmethod
    def me_add(cls, me_dict):

        me_obj = MeMapper.me_add(me_dict)
        return me_obj

    @classmethod
    def me_get(cls, me_dict):

        me_obj= MeMapper.me_get(me_dict)
        return me_obj