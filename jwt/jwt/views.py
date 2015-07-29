# -*- coding=utf-8 -*-

from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.shortcuts import render, redirect

from models import JWTUser, Data

class TestView(View):

    def get(self, request, *args, **kwargs):

        res = {'name':'tiger'}
        return JsonResponse(res)

class TestDBView(View):

    def get(self, request, *args, **kwargs):

        Data(
            name='tiger',
            age=18
        ).save()

        res = {'name':'bwhite'}
        return JsonResponse(res)

