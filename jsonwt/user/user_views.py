# -*- coding=utf-8 -*-

from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import auth

from user.user_mng import UserManager
from user.user_forms import UserRegForm, UserLoginForm


class UserRegView(View):
    ''' 用户注册 '''

    def get(self, request, *args, **kwargs):

        return render(request, 'user_reg.html')

    def post(self, request, *args, **kwargs):
        form = UserRegForm(request.POST)
        if not form.is_valid():
            # TODO error handle
            print 'form: ', form
            return render(request, 'user_reg.html', {'form':form})

        UserManager.save_user(form.cleaned_data)
        return redirect('/jwt/user/log')


class UserLoginView(View):
    ''' 用户登录 '''

    def get(self, request, *args, **kwargs):

        return render(request, 'user_log.html')


    def post(self, request, *args, **kwargs):
        form = UserLoginForm(request.POST)
        if not form.is_valid():
            # TODO error handle
            print 'form: ', form
            return render(request, 'user_log.html', {'form':form})

    def post(self, request, *args, **kwargs):
        form = UserLoginForm(request.POST)
        if not form.is_valid():
            # TODO error handle
            print 'form: ', form
            return render(request, 'user_log.html', {'form':form})

        user_data = form.cleaned_data
        username = user_data.get('username')
        password = user_data.get('password')

        user = auth.authenticate(username=username, password=password)
        auth.login(request, user)
        request.session.set_expiry(60 * 60 * 1)
        # return redirect(reverse('index'))
        return redirect('index')


class UserIndexView(View):
    ''' 用户 '''

    def get(self, request, *args, **kwargs):

        return render(request, 'user_index.html')



