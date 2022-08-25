# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 14:13:10 2022

@author: admin
"""

# total ordering

from functools import total_ordering 

@total_ordering 
class employee:
    def __init__(self,name,age):
        self.age = age
        self.name = name
        
    def __eq__(self,val):
        return self.age==val 
    
    def __lt__(self,val):
        return self.age<val
    
    
e = employee("Anshu",45)

e<45 
e>12 
e==55
e!=45
e>=16
e<=96 
