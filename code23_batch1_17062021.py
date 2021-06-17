# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 12:20:32 2021

@author: Nitu
"""

# to create a django project
# execute following on cmd
# django-admin startproject myblog


# run the server with default page
# python manage.py runserver

# perform the migration
# python manage.py migrate


# creating an app inside a django project
# python manage.py startapp main_website

#########################################
# steps for integrating webpages with django app

# step 1 - creating an app inside a django project
# python manage.py startapp main_website

# step2
# make changes in settings.py of your project and add name of app to installed apps

# step3
# modify views.py of the app by adding two functions
def homepage(request):
    return render(request,"index.html",{})
def contact(request):
    return render(request,"contact.html",{})

# step 4 - create index.html and contact.html

#step 5 -update urls.py of the project
from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include('main_website.urls')),
]

#step 6 - create a new file urls.py with in the appfrom django.urls import path
from main_website import views
urlpatterns = [
    path("",views.homepage,name="homepage"),
    path("contact",views.contact,name="contact"),
    ]