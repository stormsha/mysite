#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
@author: stormsha
@license: (C) Copyright 2020-2021, Node Supply Chain Manager Corporation Limited.
@contact: 1414749109@qq.com
@software: garner
@file: urls.py
@time: 6/27/2020 12:04 AM
@desc:
"""

from django.conf.urls import url
from .views import IndexView, about_view, message_view

urlpatterns = [
    # 首页
    url(r'^$', IndexView.as_view(template_name='index.html'), name='index'),  # 主页，自然排序
    url(r'^category/about/$', about_view, name='about'),
    url(r'^category/message/$', message_view, name='message'),
    # 分类页面
    url(r'^category/(?P<big_slug>.*?)/(?P<slug>.*?)', IndexView.as_view(template_name='base/content.html'), name='category'),
    # 归档页面
    url(r'^(?P<year>\d+)/(?P<month>\d+)', IndexView.as_view(template_name='base/content.html'), name='date'),
    # 标签页面
    url(r'^tag/(?P<tag>.*?)/$', IndexView.as_view(template_name='base/content.html'), name='tag'),
]
