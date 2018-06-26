# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 13:12:14 2018

@author: prateek
"""

from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]