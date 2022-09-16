# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 13:40:57 2022

@author: admin
"""

# =============================================================================
# Singleton - limiting the number of objects to 1 
# 
# =============================================================================


class singletonclass:
    __inst = "abc"
    
    def __init__(self):
        if singletonclass.__inst =="abc":
            singletonclass.__inst = self
        else:
            raise Exception(" This class is a singleton class")
            
    @staticmethod 
    def getinstance():
        if singletonclass.__inst=="abc":
            singletonclass()
        return singletonclass.__inst
        
    
k = singletonclass()
id(k)        
m = singletonclass()

w = singletonclass.getinstance()
id(k)
id(w)
