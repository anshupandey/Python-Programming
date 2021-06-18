# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 19:29:25 2021

@author: Nitu
"""
from django.urls import path
from main_website import views
urlpatterns = [
    path("",views.homepage,name="homepage"),
    path("contact",views.contact,name="contact"),
    ]
