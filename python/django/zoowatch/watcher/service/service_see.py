# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from logs.mylog import flogger

from watcher.mapper.mapper_see import SeeMapper


class SeeService(object):

    @classmethod
    def see_add(cls, see_dict):

        see_obj = SeeMapper.see_add(see_dict)
        return see_obj

    @classmethod
    def see_get(cls, see_dict):

        see_obj= SeeMapper.see_get(see_dict)
        return see_obj