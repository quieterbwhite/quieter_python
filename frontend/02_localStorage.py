# -*- coding=utf-8 -*-
# Created Time: 2017年08月03日 星期四 13时40分06秒
# File Name: 02_localStorage.py

LocalStorage 是 HTML5 window 的一个属性，有5MB大小，足够了。

window.localStorage.setItem("name", "tiger");

var verb = window.getItem("name");

window.localStorage.removeItem("name");

由于 vuex 里面, 我们保存的状态都是数组，而 localStorage 只支持字符串，
所以需要用 JSON 转换:

    JSON.stringify(state.subscribeList); // array -> string

    JSON.parse(window.localStorage.getItem("name"));  // sting -> array
