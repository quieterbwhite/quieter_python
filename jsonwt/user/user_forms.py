# -*- coding=utf-8 -*-

from django import forms
from django.contrib import auth
from user.user_mng import UserManager


class UserRegForm(forms.Form):
    ''' 用户注册验证表单 '''

    username = forms.CharField(
                                min_length=5,
                                max_length=20,
                                required=True
                            )
    password = forms.CharField(
                                min_length=5,
                                max_length=20,
                                required=True
                            )
    mobile = forms.CharField(
                                min_length=5,
                                max_length=20,
                                required=True
                            )
    email = forms.EmailField(
                                min_length=5,
                                max_length=20
                            )

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile', '')
        if UserManager.find_user(mobile=mobile):
            # TODO return error code or instruction ?
            raise forms.ValidationError('mobile exists')
        return mobile

    def clean_username(self):
        username = self.cleaned_data.get('username', '')
        if UserManager.find_user(username=username):
            # TODO return error code or instruction ?
            raise forms.ValidationError('username exists')
        return username

    def clean(self):
        cleaned_data = super(UserRegForm, self).clean()
        password = cleaned_data.get('password', '')
        username = cleaned_data.get('username', '')

        # do some verify stuff

        return cleaned_data


class UserLoginForm(forms.Form):
    ''' 用户登录表单 '''

    username = forms.CharField(
                                min_length=5,
                                max_length=20,
                                required=True
                            )
    password = forms.CharField(
                                min_length=5,
                                max_length=20,
                                required=True
                            )

    def clean(self):
        cleaned_data = super(UserLoginForm, self).clean()
        username = cleaned_data.get('username', '')
        password = cleaned_data.get('password', '')

        user = auth.authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError('wrong u | p')

        return cleaned_data
