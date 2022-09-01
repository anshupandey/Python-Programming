# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 13:51:14 2022

@author: admin
"""

# Prototype

import copy

class prototypeCar:
    _type = None
    _price = None
    
    def getType(self):
        return self._type
    
    def getPrice(self):
        return self._price
    
    def clone(self):
        return copy.copy(self)
    
# create derived class

class sedan(prototypeCar):
    def __init__(self,price):
        self._type = "Sedan"
        self._price = price
        
class hatchback(prototypeCar):
    def __init__(self,price):
        self._type = "Hatchback"
        self._price = price
        

class carFactory:
    _type1 = None
    _type2 = None
    
    @staticmethod 
    def start():
        carFactory._type1 = sedan(450000)
        carFactory._type2 = hatchback(561245)
        
    @staticmethod 
    def getSedanCopy():
        return carFactory()._type1.clone()
    
    @staticmethod 
    def getHatchbackCopy():
        return carFactory()._type2.clone()
        
    
carFactory.start()

a1 = carFactory.getSedanCopy()
print(a1._type, a1._price)

a2 = carFactory.getHatchbackCopy()
print(a2._type,a2._price)


#########################################

x = 5
k = copy.copy(x)
id(k)
id(x)
k = 12
print(x,k)

###################################################

q = [4,5,3]
p = copy.copy(q)
id(p)
id(q)
