# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.views import generic


# Create your views here.
class IndexView(generic.ListView):
    """
        首页视图,继承自ListVIew，用于展示从数据库中获取的文章列表
    """

    def get_queryset(self):
        # 重写通用视图的 get_queryset 函数，获取定制数据
        queryset = None
        return queryset


def about_view(request):
    return render(request, 'about.html', {'category': 'about'})


def message_view(request):
    return render(request, 'message.html', {'category': 'message'})
