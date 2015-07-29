# -*- coding=utf-8 -*-

from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.shortcuts import render, redirect

from user_mng import UserManager
from user_forms import UserRegForm


class UserRegView(View):
    ''' 用户注册 '''

    def get(self, request, *args, **kwargs):

        return render(request, 'user_reg.html')

    def post(self, request, *args, **kwargs):
        form = UserRegForm(request.POST)
        if not form.is_valid():
            # TODO error handle
            return render(request, 'user_reg.html', {'form':form})

        activate_code = UserManager.save_user(form.cleaned_data)
        return redirect(reverse('login'))


class UserLoginView(View):
    ''' 用户登录 '''

    def get(self, request, *args, **kwargs):

        return render(request, 'user_log.html')




