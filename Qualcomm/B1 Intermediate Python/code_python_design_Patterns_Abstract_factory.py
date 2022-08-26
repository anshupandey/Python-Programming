# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 09:50:01 2022

@author: admin
"""

class swift:    
    def price(self):
        return 450000
    
    def __str__(self):
        return "Maruti Suzuki Swift Dzire 349"
    
class hyundai:    
    def price(self):
        return 7845421
    
    def __str__(self):
        return "Hyndai i20 grand"

class kia:    
    def price(self):
        return 98654512
    
    def __str__(self):
        return "Kia Seltos"
    
    
s = swift()
print(f"the price for the car {s} is {s.price()}")

k = kia()
print(f"the price for the car {k} is {k.price()}")

##################################################

class AbstractFactory:
    def __init__(self,obj):
        self.obj = obj
        
    def get_details(self):
        car = self.obj()
        print(f"The price for the car {car} is {car.price()}")
        

k = AbstractFactory(kia)
k.get_details()

s = AbstractFactory(swift)
s.get_details()

type(k)


###############################################################


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