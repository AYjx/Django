#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Author: YJX

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    # (?P<article_id>[0-9]+)--将正则表达式匹配到的数字以article_id作为组名；article_id必须和views.py中的响应函数article_page(request, article_id)中的参数一致
    url(r'^article/(?P<article_id>[0-9]+)$', views.article_page, name='article_page'),
    url(r'^edit/(?P<article_id>[0-9]+)$', views.edit_page, name='edit_page'),
    url(r'^edit_action/$', views.edit_action, name='edit_action'),
]