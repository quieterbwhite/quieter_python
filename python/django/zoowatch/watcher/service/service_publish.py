# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from logs.mylog import flogger

from django.db import transaction

from watcher.service.service_see import SeeService
from watcher.service.service_me import MeService


class PublishService(object):

    @classmethod
    def publish(cls, see_dict, me_dict):

        # a = 10/0

        with transaction.atomic():

            see_obj = SeeService.see_add(see_dict)

            # a  = 10/0

            me_obj = MeService.me_add(me_dict)

        return
