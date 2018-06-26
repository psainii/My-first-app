# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 13:12:14 2018

@author: prateek
"""

from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
]