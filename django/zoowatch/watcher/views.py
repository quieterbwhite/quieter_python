# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.http import JsonResponse
from django.views.generic import View

from container.service import data_dict

from container.service import data_list

from logs.mylog import flogger

import json


class WatchTestView(View):
    """  """

    def get(self, request, *args, **kwargs):

        res = {'err_code':0}

        flogger.info(data_list)

        res.update({"data":data_list})

        return JsonResponse(res)