# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 18:34:04 2021

@author: Nitu
"""

# Working with Django
# install django = pip install django

# start creating a project - run the command on cmd
# django-admin startproject myblog

# run the project server
# python manage.py runserver

##################################################################

# step1 - create an app - run the following command on cmd
# python manage.py startapp main_website

# step 2 - modify views.py of the app add two functions to render html files
def homepage(request):
    return render(request,"index.html",{})
def contact(request):
    return render(request,"contact.html",{})

# step3 - modify settings.py of the project to register the app - add the name of app 
# in the installed apps section

# step4 - create a folder with name - templates  inside the main_wwebsite app folder
#and create index.html & contact.html

# step5 modify urls.py of the main project
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('main_website.urls')),
]

#step 6 - create urls.py in the app main_website and attach urls
from django.urls import path
from main_website import views
urlpatterns = [
    path("",views.homepage,name="homepage"),
    path("contact",views.contact,name="contact"),
    ]


