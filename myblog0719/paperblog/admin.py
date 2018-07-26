#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Author: YJX
from django.contrib import admin

from .models import BArticle
from .models import Article

# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ('title', 'content', 'publish_time')
#     list_filter = ('publish_time',)

admin.site.register(Article)

admin.site.register(BArticle)

