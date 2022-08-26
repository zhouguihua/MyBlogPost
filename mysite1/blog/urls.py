#!/user/bin/env python
# -*- coding:utf-8 -*-
# 作者：周桂华
# 开发时间: 2022/8/24 22:30
from django.urls import path

from . import views

urlpatterns = [
    path("", views.archive, name='index'),
    path("create/", views.create_blogpost, name='create_blog'),
]