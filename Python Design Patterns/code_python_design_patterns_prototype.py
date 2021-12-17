# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 10:38:09 2021

@author: anshu
"""
# prototype design pattern

import copy

class prototype:
    _type = None
    _value = None
    
    def clone(self):
        pass
    
    def getType(self):
        return self._type
    
    def getValue(self):
        return self._value
    
    
class Type1(prototype):
    def __init__(self,number):
        self._type = "Type1"
        self._value = number
        
    def clone(self):
        return copy.copy(self)
    
class Type2(prototype):
    def __init__(self,number):
        self._type = "Type2"
        self._value = number
        
    def clone(self):
        return copy.copy(self)
    
class FactoryObject:
    _type1v = None
    _type2v = None
    
    @staticmethod
    def start():
        FactoryObject._type1v = Type1(10)
        FactoryObject._type2v = Type2(20)
    
    @staticmethod
    def gettype1():
        return FactoryObject()._type1v.clone()
    
    @staticmethod
    def gettype2():
        return FactoryObject()._type2v.clone()
    
FactoryObject.start()
ins1 = FactoryObject.gettype1()
print(ins1.getType(),ins1.getValue())

ins2 = FactoryObject.gettype2()
print(ins2.getType(),ins2.getValue())

