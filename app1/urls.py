# -*- coding: utf-8 -*-
# @Time    : 2020/5/10 16:14
# @Author  : Lixun
# @Email   : lixunpost@163.com
# @File    : urls.py
# @Software: PyCharm

from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.index_view)
]