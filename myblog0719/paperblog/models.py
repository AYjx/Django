#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Author: YJX
from django.db import models
from django.contrib.auth.models import User

class BArticle(models.Model):
    Btitle = models.CharField(max_length=32, default='blog title')
    Bauthor = models.ForeignKey(User, related_name="blog_posts", on_delete=models.CASCADE, null=True)
    Bcontent = models.TextField(null=True)
    # 发布时间，auto_now=True——在创建对象时，将publish_time自动设置为当前时间
    Bpublish_time = models.DateTimeField(null=True)

    class Meta:
        ordering = ("-Bpublish_time",)

    def __str__(self):
        return self.Btitle


class Article(models.Model):
    title = models.CharField(max_length=32, default='blog title')
    content = models.TextField(null=True)
    # 发布时间，auto_now=True——在创建对象时，将publish_time自动设置为当前时间
    publish_time = models.DateTimeField(null=True)

    def __str__(self):
        return self.title
