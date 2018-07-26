#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Author: YJX
"""views.py 即为django的后台代码"""
from django.shortcuts import render
from django.http import HttpResponse
import datetime
from . import models

def index(request):
    nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # all()--返回结果是Python内置的集合对象（可理解为列表）
    articles = models.Article.objects.all()
    return render(request, 'index.html', {'articles': articles})

def article_page(request, article_id):
    """获取文章详情"""
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'article_page.html', {'article': article})

def edit_page(request, article_id):
    """跳转到文章编辑页面，根据文章id判断是新建文章（id=0）还是修改文章（文章存在，id从1开始）"""
    if str(article_id) == '0':
        return render(request, 'edit_page.html')
    else:
        article = models.Article.objects.get(pk=article_id)
        return render(request, 'edit_page.html',  {'article': article})

def edit_action(request):
    """文章编辑页面的操作，文章id=1：创建文章；id不等于1：先获取文章标题、内容，然后修改为新的标题和内容"""
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')
    article_id = request.POST.get('article_id', '0')
    if str(article_id) == '0':
        models.Article.objects.create(title=title, content=content)
        articles = models.Article.objects.all()
        return render(request, 'index.html', {'articles': articles})
    else:
        article = models.Article.objects.get(pk=article_id)
        article.title = title
        article.content = content
        article.save()
        return render(request, 'article_page.html', {'article': article})