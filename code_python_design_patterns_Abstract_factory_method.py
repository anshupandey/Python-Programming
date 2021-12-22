# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 14:09:43 2021

@author: anshu
"""

# =============================================================================
# Abstract Factory methods  - factory of factories 
# - widely to combine multiple objects of same family together to create objects with 
# a uniform method.
# 
# =============================================================================

# web app

class webapp:
    __title = ""
    __purpose = ""
    
    def __init__(self,title,purpose):
        self.__title = title
        self.__purpose = purpose
        
    def gettitle(self):
        return self.__title
    
    def getpurpose(self):
        return self.__purpose
    
class appmenu(webapp):
    def __init__(self):
        webapp.__init__(self,"My Website",'main menu')

class appbanner(webapp):
    def __init__(self):
        webapp.__init__(self,"My Website",'Home Page Banner')

class appcontent(webapp):
    def __init__(self):
        webapp.__init__(self,"My Website",'Home Page content')

class appfooter(webapp):
    def __init__(self):
        webapp.__init__(self,"My Website",'Home page footer')
        
# Abstract Factory class
class UIFactory:
    def get_appmenu(self):
        return appmenu()
    
    def get_appbanner(self):
        return appbanner()
    
    def get_appcontent(self):
        return appcontent()
    
    def get_appfooter(self):
        return appfooter()
    
    
ui = UIFactory()

print(ui.get_appbanner().getpurpose())

print(ui.get_appcontent().getpurpose())

print(ui.get_appfooter().getpurpose())
