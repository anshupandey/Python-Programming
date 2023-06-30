# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 11:59:22 2022

@author: admin
"""

import copy

class baseCar:
    _type = None
    _value = None
    
    def getType(self):
        return self._type 
    
    def getValue(self):
        return self._value
    
    def clone(self):
        return copy.copy(self)
    
    

class Sedan(baseCar):
    def __init__(self,price):
        self._type = "sedan"
        self._value = price
        
class hatchback(baseCar):
    def __init__(self,price):
        self._type = "hatchback"
        self._value = price
        
class carFactory:
    _type1 = None
    _type2 = None 
    
    @staticmethod 
    def start():
        carFactory._type1 = Sedan(45000)
        carFactory._type2 = hatchback(785200)
        
    @staticmethod 
    def gettype1():
        return carFactory()._type1.clone()
    
    @staticmethod 
    def gettype2():
        return carFactory()._type2.clone()
    
carFactory.start()
        
        
c1 = carFactory.gettype1()
print(c1.getType(),c1.getValue())


c2 = carFactory.gettype2()
print(c2.getType(),c2.getValue())

